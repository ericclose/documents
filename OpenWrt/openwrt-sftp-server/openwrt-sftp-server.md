
## exroot

```bash
# proxy settings
export http_proxy=http://<Proxy_Host>:7890
export https_proxy=http://<Proxy_Host>:7890
export no_proxy=localhost,127.0.0.0/8,::1

# Install the required packages
opkg update
opkg install block-mount kmod-fs-ext4 e2fsprogs parted kmod-usb-storage

# Identify the name of the USB disk
ls -al /dev/sd*

# Partition and format the USB disk
DISK="/dev/sda"
parted -s ${DISK} -- mklabel gpt mkpart extroot 2048s -2048s
DEVICE="${DISK}1"
mkfs.ext4 -L extroot ${DEVICE}

# Configure the extroot mount entry
eval $(block info ${DEVICE} | grep -o -e 'UUID="\S*"')
eval $(block info | grep -o -e 'MOUNT="\S*/overlay"')
uci -q delete fstab.extroot
uci set fstab.extroot="mount"
uci set fstab.extroot.uuid="${UUID}"
uci set fstab.extroot.target="${MOUNT}"
uci commit fstab

# Transfer the content of the current overlay to the external drive
mount ${DEVICE} /mnt
tar -C ${MOUNT} -cvf - . | tar -C /mnt -xf -

# Configure a mount entry for the the original overlay
DEVICE="$(block info | sed -n -e '/MOUNT="\S*\/overlay"/s/:\s.*$//p')"
uci -q delete fstab.rwm
uci set fstab.rwm="mount"
uci set fstab.rwm.device="${DEVICE}"
uci set fstab.rwm.target="/rwm"
uci commit fstab

# Reboot the device to apply the changes
reboot
```

---

```bash
# Start by refreshing the list of available software packages
opkg update
# Install the USB storage package (all USB versions)
opkg install kmod-usb-storage
# Install USB 3.0 drivers
opkg install kmod-usb3
insmod xhci-hcd
# To install support for UASP aka USB Attached SCSI (supported by many USB drives and drive enclosures, especially if USB 3.0. It enhances performance if it's supported by both the drive and the host controller in your device)
opkg install kmod-usb-storage-uas
# This will download the driver to use exFAT, there are currently no tools in OpenWrt to format/check exFAT
# opkg install kmod-fs-exfat libblkid1 exfat-mkfs


# change Dropbear port to something other than 22 (I used 2022)
uci set dropbear.@dropbear[0].Port='2022'
uci commit dropbear
service dropbear restart
# Exit and connect to router via Dropbear SSH on the new port
exit

# Install OpenSSH and SFTP
opkg install openssh-server openssh-sftp-server
# Enable & start OpenSSH
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config
service sshd enable
service sshd start

# Log out of Dropbear SSH and reconnect with OpenSSH (using port 22 now)
exit

# Stop & disable Dropbear
service dropbear disable
service dropbear stop
opkg remove --autoremove dropbear
rm -rf /etc/dropbear /etc/config/dropbear

# mkdir ~/.ssh
# touch ~/.ssh/authorized_keys
# chmod 700 ~/.ssh
# chmod 600 ~/.ssh/authorized_keys
# echo '<Put_Your_Public_Key_Here>>' >> ~/.ssh/authorized_keys

service sshd restart

# Install necessary packages to manage users and groups
opkg install shadow-useradd shadow-groupadd shadow-userdel shadow-groupdel shadow-usermod
# Create user and group for fstp
useradd sftpuser
groupadd sftpusers
usermod -aG sftpusers sftpuser
# Grant users directory access
mkdir -p /sftp/sftpuser
chown sftpuser:sftpusers /sftp/sftpuser
chmod 700 /sftp/sftpuser
# Disable shell access for the SFTP users created
usermod -s /bin/false sftpuser

# Set user passwords
passwd sftpuser

# Change SFTP server from `Subsystem sftp /usr/lib/sftp-server` to `Subsystem sftp internal-sftp`:
sed -i 's#^Subsystem\s\+sftp\s\+/usr/lib/sftp-server$#Subsystem sftp internal-sftp#' /etc/ssh/sshd_config

# Configure chroot for SFTP group
cat <<EOF >> /etc/ssh/sshd_config
Match Group sftpusers
ChrootDirectory /sftp/
ForceCommand internal-sftp -d /%u
EOF

# Restart SSH
service sshd restart

# firewall
# firewall.@rule[9]=rule
# firewall.@rule[9].name='Allow-SSH'
# firewall.@rule[9].proto='tcp'
# firewall.@rule[9].src='wan'
# firewall.@rule[9].dest_port='22'
# firewall.@rule[9].target='ACCEPT'
# firewall.@rule[10]=rule
# firewall.@rule[10].name='Allow-Luci'
# firewall.@rule[10].proto='tcp'
# firewall.@rule[10].src='wan'
# firewall.@rule[10].dest_port='80'
# firewall.@rule[10].target='ACCEPT'
```

## Reference

* [Extroot configuration - OpenWrt Wiki](https://openwrt.org/docs/guide-user/additional-software/extroot_configuration)
* [Using storage devices - OpenWrt Wiki](https://openwrt.org/docs/guide-user/storage/usb-drives)
* [Quick Start for Adding a USB driv - OpenWrt Wiki](https://openwrt.org/docs/guide-user/storage/usb-drives-quickstart)
* [OpenWRT SFTP & BitTorrent server - GitHub](https://github.com/matthewtraughber/openwrt_sftp-bittorrent_guide)