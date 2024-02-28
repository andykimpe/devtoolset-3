#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# Mock chroot: fedora-39-x86_64
# External repositories for build dependencies
# https://download.copr.fedorainfracloud.org/results/andykimpe/php-scl/fedora-39-x86_64/
# Build dependencies: scl-utils-build php56-runtime wget
wget https://archives.fedoraproject.org/pub/fedora/linux/releases/37/Everything/source/tree/Packages/g/gcc-12.2.1-2.fc37.src.rpm -O gcc-12.2.1-2.fc37.src.rpm
rpm2cpio gcc-12.2.1-2.fc37.src.rpm | cpio -idmv
rm -rf gcc-12.2.1-2.fc37.src.rpm gcc.spec
wget https://github.com/andykimpe/scl-php56/raw/master/gcc-12/gcc-12.spec -O gcc-12.spec
