```bash
passwd
sudo systemctl start sshd

ssh-keygen -R 127.0.0.1
ssh liveuser@127.0.0.1

sudo dnf install vim
sudo setenforce 0
wget https://github.com/glacion/genfstab/releases/download/1.0/genfstab; chmod +x genfstab
```

---

## 分区

If you are not familiar with partitioning, [get comfortable with it](https://wiki.archlinux.org/index.php/Partitioning).  
For reference, these are the partitions i use for testing in a VM with a drive of 12GiB:

- `/dev/sda1` ESP partition of size 100MiB, mounted on `/boot`.
- `/dev/sda2` swap partition of size 1.9GiB.
- `/dev/sda3` XFS partition of size 10GiB, mounted on `/`.

I chose `/mnt` to be my install root, you may change to your preference but be sure to update the commands accordingly.

```bash
sudo fdisk /dev/sda

sudo mkfs.fat -F32 /dev/sda1

sudo swapoff /dev/zram0

sudo mkswap /dev/sda2
sudo mkfs.ext4 /dev/sda3

sudo swapon /dev/sda2
sudo mount /dev/sda3 /mnt

sudo mkdir /mnt/boot
sudo mount /dev/sda1 /mnt/boot
```

---

```bash
sudo vi /etc/resolv.conf
```



```bash
sudo dnf install \
--installroot=/mnt \
--releasever=34 \
--setopt=install_weak_deps=False \
--setopt=keepcache=True \
--assumeyes \
--nodocs \
systemd dnf glibc-langpack-en passwd rtkit policycoreutils \
NetworkManager audit firewalld selinux-policy-targeted kbd zchunk sudo \
vim-minimal systemd-udev rootfiles less iputils deltarpm sqlite lz4 xfsprogs \
kernel
```

```bash
sudo systemd-firstboot \
--root=/mnt \
--locale=C.UTF-8 \
--keymap=us \
--hostname=fedora \
--setup-machine-id
```

```bash
sudo bash -c "./genfstab -U /mnt > /mnt/etc/fstab"
```

```bash
sudo systemd-nspawn -D /mnt
useradd -m -G wheel -s /bin/bash eric
passwd eric
exit
```

```bash
sudo rm -f /mnt/etc/yum.repos.d/*{*cisco*,*testing*,*modular*}*
sudo vi /mnt/etc/dnf/dnf.conf

# add this:
install_weak_deps=False
keepcache=True
tsflags=nodocs
```

```bash
sudo dnf update kernel
reboot
sudo systemd-nspawn -bD /mnt
sudo dnf update
```

```bash
sudo dnf install kernel
sudo bootctl install
sudo cp /usr/lib/modules/5.13.12-200.fc34.x86_64/vmlinuz /boot/vmlinuz-linux
sudo cp /boot/initramfs-5.13.12-200.fc34.x86_64.img /boot/initramfs-linux.img

sudo dnf install vim
sudo vim /etc/dracut.conf.d/fs.conf
# add this:
filesystems+="xfs"
```

---

```bash
sudo vim /boot/loader/loader.conf
```

```conf
default  fedora
timeout  4
console-mode max
editor   no
```

```bash
sudo vim /boot/loader/entries/fedora.conf
```

```conf
title   Fedora
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options root=PARTUUID=
```

```bash
cat /etc/fstab
```

```bash
title   Fedora
linux   /vmlinuz-linux
initrd  /initramfs-linux.img
options root=PARTUUID=9d64b391-559a-41f0-b6ac-06be907038dd    rw
```

---

```
sudo vim /boot/loader/entries/<MACHINE_ID>-<KVER>.conf

# add this:

options    BOOT_IMAGE=/images/pxeboot/vmlinuz
root=live:CDLABEL=Fedora-WS-Live-30-1-2 rd.live.image quiet

# change this:

options    root=UUID=<UUID_OF_ROOT_PARTITION> ro quiet
```

---

```
sudo dnf install efibootmgr
```

---

- Exit the container with `sudo poweroff`

- EFI Entry
  
  Create an EFI entry using `efibootmgr` like below.  
  **Note:** Make sure that the -d and -p arguments point to the ESP of your system.

```bash
sudo efibootmgr -d /dev/sda1 \
-p 1 \
-c \
-L "Fedora" \
-l /EFI/systemd/systemd-bootx64.efi
```

Clean up and reboot

```bash
umount -R /mnt
reboot
```