#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# add chroot with config
# Mock chroot: epal-6-x86_64
# Build dependencies: wget
# #! /bin/sh -x
# wget https://github.com/andykimpe/devtoolset-3/raw/master/devtoolset-3-binutils/copr-Custom.sh -O copr-Custom.sh
# bash copr-Custom.sh
# rm -f copr-Custom.sh
wget http://archive.kernel.org/centos-vault/centos/6/sclo/Source/rh/devtoolset-3/devtoolset-3-binutils-2.24-18.el6.src.rpm
rpm2cpio *.src.rpm | cpio -idmv
rm -f *.src.rpm
rm -rf *.spec
wget https://github.com/andykimpe/devtoolset-3/raw/master/devtoolset-3-binutils/devtoolset-3-binutils.spec
