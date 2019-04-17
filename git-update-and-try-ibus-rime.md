# 升级 git 版本

```bash
sudo yum install dnf
sudo dnf install dh-autoreconf curl-devel expat-devel gettext-devel openssl-devel perl-devel zlib-devel
```

```bash
sudo dnf install asciidoc xmlto docbook2X
```

```bash
sudo yum install gnu-getopt
```

```bash
sudo ln -s /usr/bin/db2x_docbook2texi /usr/bin/docbook2x-texi
```

```bash
sudo yum remove git
```

```bash
$ wget https://github.com/git/git/archive/v2.21.0.tar.gz
$ tar -zxf v2.21.0.tar.gz
$ cd git-2.21.0
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info
```

# ibus-rime on Centos 7

```bash
yum install -y gcc gcc-c++ boost boost-devel cmake make cmake3
yum install glog glog-devel kyotocabinet kyotocabinet-devel marisa-devel yaml-cpp yaml-cpp-devel gtest gtest-devel libnotify zlib zlib-devel gflags gflags-devel leveldb leveldb-devel libnotify-devel ibus-devel
cd /usr/src
```
# install opencc

```bash
curl -L https://github.com/BYVoid/OpenCC/archive/ver.1.0.5.tar.gz | tar zx
cd OpenCC-ver.1.0.5/
make
make install
ln -s /usr/lib/libopencc.so /usr/lib64/libopencc.so

cd /usr/src
git clone --recursive https://github.com/rime/ibus-rime.git

cd /usr/src/ibus-rime
./install.sh
```

# checkout master & pull

```bash
cd /usr/src/ibus-rime/plum/
git checkout master
git pull origin master

cd /usr/src/ibus-rime
# skip submodule init
sed -i 's/git submodule update --init/#git submodule update --init/g' ./install.sh
./install.sh
```



# luna_pinyin.custom.yaml

```yaml
patch:
  switches:                   # 注意缩进
    - name: ascii_mode
      reset: 0                # reset 0 的作用是当从其他输入法切换到本输入法重设为指定状态
      states: [ 中文, 西文 ]   # 选择输入方案后通常需要立即输入中文，故重设 ascii_mode = 0
    - name: full_shape
      states: [ 半角, 全角 ]   # 而全／半角则可沿用之前方案的用法。
    - name: simplification
      reset: 1                # 增加这一行：默认启用「繁→簡」转换。
      states: [ 漢字, 汉字 ]
```
