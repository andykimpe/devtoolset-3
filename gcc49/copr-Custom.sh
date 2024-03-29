#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# add chroot with config
# Mock chroot: custom-1-x86_64
# add External repositories for build dependencies
# https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/23/Everything/x86_64/os/
# https://archives.fedoraproject.org/pub/archive/fedora/linux/updates/23/x86_64/
# https://download.copr.fedorainfracloud.org/results/yourusername/projectname/custom-1-x86_64/
# Mock chroot: custom-1-i386
# add External repositories for build dependencies
# https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/23/Everything/i386/os/
# https://archives.fedoraproject.org/pub/archive/fedora/linux/updates/23/i386/
# https://download.copr.fedorainfracloud.org/results/yourusername/projectname/custom-1-i386/
# Build dependencies: wget
# #! /bin/sh -x
# wget https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/copr-Custom.sh -O copr-Custom.sh
# bash copr-Custom.sh
# rm -f copr-Custom.sh
wget https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/gcc49.spec -O gcc49.spec
wget https://gcc.gnu.org/pub/gcc/releases/gcc-4.9.3/gcc-4.9.3.tar.bz2 -O gcc-4.9.3.tar.bz2
wget https://gcc.gnu.org/pub/gcc/infrastructure/isl-0.12.2.tar.bz2 -O isl-0.12.2.tar.bz2
wget http://www.bastoul.net/cloog/pages/download/cloog-0.18.4.tar.gz -O cloog-0.18.4.tar.gz
wget https://gcc.gnu.org/pub/gcc/infrastructure/mpfr-3.1.4.tar.bz2 -O mpfr-3.1.4.tar.bz2
wget https://gcc.gnu.org/pub/gcc/infrastructure/gmp-6.1.0.tar.bz2 -O gmp-6.1.0.tar.bz2
wget https://gcc.gnu.org/pub/gcc/infrastructure/mpc-1.0.3.tar.gz -O mpc-1.0.3.tar.gz
wget https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/gcc49 -O gcc49
wget https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/target.path -O target.path
wget https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/local_atomic.patch -O local_atomic.patch
