## 排查 Wi-Fi

手机 USB 开启 USB 热点

```bash
# dnf provides lspci
# sudo dnf -y install pciutils.x86_64
# lspci | grep -i network

dmesg | grep wifi

dnf search iwl
sudo dnf -y install iwl7260-firmware

# man nmcli | grep -A 1 NAME
dnf search NetworkManager | grep wifi
sudo dnf -y install NetworkManager-wifi

sudo reboot

# man nmcli | grep -B 1 creates
nmcli device wifi connect "SSID_NAME" password "PASSWORD" name "My room"
```

[Networking/CLI - Fedora Project Wiki](https://fedoraproject.org/wiki/Networking/CLI)

## Desktop Environment

### KDE

```bash
sudo dnf -y install plasma-workspace-wayland
sudo dnf -y install sddm
sudo systemctl enable sddm
sudo systemctl set-default graphical.target
reboot
```

### Gnome

```bash
# Required package for gnome desktop
sudo dnf install gdm gnome-shell gnome-terminal

# Enable login using graphical interface
sudo systemctl enable gdm

# Boot to graphical interface as default
sudo systemctl set-default graphical.target
```

## fonts

```bash
# Noto Sans CJK SC font
# sudo dnf -y install google-noto-sans-cjk-sc-fonts
sudo dnf -y install google-noto-sans-cjk-vf-fonts
```
