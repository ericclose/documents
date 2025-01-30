## Fedora Workstation 配置

### Nvidia

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

sudo dnf -y install xorg-x11-drv-nvidia-cuda

# 查看英伟达显卡使用情况
$ nvidia-smi
Thu Jan 30 18:49:31 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 565.77                 Driver Version: 565.77         CUDA Version: 12.7     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    Off |   00000000:01:00.0 Off |                  N/A |
| N/A   57C    P0             25W /   85W |    1922MiB /   8188MiB |      3%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2563      G   /usr/bin/gnome-shell                            2MiB |
|    0   N/A  N/A      6263    C+G   ....local/share/Steam/logs/cef_log.txt          6MiB |
|    0   N/A  N/A      6792    C+G   ...Become Human\DetroitBecomeHuman.exe       1762MiB |
+-----------------------------------------------------------------------------------------+
```

---

### Vim

```bash
sudo dnf install vim
```

---

### clash

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

---

### RPM Fusion

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

---

### VLC

```bash
# with x265 support
sudo dnf install --allowerasing vlc ffmpeg-libs x265-libs
```

---

### ibus-rime

```bash
sudo dnf -y install ibus-rime

# append these line to ~/.bashrc
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_QPA_PLATFORM=xcb
```

---

### VSCode

```bash
# * Docs: https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null
sudo dnf -y install code
```

---

### flathub

```bash
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

---

### Refine

Tweak various aspects of GNOME

```bash
flatpak install --user page.tesk.Refine
```

### qq

```bash
flatpak install --user com.qq.QQ
```

### wechat

```bash
flatpak install --user com.tencent.WeChat
```

### TencentMeeting

```bash
flatpak install --user com.tencent.wemeet
```

---

### LocalSend

```bash
flatpak install --user org.localsend.localsend_app
```

---

### Google Chrome

```bash
sudo dnf -y install google-chrome-stable
```

----

### Steam

```bash
sudo dnf -y install steam
```

* Library -> Manage -> General -> Lauch Options: `__NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia DRI_PRIME=1 %command%`
* Library -> Manage -> Compatibility ->
- [x] Force the use of a specific Steam Play compatibility tool: `Proton Hotfix`
