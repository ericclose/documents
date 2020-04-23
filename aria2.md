# Aria2

- [Aria2](#aria2)
  - [连接 VPS](#%e8%bf%9e%e6%8e%a5-vps)
  - [安装 aria2](#%e5%ae%89%e8%a3%85-aria2)
  - [编辑配置文件](#%e7%bc%96%e8%be%91%e9%85%8d%e7%bd%ae%e6%96%87%e4%bb%b6)
  - [使用 systemd 管理 aria2](#%e4%bd%bf%e7%94%a8-systemd-%e7%ae%a1%e7%90%86-aria2)
  - [通过 WebUI 调用 Aria2](#%e9%80%9a%e8%bf%87-webui-%e8%b0%83%e7%94%a8-aria2)
  - [Nginx 搭建 HTTP 文件服务](#nginx-%e6%90%ad%e5%bb%ba-http-%e6%96%87%e4%bb%b6%e6%9c%8d%e5%8a%a1)
  - [配置访问密码](#%e9%85%8d%e7%bd%ae%e8%ae%bf%e9%97%ae%e5%af%86%e7%a0%81)

## 连接 VPS

```bash
ssh user@127.0.0.1
```

## 安装 aria2

```bash
sudo apt install aria2
```

## 编辑配置文件

```bash
mkdir ~/.aria2
touch ~/.aria2/aria2.session
vim ~/.aria2/aria2.conf
```

> 在本文中，我提供了一个可直接使用的配置文件样本，你可以粘贴至 aria2.conf 文件内，注意修改 rpc-secret 为自己喜欢的密码。如果在上一步操作中选择了其它文件路径，不要忘了修改哦。

```conf
# 文件的保存路径（可自行修改）
dir=/home/user/Downloads
# 启用磁盘缓存, 0为禁用缓存
disk-cache=32M
# 文件预分配方式, 能有效降低磁盘碎片
file-allocation=none
# 断点续传
continue=true
# 最大同时下载任务数, 运行时可修改
max-concurrent-downloads=5
# 同一服务器连接数, 添加时可指定
max-connection-per-server=16
# 最小文件分片大小, 添加时可指定
min-split-size=20M
# 单个任务最大线程数, 添加时可指定
split=5
# 整体下载速度限制, 运行时可修改
# max-overall-download-limit=0
# 单个任务下载速度限制
# max-download-limit=0
# 整体上传速度限制, 运行时可修改
# max-overall-upload-limit=0
# 单个任务上传速度限制
# max-upload-limit=0
# 禁用IPv6
disable-ipv6=true
# 从会话文件中读取下载任务
input-file=/home/user/.aria2/aria2.session
# 退出时保存`错误/未完成`的下载任务到会话文件
save-session=/home/user/.aria2/aria2.session
# 定时保存会话, 0为退出时才保存
# save-session-interval=60
# 启用RPC
enable-rpc=true
# 允许所有来源
rpc-allow-origin-all=true
# 允许非外部访问
rpc-listen-all=true
# 事件轮询方式, 取值:[epoll, kqueue, port, poll, select]
# event-poll=select
# RPC监听端口, 端口被占用时可以修改
rpc-listen-port=6800
# 设置的RPC授权令牌
rpc-secret=hello
# 当下载的是一个种子(以.torrent结尾)时, 自动开始BT任务
# follow-torrent=true
# BT监听端口, 当端口被屏蔽时使用
listen-port=6881-6999
# 单个种子最大连接数
# bt-max-peers=55
# 打开DHT功能, PT需要禁用
enable-dht=false
# 打开IPv6 DHT功能, PT需要禁用
# enable-dht6=false
# DHT网络监听端口
# dht-listen-port=6881-6999
# 本地节点查找, PT需要禁用
# bt-enable-lpd=false
# 种子交换, PT需要禁用
enable-peer-exchange=false
# 每个种子限速
# bt-request-peer-speed-limit=50K
# 客户端伪装, PT需要
peer-id-prefix=-TR2770-
user-agent=Transmission/2.77
# 当种子的分享率达到这个数时, 自动停止做种, 0为一直做种
seed-ratio=1.0
# 强制保存会话, 即使任务已经完成
# force-save=false
# BT校验相关, 默认:true
# bt-hash-check-seed=true
# 继续之前的BT任务时, 无需再次校验
bt-seed-unverified=true
# 保存磁力链接元数据为 .torrent 文件
bt-save-metadata=true
# 启用后台进程
daemon=true
```

## 使用 systemd 管理 aria2

```bash
sudo vim /etc/systemd/system/aria2.service
```

将下列内容复制进去：

```conf
[Unit]
Description=Aria2 Daemon

[Service]
Type=forking
ExecStart=/usr/bin/aria2c --conf-path=/home/user/.aria2/aria2.conf

[Install]
WantedBy=default.target
```

开启并将 aria2 设为开机自启：

```bash
sudo systemctl enable aria2.service --now
```

## 通过 WebUI 调用 Aria2

安装 nginx

```bash
sudo apt install nginx
```

Nginx 的默认 web 根目录是 /var/www/html ，所以我选择部署 webui-aria2 到 /var/www/html/webui-aria2 下。

```
cd /var/www/html
sudo git clone https://github.com/ziahamza/webui-aria2.git
sudo systemctl restart nginx
```

* Aria2 WebUI 网址: http://127.0.0.1/webui-aria2/docs

---

以上只是配置了 WebUI 调用 aria2 下载文件到 VPS 上，接下来设置文件取回。你可以使用 ftp 取回文件，也可以使用其他轻量级 http 服务器应用取回。这里演示使用 nginx 生成 HTTP 文件服务。

## Nginx 搭建 HTTP 文件服务

这里使用另一个端口号（7080）做文件服务器，若要访问下载目录，在浏览器输入 [主机IP地址或域名]:7080 访问。

* 在 `/etc/nginx/sites-available/` 下新建一个站点配置

```bash
cd /etc/nginx/sites-available/
sudo touch aria2File # 创建一个名为aria2File的站点配置
```

* `sudo vim aria2File` ，输入一下内容：

```
server {
        listen 7080 default_server;
        listen [::]:7080 default_server;
        root /home/user/Downloads;   # 这里使用下载文件夹的绝对路径
        server_name _;
        auth_basic "Authorization needed";
        auth_basic_user_file /var/www/auth/auth4aria2File;  # 设置要求密码登陆
        location / {
                # 使nginx自动生成文件列表
                autoindex on;
                autoindex_exact_size on;
                autoindex_localtime on;
        }
}
```

* 然后创建配置文件的软链接，开启站点配置：

```bash
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/aria2File ./aria2File
```

最后 `sudo vim /etc/nginx/nginx.conf` ，修改 nginx 配置文件首行的内容如下：

```bash
# user www-data;
user root;  # 或者其他具有下载文件夹访问权限的用户名称
```

从而避免因默认的 www-data 用户无权访问下载文件夹导致的 403 错误。

## 配置访问密码

上面我们在 aria2File 站点配置文件中写了一行 `auth_basic_user_file /var/www/auth/auth4aria2File; # 设置要求密码登陆` ，所以这里我们在对应位置也要生成一个访问验证文件。

```bash
sudo apt install apache2-utils
sudo mkdir -p /var/www/auth/
cd /var/www/auth/
sudo htpasswd -c ./auth4aria2File admin
```

`$USERNAME` 改为你想要的登录用户名。

然后根据提示设置密码，生成文件 `auth4aria2File` 。

* 获取文件网址: http://127.0.0.1:7080