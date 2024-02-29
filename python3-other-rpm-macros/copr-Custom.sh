#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# add chroot with config
# Mock chroot: epal-6-x86_64
# Build dependencies: wget
# #! /bin/sh -x
# wget https://github.com/andykimpe/devtoolset-3/raw/master/python3-other-rpm-macros/copr-Custom.sh -O copr-Custom.sh
# bash copr-Custom.sh
# rm -f copr-Custom.sh
wget https://dl.fedoraproject.org/pub/epel/7/SRPMS/Packages/p/python-epel-rpm-macros-3-26.el7.src.rpm
rpm2cpio *.src.rpm | cpio -idmv
rm -f *.src.rpm
rm -rf *.spec
wget https://github.com/andykimpe/devtoolset-3/raw/master/python3-other-rpm-macros/python3-other-rpm-macros.spec
