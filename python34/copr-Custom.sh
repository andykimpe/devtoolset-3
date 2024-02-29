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
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/python34.spec -O python34.spec
wget https://www.python.org/ftp/python/3.4.10/Python-3.4.10.tar.xz
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/libpython.stp
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/systemtap-example.stp
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/pyfuntop.stp
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/check-pyc-and-pyo-timestamps.py
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00001-rpath.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/python34-readline.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00055-systemtap.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00102-lib64.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00104-lib64-fix-for-test_install.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00111-no-static-lib.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00113-more-configuration-flags.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00125-less-verbose-COUNT_ALLOCS.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00131-disable-tests-in-test_io.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00132-add-rpmbuild-hooks-to-unittest.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00134-fix-COUNT_ALLOCS-failure-in-test_sys.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00135-fix-test-within-test_weakref-in-debug-build.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00137-skip-distutils-tests-that-fail-in-rpmbuild.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00139-skip-test_float-known-failure-on-arm.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/python3-arm-skip-failing-fragile-test.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00141-fix-tests_with_COUNT_ALLOCS.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00143-tsc-on-ppc.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00146-hashlib-fips.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00150-disable-rAssertAlmostEqual-cmath-on-ppc.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00155-avoid-ctypes-thunks.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00157-uid-gid-overflows.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00160-disable-test_fs_holes-in-rpm-build.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00163-disable-parts-of-test_socket-in-rpm-build.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00164-disable-interrupted_write-tests-on-ppc.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00173-workaround-ENOPROTOOPT-in-bind_port.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00178-dont-duplicate-flags-in-sysconfig.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00179-dont-raise-error-on-gdb-corrupted-frames-in-backtrace.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00180-python-add-support-for-ppc64p7.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00184-ctypes-should-build-with-libffi-multilib-wrapper.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00186-dont-raise-from-py_compile.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00188-fix-lib2to3-tests-when-hashlib-doesnt-compile-properly.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00189-add-rewheel-module.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/temporarily-disable-tests-requiring-SIGHUP.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00196-test-gdb-match-addr-before-builtin.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00203-disable-threading-test-koji.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00205-make-libpl-respect-lib64.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00311-fix-test_dbm_gnu-for-gdbm-1-15.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00320-CVE-2019-10160.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00332-CVE-2019-16056.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00346-CVE-2020-8492.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00351-avoid-infinite-loop-in-tarfile-module.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00352-resolve-hash-collisions-for-ipv_interface.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00353-update-test-certs-and-keys.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/00354-CVE-2020-26116-HTTP-request-method-CRLF-inject.patch
wget https://github.com/andykimpe/devtoolset-3/raw/master/python34/05000-autotool-intermediates.patch
