#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# add chroot with config
# Mock chroot: epal-6-x86_64
# Build dependencies: wget
# #! /bin/sh -x
# wget https://github.com/andykimpe/devtoolset-3/raw/master/python34-sphinx/copr-Custom.sh -O copr-Custom.sh
# bash copr-Custom.sh
# rm -f copr-Custom.sh
wget https://dl.fedoraproject.org/pub/epel/7/SRPMS/Packages/c/cmake3-3.17.5-1.el7.src.rpm
rpm2cpio *.src.rpm | cpio -idmv
rm -f *.src.rpm
rm -rf python34-sphinx.spec python3-sphinx.spec python-sphinx.spec sphinx.spec
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34-sphinx/python34-sphinx.spec
