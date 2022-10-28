- [Nvidia](#nvidia)
  - [禁用 nouveau](#%e7%a6%81%e7%94%a8-nouveau)
  - [查看当前设备的显卡](#%e6%9f%a5%e7%9c%8b%e5%bd%93%e5%89%8d%e8%ae%be%e5%a4%87%e7%9a%84%e6%98%be%e5%8d%a1)
  - [安装 Nvidia 闭源驱动](#%e5%ae%89%e8%a3%85-nvidia-%e9%97%ad%e6%ba%90%e9%a9%b1%e5%8a%a8)
  - [编辑配置文件](#%e7%bc%96%e8%be%91%e9%85%8d%e7%bd%ae%e6%96%87%e4%bb%b6)
  - [prime-run](#prime-run)
  - [glxinfo](#glxinfo)
  - [启用 multilib 库](#%e5%90%af%e7%94%a8-multilib-%e5%ba%93)
  - [安装 lib32-mesa](#%e5%ae%89%e8%a3%85-lib32-mesa)
  - [安装 linux-zen](#%e5%ae%89%e8%a3%85-linux-zen)
  - [安装 Steam](#%e5%ae%89%e8%a3%85-steam)

# Nvidia

## 禁用 nouveau

```bash
sudo vim /etc/modprobe.d/blacklist.conf
```

追加 **blacklist nouveau**

## 查看当前设备的显卡

```bash
[innovation@arch ~]$ lspci -k | grep -A 2 -E "(VGA|3D)"
00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620 (rev 07)
	DeviceName: Onboard IGD
	Subsystem: Hewlett-Packard Company UHD Graphics 620
--
01:00.0 3D controller: NVIDIA Corporation GP108M [GeForce MX150] (rev a1)
	Subsystem: Hewlett-Packard Company GP108M [GeForce MX150]
	Kernel modules: nouveau
```

## 安装 Nvidia 闭源驱动

```bash
sudo pacman -S nvidia xorg-xrandr
```

## 编辑配置文件

```bash
sudo vim /etc/X11/xorg.conf.d/nvidia.conf
```

添加如下内容

```conf
Section "ServerLayout"
  Identifier "layout"
  Screen 0 "iGPU"
  Option "AllowNVIDIAGPUScreens"
EndSection

Section "Device"
  Identifier "iGPU"
  Driver "modesetting"
  BusID "PCI:0:2:0"
EndSection

Section "Screen"
  Identifier "iGPU"
  Device "iGPU"
EndSection

Section "Device"
  Identifier "dGPU"
  Driver "nvidia"
  BusID "PCI:1:0:0"
EndSection
```

## prime-run

```bash
[innovation@arch ~]$ sudo vim /usr/bin/prime-run
```

```bash
#!/bin/bash
__NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia "$@"
```

```bash
sudo chmod 755 /usr/bin/prime-run
```

## glxinfo

```bash
[innovation@arch ~]$ sudo pacman -Ss glxinfo
extra/mesa-demos 8.4.0-2
    Mesa demos and tools incl. glxinfo + glxgears
[innovation@arch ~]$ sudo pacman -S mesa-demos
[innovation@arch ~]$ prime-run glxinfo | grep "OpenGL renderer"
OpenGL renderer string: GeForce MX150/PCIe/SSE2
```

## 启用 multilib 库

```bash
sudo vim /etc/pacman.conf
```

为了启用 multilib 库, 需要取消对 [multilib] 部分的注释，如下：

```plain
[multilib]
Include = /etc/pacman.d/mirrorlist
```

然后更新下仓库数据库即可。

## 安装 lib32-mesa

```bash
sudo pacman -S lib32-mesa
```

## 安装 linux-zen

```bash
sudo pacman -S linux-zen
```

## 安装 Steam

```bash
sudo pacman -S steam
```

打开相应游戏的属性然后设置启动选项，最后填入 `env __NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia %command%` 保存关闭既可