# 初次配置


1. 对Linux 进行更新
* 对安装的Kali Linux 清除安装包缓存、更新apt-get源文件、软件升级和发行版升级执行命令

```bash
apt-get clean && apt-get update && apt-get upgrade && apt-get dist-upgrade -y
```

2. 添加用户
* 新建用户user并指定用户的家目录为/home

```bash
useradd -m user
```

* 设置新用户的密码

```bash
passwd user
```

3. 将用户添加进sudo用户组
// -a 附加组 -G 指定一个群组 或者多个群组

```bash
usermod -a -G sudo user
```

4. 修改更新源

```bash
#
#deb cdrom:[Debian GNU/Linux 7.0 Kali - Official Snapshot amd64 LIVE/INSTALL Binary 20150312-17:50]/ kali contrib main non-free

#deb cdrom:[Debian GNU/Linux 7.0 Kali - Official Snapshot amd64 LIVE/INSTALL Binary 20150312-17:50]/ kali contrib main non-free

deb http://http.kali.org/kali moto main non-free contrib
deb-src http://http.kali.org/kali moto main non-free contrib

deb http://security.kali.org/ moto/updates main contrib non-free
deb-src http://security.kali.org/ moto/updates main contrib non-free

#中科大kali源
deb http://mirrors.ustc.edu.cn/kali kali main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali main non-free contrib
deb http://mirrors.ustc.edu.cn/kali-security kali/updates main contrib non-free

#新加坡kali源
deb http://mirror.nus.edu.sg/kali/kali/ kali main non-free contrib
deb-src http://mirror.nus.edu.sg/kali/kali/ kali main non-free contrib
deb http://security.kali.org/kali-security kali/updates main contrib non-free
deb http://mirror.nus.edu.sg/kali/kali-security kali/updates main contrib non-free
deb-src http://mirror.nus.edu.sg/kali/kali-security kali/updates main contrib non-free

#阿里云kali源
deb http://mirrors.aliyun.com/kali kali main non-free contrib
deb-src http://mirrors.aliyun.com/kali kali main non-free contrib
deb http://mirrors.aliyun.com/kali-security kali/updates main contrib non-free

#163 Kali源
deb http://mirrors.163.com/debian wheezy main non-free contrib
deb-src http://mirrors.163.com/debian wheezy main non-free contrib
deb http://mirrors.163.com/debian wheezy-proposed-updates main non-free contrib
deb-src http://mirrors.163.com/debian wheezy-proposed-updates main non-free contrib
deb-src http://mirrors.163.com/debian-security wheezy/updates main non-free contrib
deb http://mirrors.163.com/debian-security wheezy/updates main non-free contrib
#auto
deb http://http.kali.org/kali kali-rolling main non-free contrib

#中科大
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

#浙大
deb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free
deb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free

#东软大学
deb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib
deb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib

#重庆大学
deb http://http.kali.org/kali kali-rolling main non-free contrib
deb-src http://http.kali.org/kali kali-rolling main non-free contrib

#官方源
#deb http://http.kali.org/kali kali-rolling main non-free contrib
#deb-src http://http.kali.org/kali kali-rolling main non-free contrib
```

# 常见问题

1. ssh 配置(虚拟机遇到 ssh -T git@github.com 错误添加`IPQoS=throughput`即可)

```bash
# 需要修改的文件是/etc/ssh/ssh_config
Host *
    IPQoS=throughput
```

2. 如果能 ping 通 ip 地址，但是不能通过浏览器输入域名访问相关网页，则很可能是域名解析出了问题。
这时需要配置域名解析服务器的 ip 地址。
用 Kali Linux 的内置文本编辑器 `leafpad` 打开 `/etc/resolv.conf`

```bash
leafpad /etc/resolv.conf
```

添加 DNS 解析服务器的 ip 地址，此处添加Google 解析服务器的 ip 地址，做域名解析的时候是有先后顺序的。

```bash
nameserver 8.8.8.8
nameserver 8.8.4.4
```

如果发现保存不了，则将其删除：

```bash
sudo rm /etc/resolv.conf
```

重新建立一个 resolv.conf 文件，重复刚才的过程，保存文件即可解决问题。

# 常见问题

* root 用户居然打不开内置的 Chromium



Kali Linux 没有内置中文输入法的情况下，你会想到哪个输入法呢？ 我选择Fcitx~
<!-- more -->

![优雅的输入中文](https://github.com/ericclose/images/raw/master/install-chinese-ime.jpg)

# Kali Linux 如何安装 Fcitx

## 敲命令

1. 首先确保您的软件包列表是最新的
`apt-get update`
2. 安装`fcitx-googlepinyin`
`apt-get install fcitx fcitx-googlepinyin`
3. 安装配置工具`fcitx-config-gtk2`
`apt-get install fcitx-config-gtk2`
4. 立即重启
`reboot now`

## 美化

Github 上有一个漂亮的Material Design 风格的皮肤，你可以来[这里](https://github.com/ootaharuki99/fcitx-skin-material)下载，然后将`material`文件夹移动到`/usr/share/fcitx/skin/`目录下，托盘图标右键 skin 即可换皮肤。

>  * 托盘的图标太亮。将/usr/share/fcitx/skin/classic/目录下的 active.png 和 inactive.png 复制到/usr/share/fcitx/skin/material/目录，替换即可。
>  * 字体太大，输入英文时颜色不好分辨。修改 material 主题目录下的 fcitx_skin.conf 文件：

```bash
FontSize=11
MenuFontSize=10
TipColor=220 220 220
InputColor=170 170 170
```

## Sublime Text 3 Fcitx 中文输入法问题

解决方法： 参见 [lyfeyaj](https://github.com/lyfeyaj) 的仓库 `sublime-text-imfix`  [README.md](https://github.com/lyfeyaj/sublime-text-imfix/blob/master/README.md)



我们把下载的图标移动至Electronic WeChat文件夹下的resources文件夹中

接下来我们来给微信添加一个桌面启动器，类似于Windows下的快捷方式，方便我们随时启动，在Kali Linux中我们使用如下命令创建一个配置文件（文件后缀为.desktop）

`vi /usr/share/applications/electronic-wechat.desktop`

接着我们向该文件中添加如下内容：

```bash
[Desktop Entry]
Name=Electronic Wechat
Name[zh_CN]=微信电脑版
Name[zh_TW]=微信电脑版
Exec=/opt/electronic-wechat/electronic-wechat
Icon=/opt/electronic-wechat/resources/electronic-wechat.png
Terminal=false
X-MultipleArgs=false
Type=Application
Encoding=UTF-8
Categories=Application;Utility;Network;InstantMessaging;
StartupNotify=false
```

保存并退出后，就可以看见你的微信出现在软件菜单里了，也可以添加收藏在dock中显示，就这么简单，愉快的享用吧～～
