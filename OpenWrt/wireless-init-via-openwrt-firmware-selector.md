# Initial Wireless Configuration via OpenWrt Firmware Selector

**Customize installed packages and/or first boot script**

* Script to run on first boot (uci-defaults)

```bash
uci set wireless.@wifi-device[0].disabled='0'
uci set wireless.@wifi-device[0].cell_density='0'
uci set wireless.@wifi-iface[0].disabled='0'
uci set wireless.@wifi-iface[0].ssid='OpenWrt0815'
uci set wireless.@wifi-iface[0].encryption='sae-mixed'
uci set wireless.@wifi-iface[0].key='HelloWorld'
uci commit wireless
```

This configuration enable the wireless interface 0, and set something following:

* ESSID: `OpenWrt0815`
* Key: `HelloWorld`
* Encryption: `WPA2-PSK/WPA3-SAE Mixed Mode (strong security)`
