#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# add chroot with config
# Mock chroot: epal-6-x86_64
# Build dependencies: wget
# #! /bin/sh -x
# wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/copr-Custom.sh -O copr-Custom.sh
# bash copr-Custom.sh
# rm -f copr-Custom.sh
wget  https://dl.fedoraproject.org/pub/epel/7/SRPMS/Packages/p/python34-3.4.10-8.el7.src.rpm -O python34-3.4.10-8.el7.src.rpm
rpm2cpio python34-3.4.10-8.el7.src.rpm | cpio -idmv
rm-f python34-3.4.10-8.el7.src.rpm
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/python34.spec -O python34.spec
wget https://www.python.org/ftp/python/3.4.10/Python-3.4.10.tar.xz
