# 安装 Chrome

```bash
su -
yum update
vi /etc/yum.repos.d/google-chrome.repo
```

`/etc/yum.repos.d/google-chrome.repo` 的内容如下：

```bash
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub
```

安装 Chrome 稳定版

```bash
yum install google-chrome-stable
```

# 美化
## theme / icon
`~/.themes` , `~/.icons`
## extensions
`~/.local/gnome-shell/extensions`
## panel
`/usr/share/gnome-shell/modes/classic.json`

# 安装 AnyDesk

```bash
wget https://download.anydesk.com/linux/rhel7/anydesk-4.0.1-1.el7.x86_64.rpm
sudo yum localinstall -y anydesk-4.0.1-1.el7.x86_64.rpm
```

# 安装TeamViewer

```bash
wget https://download.teamviewer.com/download/linux/signature/TeamViewer2017.asc
rpm --import TeamViewer2017.asc
                                       # assuming 64bit Workstation
wget https://download.teamviewer.com/download/linux/teamviewer.x86_64.rpm
yum install epel-release               # must be installed first
yum install ./teamviewer.x86_64.rpm --enablerepo="cr"
```

# 编译安装 Shadowsocks-libev
## Get the latest source code

```bash
git clone https://github.com/shadowsocks/shadowsocks-libev.git
cd shadowsocks-libev
git submodule update --init --recursive
```

## Build from source
### prequirement：

```bash
su -
yum install epel-release -y
yum install gcc gettext autoconf libtool automake make pcre-devel asciidoc xmlto c-ares-devel libev-devel libsodium-devel mbedtls-devel -y
```

### 开始进行编译：

```bash
./autogen.sh && ./configure --prefix=/usr && make
make install
```

```bash
vi ~/shadowsocks.json
```

### 清除旧的内核

```bash
package-cleanup --oldkernels --count=1
```

### 安装 privoxy

```bash
yum -y install privoxy
```

### 配置 socks5 全局代理

```bash
echo 'forward-socks5 / 127.0.0.1:1080 .' >> /etc/privoxy/config
```

### 使用

```bash
ss-local ~/shadowsocks.json
export http_proxy=http://127.0.0.1:8118 && export https_proxy=http://127.0.0.1:8118 && systemctl start privoxy
```

### 停用

### 设置开机自启
每次开机都要手动在终端启动一个线程，忘了还上不了网，这是让人很烦的，所以这里设置一下让它开机自动启动sslocal。

编辑/etc/rc.local文件，没有就创建一个，添加以下内容：

```bash
#!/bin/sh -e
sslocal -c /etc/shadowsocks.json&
exit 0
```
登出测试，如果能直接打开网页，则说明已经成功了。

使用Systemd来实现Shadowsocks开机自启

```bash
sudo emacs /etc/systemd/system/shadowsocks.service

[Unit]
Description=Shadowsocks Client Service
After=network.targe

[Service]
Type=simple
User=root
ExecStart=/usr/bin/sslocal -c /etc/shadowsocks.json

[Install]
WantedBy=multi-user.target
```
让配置生效：

```bash
systemctl enable /etc/systemd/system/shadowsocks.service
```
然后就好了。

## 创建桌面快捷方式

```bash
unset http_proxy && unset https_proxy && systemctl stop privoxy && pkill ss-local
```

```bash
Settings --> Network --> Network Proxy --> Manual --> Socks Host: 127.0.0.1:1080

Open the file browser (the "home" folder shortcut is on the desktop by default)

Click the "Computer" link on the left navigation panel and go to "/usr/shared/applications". This should now display all the applications icons/shortcuts in the browser window.

Now here, I first tried dragging the Terminal icon over to the desktop, but got an error due to permissions (Error setting owner: Operation not permitted), (Any input on this would be appreciated).

Instead do "Right-click Icon->Context Menu->Copy To". This will bring up another browser window titled "Select Destination".

Select (left-click) the "Desktop" folder in the left navigation panel, and the click the "Select" button in the bottom right.

The Application icon should now be on the desktop! Sure it's not as easy as simple drag-and-drop functionality that was present before, but at least it works(?).
```
