1. 备份硬盘

2. 备份 & 还原驱动

```batch
# 备份驱动
pnputil /export-driver * D:\DriverBackup

# 还原驱动
pnputil /add-driver D:\DriverBackup\*.inf /subdirs /install
```

3. 常见库
* `VCRUNTIME140.dll not Found`

[Latest supported Visual C++ Redistributable downloads](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)


