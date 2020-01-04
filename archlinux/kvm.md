# KVM

## 检查是否支持 KVM

### 硬件支持

KVM需要虚拟机宿主（host）的处理器带有虚拟化支持（对于Intel处理器来说是VT-x，对于AMD处理器来说是AMD-V）。你可以通过以下命令来检查你的处理器是否支持虚拟化：

```bash
LC_ALL=C lscpu | grep Virtualization
```

或者：

```bash
grep -E --color=auto 'vmx|svm|0xc0f' /proc/cpuinfo
```

如果运行后**没有显示**，那么你的处理器**不支持**硬件虚拟化，你不能使用KVM。

> **注意**: 您可能需要在BIOS中启用虚拟化支持

### 内核支持

Arch Linux 的内核提供了相应的内核模块来支持 KVM

* 你可以通过以下命令来检查你的内核是否已经包含了支持虚拟化所必须的模块（ **kvm** 及 **kvm_amd** 与 **kvm_intel** 这两者中的任意一个）：

```bash
zgrep CONFIG_KVM /proc/config.gz
```

如果模块设置不为 **y** 或 **m** ,则该模块不可用

* 然后，使用以下命令确保内核模块已自动加载：

```bash
[innovation@arch ~]$ lsmod | grep kvm
kvm_intel             311296  0
kvm                   790528  1 kvm_intel
irqbypass              16384  1 kvm
```

## 准虚拟化(使用VIRTIO)

准虚拟化为客户机提供了一种使用主机上设备的快速有效的通信方式。KVM使用 Virtio API 作为虚拟机管理程序和客户机之间的连接层，为虚拟机提供准虚拟化设备（亦称Virtio设备）。 所有Virtio设备都包括两部分：主机设备和客户机驱动程序。

### 内核支持

使用以下命令检查VIRTIO模块在内核中是否可用：

```bash
zgrep VIRTIO /proc/config.gz
```

然后，检查VIRTIO模块是否已经自动加载:

```bash
lsmod | grep virtio
```

如果运行后没有显示，那么需要**手动加载**模块。

```bash
sudo modprobe virtio
```

# QEMU

* qemu: 通用的开源计算机仿真器和虚拟器

安装 qemu

```bash
sudo pacman -S qemu
```

# libvirt

## 服务端

* *libvirt*: 用于控制虚拟化引擎（openvz，kvm，qemu，virtualbox，xen等）的API

安装 libvirt 以及至少一个虚拟运行环境（hypervisor）：

libvirt 的 KVM/QEMU 驱动 是 libvirt 的首选驱动，前面我们已经安装过了，所以可以开始安装 libvirt 了。

```bash
sudo pacman -S libvirt
```

## 网络相关

为了网络连接，需要安装这些包：

* *ebtables* 和 *dnsmasq*: 用于 默认的 NAT/DHCP 网络
* *bridge-utils*: 用于桥接网络
* *openbsd-netcat*: 通过 SSH 远程管理

```bash
sudo pacman -S ebtables dnsmasq bridge-utils openbsd-netcat
```

## 客户端

* *virt-manager*: 使用libvirt对KVM，Xen，LXC进行管理的图形化工具。

安装 virt-manager:

```bash
sudo pacman -S virt-manager
```

## 配置

对于**系统**级别的管理任务（如： 全局配置 和 镜像卷位置），libvirt 要求至少要**设置授权**和**启动守护进程**。

### 设置授权

> Libvirt 守护进程允许管理员分别为客户端连接的每个网络 socket 选择不同授权机制。这主要是通过 libvirt 守护进程的主配置文件 */etc/libvirt/libvirtd.conf* 来实现的。每个 libvirt socket 可以有独立的授权机制配置。目前的可选项有 *none*、*polkit* 和 *sasl*。    --From [libvirt: Connection authentication](http://libvirt.org/auth.html#ACL_server_config)

由于 libvirt 在安装时将把 polkit 作为依赖一并安装，所以 **polkit** 通常是 *unix_sock_auth* 参数的默认值（[来源](http://libvirt.org/auth.html#ACL_server_polkit)）。但基于文件的权限仍然可用。

#### 使用 polkit

> 注意：为使 polkit 认证工作正常，可能需要重新启动系统。

从 libvirt 1.2.16 版开始（commit见：[1](http://libvirt.org/git/?p=libvirt.git;a=commit;h=e94979e901517af9fdde358d7b7c92cc055dd50c)），**libvirt** 组的成员用户默认可以无口令访问读写模式 socket。最简单的判断方法就是看 libvirt 组是否存在并且用户是否该组成员。你可能想要修改授权以读写模式访问socket的组。

假如你想允许 kvm 用户组中的用户无需身份验证即可管理libvirt守护程序，可以这么做：

```bash
sudo vim /etc/polkit-1/rules.d/50-libvirt.rules
```

插入的内容如下：

```conf
/* Allow users in kvm group to manage the libvirt
daemon without authentication */
polkit.addRule(function(action, subject) {
    if (action.id == "org.libvirt.unix.manage" &&
        subject.isInGroup("kvm")) {
            return polkit.Result.YES;
    }
});
```

然后添加当前用户到 kvm 组:

```bash
sudo usermod -aG kvm $USER
```


最后为了生效别忘了先注销帐号然后再重新登录。

### 守护进程

**Start** both *libvirtd.service* and *virtlogd.service*. Optionally **enable** *libvirtd.service*. There is no need to enable *virtlogd.service*, since *libvirtd.service*, when enabled, also enables the *virtlogd.socket* and *virtlockd.socket* units.

```bash
systemctl start libvirtd.service virtlogd.service
systemctl enable libvirtd.service
```