#! /bin/sh -x
#use for build on
# copr.fedorainfracloud.org
# Mock chroot: epel-6-x86_64
# External repositories for build dependencies
# https://download.copr.fedorainfracloud.org/results/andykimpe/devtoolset-3/epel-6-x86_64/
# Build dependencies: scl-utils-build wget
# #! /bin/sh -x
# wget https://github.com/andykimpe/devtoolset-3/raw/master/devtoolset-3/copr-Custom.sh -O copr-Custom.sh
# bash copr-Custom.sh
# rm -f copr-Custom.sh
wget https://github.com/andykimpe/devtoolset-3/raw/master/devtoolset-3/devtoolset-3.spec -O devtoolset-3.spec
wget  https://github.com/sclorg/rhscl-dockerfiles/archive/e90f5f98179410b7262098e4a016aa26dba598af/rhscl-dockerfiles-e90f5f9.tar.gz -O rhscl-dockerfiles-e90f5f9.tar.gz
# backup
# wget https://github.com/andykimpe/devtoolset-3/raw/master/devtoolset-3/rhscl-dockerfiles-e90f5f98179410b7262098e4a016aa26dba598af.tar.gz -O rhscl-dockerfiles-e90f5f98179410b7262098e4a016aa26dba598af.tar.gz
