# Configuring RHEL as a wifi access point

When you configure an access point, NetworkManager automatically:

- Configures the `dnsmasq` service to provide DHCP and DNS services for clients
- Enables IP forwarding
- Adds `nftables` firewall rules to masquerade traffic from the wifi device and configures IP forwarding

## Identifying whether a wifi device supports the access point mode

```bash
# List the wifi devices to identify the one that should provide the access point:
[admin@localhost ~]$ nmcli device status | grep wifi
wls160u1i3  wifi      disconnected  --

# Verify that the device supports the access point mode:
[admin@localhost ~]$ nmcli -f WIFI-PROPERTIES.AP device show wls160u1i3
WIFI-PROPERTIES.AP:                     yes
```

## Configuring RHEL as a WPA2 or WPA3 Personal access point

**Prerequisites**

- The wifi device supports running in access point mode.
- The wifi device is not in use.
- The host has internet access.

```bash
# Install the dnsmasq and NetworkManager-wifi packages:
[admin@localhost ~]$ sudo dnf install dnsmasq NetworkManager-wifi

# Create the initial access point configuration:
[admin@localhost ~]$ sudo nmcli device wifi hotspot ifname wls160u1i3 con-name Example-Hotspot ssid Example-Hotspot password "password"
Device 'wls160u1i3' successfully activated with 'd5c1f919-dca0-482e-8cf2-298543c9671d'.
Hint: "nmcli dev wifi show-password" shows the Wi-Fi name and password.

# Optional: Configure the access point to support only WPA3:
[admin@localhost ~]$ sudo nmcli connection modify Example-Hotspot 802-11-wireless-security.key-mgmt sae

# By default, NetworkManager uses the IP address 10.42.0.1 for the wifi device and 
# assigns IP addresses from the remaining 10.42.0.0/24 subnet to clients. To 
# configure a different subnet and IP address, enter:
[admin@localhost ~]$ sudo nmcli connection modify Example-Hotspot ipv4.addresses 192.0.2.254/24
# The IP address you set, in this case 192.0.2.254, is the one that NetworkManager 
# assigns to the wifi device. Clients will use this IP address as default gateway 
# and DNS server.

# Activate the connection profile:
[admin@localhost ~]$ sudo nmcli connection up Example-Hotspot
```

## 802-11-wireless

802-11-wireless — Wi-Fi Settings

## Properties

| Key Name | Value Type | Default Value | Value Description                                                                                                                                                                                                                                                                                                                                                                                         |
| -------- | ---------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| band     | string     |               | 802.11 frequency band of the network. One of "a" for 5GHz 802.11a or "bg" for 2.4GHz 802.11. This will lock associations to the Wi-Fi network to the specific band, i.e. if "a" is specified, the device will not associate with the same network in the 2.4GHz band even if the network's settings are compatible. This setting depends on specific driver capability and may not work with all drivers. |

```bash
[admin@localhost ~]$ sudo nmcli connection modify Example-Hotspot 802-11-wireless.band a
```

## Commands

```bash
[admin@localhost ~]$ nmcli device status | grep wifi
wls160u1i3  wifi      disconnected  --

[admin@localhost ~]$ nmcli -f WIFI-PROPERTIES.AP device show wls160u1i3
WIFI-PROPERTIES.AP:                     yes

[admin@localhost ~]$ sudo dnf install dnsmasq NetworkManager-wifi

[admin@localhost ~]$ sudo nmcli device wifi hotspot ifname wls160u1i3 con-name Example-Hotspot ssid Example-Hotspot password "password"
Device 'wls160u1i3' successfully activated with 'ebc648f7-c48a-4d6a-9935-3686c816d644'.
Hint: "nmcli dev wifi show-password" shows the Wi-Fi name and password.

[admin@localhost ~]$ sudo nmcli connection modify Example-Hotspot 802-11-wireless.band a

[admin@localhost ~]$ sudo nmcli connection modify Example-Hotspot 802-11-wireless-security.key-mgmt sae

[admin@localhost ~]$ sudo nmcli connection up Example-Hotspot
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/8)
```

## Reference

* [Configuring RHEL as a wifi access point](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/assembly_configuring-rhel-as-a-wifi-access-point_configuring-and-managing-networking)
* [nm-settings-nmcli - 802-11-wireless setting](https://networkmanager.dev/docs/api/latest/nm-settings-nmcli.html#:~:text=802%2D11%2Dwireless%20setting)
