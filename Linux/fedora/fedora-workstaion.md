## Fedora Workstation 配置

### 自启动 sshd 服务

```bash
sudo systemctl enable --now sshd
```

---

### Nvidia

## Determining your card model

<!-- NVIDIA has several driver series, each of which has different hardware support. To determine which driver you need to install, you'll first need to find your graphics card model.

If you don't know it, open a Terminal (Applications > System Tools > Terminal) and type:

```bash
/sbin/lspci | grep -e VGA
```

You can also check the [supported chips](https://download.nvidia.com/XFree86/Linux-x86_64/495.44/README/supportedchips.html) section and see which series is recommended for you card, then install the appropriate driver series. Please remember that you need additional steps for optimus.

You are probably in the [Optimus](https://rpmfusion.org/Howto/Optimus) case if your NVIDIA card is found with the next command:

```bash
/sbin/lspci | grep -e 3D
```

## Installing the drivers

Please remember that once the driver is installed, there is no need to configure xorg.conf by default. Changes will take effect after a ***full reboot*** on the newest kernel.

⚠️ The ***Secure Boot*** Please have a look on [Howto/Secure Boot](https://rpmfusion.org/Howto/Secure%20Boot) in order to sign the nvidia kmod. You will have to enter the BIOS/EFI to import your self generated key.

### Current GeForce/Quadro/Tesla

Supported on current stable Xorg server release.

This driver is suitable for any GPU found in 2014 and later.

⚠️ The 510+ driver is available by default on Fedora 34+ and later and has dropped support for some older Kepler GPU.

```bash
sudo dnf update -y # and reboot if you are not on the latest kernel
sudo dnf install akmod-nvidia # rhel/centos users can use kmod-nvidia instead
sudo dnf install xorg-x11-drv-nvidia-cuda #optional for cuda/nvdec/nvenc support
```

⚠️ Please remember to wait after the RPM transaction ends, until the kmod get built. This can take up to 5 minutes on some systems.

Once the module is built, "`modinfo -F version nvidia`" should outputs the version of the driver such as 440.64 and not modinfo: ERROR: Module nvidia not found. -->

```bash
# Make sure the Nvidia graphic card is present 
lspci | grep -E '3D|VGA'

# 进入 BIOS，关掉安全启动
sudo systemctl reboot --firmware-setup

# 1. Go to the Gnome Software
# 2. Software Repositories, then enable *Nvidia Driver
# 3. Install the NVIDIA Linux Graphics Driver
# 4. Reboot once as normal, then 进入 BIOS，Enable Secure Boot
sudo systemctl reboot --firmware-setup
# 5. Reboot, and check the kernel modules works or not
lsmod | grep -E 'nvidia|nouveau'
```

---

### Vim

```bash
sudo dnf install vim
```

---

### clash

<!-- ```bash
# su - root
# gzip -dc clash*.gz > /usr/local/bin/clash
# chmod +x /usr/local/bin/clash
# mkdir /etc/clash
# curl -L https://github.com/Dreamacro/maxmind-geoip/releases/latest/download/Country.mmdb > /etc/clash/Country.mmdb
# curl 订阅链接 > /etc/clash/config.yaml

# vim /etc/systemd/system/clash.service
```

```ini
[Unit]
Description=Clash daemon, A rule-based proxy in Go.
After=network.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/local/bin/clash -d /etc/clash

[Install]
WantedBy=multi-user.target
```

```bash
git clone -b gh-pages --depth 1 https://github.com/Dreamacro/clash-dashboard /opt/clash-dashboard
```

```bash
vim /etc/clash/config.yaml
```

```yaml
......
external-ui: /opt/clash-dashboard
......
``` -->

```bash
curl https://api.github.com/repos/MetaCubeX/mihomo/releases/latest | grep browser_download_url | awk -F '"' '{ printf $4 "\n" }' | grep -E 'linux.*amd64.*rpm'
sudo dnf install ./mihomo-linux-amd64-*.rpm

sudo bash -c "curl 订阅链接 > /etc/mihomo/config.yaml"
sudo sed -i -e 's|127.0.0.1:9090|0.0.0.0:9090|g' -e 's|# external-ui: folder|external-ui: /etc/mihomo/ui|g' /etc/mihomo/config.yaml

sudo git clone https://github.com/metacubex/metacubexd.git -b gh-pages /etc/mihomo/ui
# Update
git -C /etc/mihomo/ui pull -r

sudo systemctl start mihomo.service && sleep 15s && systemctl status mihomo.service
```

**服务**

```bash
# 因为 Fedora 默认启用 cockpit，占用 9090 端口，与 clash-dashboard 端口冲突，故禁用之
sudo systemctl disable --now cockpit.socket

# 因 systemd-reslove 服务占用 9090 端口，与 clash 的 DNS 端口冲突，故禁用之
sudo systemctl disable --now systemd-resolved.service
```

**防火墙**

```bash
# allow port 9090/tcp for clash external controller
sudo firewall-cmd --permanent --add-port=9090/tcp
sudo firewall-cmd --reload
```

---

### RPM Fusion

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

---

### qq

```bash
flatpak install --user flathub com.qq.QQ

# icalingua
# sudo dnf install https://github.com/Icalingua-plus-plus/Icalingua-plus-plus/releases/download/v2.6.2/icalingua-2.6.2.x86_64.rpm
```

### wechat

```bash
# v21.08
git clone https://github.com/catsout/flatpak-wechat.git
flatpak remote-add --if-not-exists --user flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install --user org.electronjs.Electron2.BaseApp
flatpak install --user org.freedesktop.Sdk
sudo dnf install flatpak-builder
make -j$(nproc)
make install
```

### TencentMeeting

```bash
flatpak install --user flathub com.tencent.wemeet
```
