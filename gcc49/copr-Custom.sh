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
# Build dependencies: scl-utils-build wget
wget https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/gcc49.spec -O gcc49.spec
