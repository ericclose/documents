```bash
sudo vim /etc/dnf/dnf.conf
```

```ini
max_parallel_downloads=10
fastestmirror=True

# Optional: dnf with a proxy server
proxy=http://URL:PORT
```

```bash
sudo dnf clean all
sudo dnf makecache
```
