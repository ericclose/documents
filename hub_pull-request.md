## 通过命令行给 GitHub 仓库发起 pull request

### 安装 hub

因为我用的是 Arch Linux，所以我这么安装

```bash
sudo pacman -S hub
```

## 配置 hub

如果你喜欢用 HTTPS 协议来进行 git 操作，可以这么配置：

```bash
git config --global hub.protocol https
```

## pull request

```bash
hub pull-request --base OWNER:master --head MYUSER:my-branch
```

执行这个命令会使用你 Git 配置里默认的编辑器编辑 `PULLREQ_EDITMSG`，文件的首行是个空行，第一行作为 pull request 的 title（标题），然后空一行，再写 pull request 的 description（描述），写完描述后在分割线前得留一空行，最后保存（`:wq`）即可完成 pull request。