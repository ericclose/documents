```bash
sudo vim /etc/dnf/dnf.conf
```

```ini
max_parallel_downloads=10
fastestmirror=True
```

```bash
sudo dnf clean all
sudo dnf makecache
```
