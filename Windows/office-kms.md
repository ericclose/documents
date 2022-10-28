以管理员模式运行 cmd，然后执行下列命令：

```bash
cd /d "C:\Program Files\Microsoft Office\Office16"
cscript ospp.vbs /sethst:kms.03k.org
cscript ospp.vbs /act

cscript OSPP.VBS /dstatus

# 取消使用某个产品密钥
cscript ospp.vbs /unpkey:<PRODUCT_KEY>
```
