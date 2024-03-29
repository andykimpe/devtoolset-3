%global _optdir /opt
%global _islver 0.12.2
%global _cloogver 0.18.4
%global _mpfrver 3.1.4
%global _gmpver 6.1.0
%global _mpcver 1.0.3
%global gcc_target_platform %{_arch}-fedoraunited-linux-gnu
%define debug_package %{nil}

Summary: Various compilers (C, C++, Objective-C, Java, ada, go, obj-c++ ...)
Name: gcc49
Version: 4.9.3
Release: 3

License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Languages

Source:  https://gcc.gnu.org/pub/gcc/releases/gcc-4.9.3/gcc-4.9.3.tar.bz2
Source1: https://gcc.gnu.org/pub/gcc/infrastructure/isl-0.12.2.tar.bz2
Source2: http://www.bastoul.net/cloog/pages/download/cloog-0.18.4.tar.gz
Source3: https://gcc.gnu.org/pub/gcc/infrastructure/mpfr-3.1.4.tar.bz2
Source4: https://gcc.gnu.org/pub/gcc/infrastructure/gmp-6.1.0.tar.bz2
Source5: https://gcc.gnu.org/pub/gcc/infrastructure/mpc-1.0.3.tar.gz
Source6: https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/gcc49
Patch1:  https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/target.path

# Patch1 for libitm: Don't redefine __always_inline in local_atomic.
# https://gcc.gnu.org/viewcvs/gcc?view=revision&revision=227040
Patch2: https://github.com/andykimpe/devtoolset-3/raw/master/gcc49/local_atomic.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildRequires: binutils >= 2.24
BuildRequires: binutils
BuildRequires: make autoconf m4 gettext dejagnu bison flex sharutils
BuildRequires: texinfo texinfo-tex
BuildRequires: python-sphinx
BuildRequires: zlib-devel
BuildRequires: texinfo
BuildRequires: glibc-devel
#ada
BuildRequires: dejagnu

# go
BuildRequires: /usr/bin/hostname, procps

# java
# BuildRequires: which
# BuildRequires: dejagnu
# BuildRequires: libart_lgpl-devel
# BuildRequires: gtk2-devel

Requires: binutils >= 2.24
Conflicts: gdb < 5.1-2
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
AutoReq: true



%description
The gcc package contains the GNU Compiler Collection version 4.9.
You'll need this package in order to compile C code.
You can change the environment variables as follows adding
"source /usr/bin/gcc49" 



%prep
%setup -n gcc-4.9.3
%patch1 -p0
%patch2 -p0

tar jxvf %{SOURCE1} -C %{_builddir}/gcc-%{version}/
tar zxvf %{SOURCE2} -C %{_builddir}/gcc-%{version}/
tar jxvf %{SOURCE3} -C %{_builddir}/gcc-%{version}/
tar jxvf %{SOURCE4} -C %{_builddir}/gcc-%{version}/
tar zxvf %{SOURCE5} -C %{_builddir}/gcc-%{version}/

  # link isl/cloog for in-tree builds
  ln -s isl-%{_islver} isl
  ln -s cloog-%{_cloogver} cloog
  ln -s mpfr-%{_mpfrver} mpfr
  ln -s gmp-%{_gmpver} gmp
  ln -s mpc-%{_mpcver} mpc

  # Do not run fixincludes
  sed -i 's@\./fixinc\.sh@-c true@' gcc/Makefile.in

  # Fedora Linux installs x86_64 libraries /lib

[[ $CARCH == "x86_64" ]] && sed -i '/m64=/s/lib64/lib/' gcc/config/i386/t-linux64

  echo %{version} > gcc/BASE-VER

  # hack! - some configure tests for header files using "$CPP $CPPFLAGS"
  sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" {libiberty,gcc}/configure

  mkdir -p %{_builddir}/gcc-build

%build
cd %{_builddir}/gcc-build

  # using -pipe causes spurious test-suite failures
  # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48565
  CFLAGS=${CFLAGS/-pipe/}
  CXXFLAGS=${CXXFLAGS/-pipe/}


  %{_builddir}/gcc-%{version}/configure --prefix=/opt/gcc-%{version} \
      --libdir=/opt/gcc-%{version}/%{_lib} --libexecdir=/opt/gcc-%{version}/%{_lib} \
      --mandir=/opt/gcc-%{version}/man --infodir=/opt/gcc-%{version}/info --with-gxx-include-dir=/opt/gcc-%{version}/include \
      --host=%{_arch}-fedoraunited-linux-gnu \
      --build=%{_arch}-fedoraunited-linux-gnu \
      --enable-languages=c,c++,objc,obj-c++,go,fortran,lto \
      --with-system-zlib \
      --enable-libstdcxx-time \
      --disable-multilib \
      --enable-version-specific-runtime-libs \
      --enable-plugin \
      --enable-threads=posix \
      --enable-checking=release \
      --enable-gnu-unique-object \
      --enable-linker-build-id \
      --enable-lto \
      --enable-initfini-array \
      --enable-gnu-indirect-function \
      --enable-tls \
      %ifarch %{ix86} x86_64
	  --with-tune=generic \
%endif
      --enable-bootstrap 
 

make bootstrap || return 1

  

%install

cd %{_builddir}/gcc-build

  make -j1 DESTDIR=%{buildroot} install


  # Install Runtime Library Exception
  install -dm 755 %{buildroot}/usr/share/licenses/%{name}/
  install -m 0644 %{_builddir}/gcc-%{version}/COPYING.RUNTIME %{buildroot}/usr/share/licenses/%{name}/RUNTIME.LIBRARY.EXCEPTION

  # Help plugins find out nvra.
echo "gcc-%{version}-%{release}.%{_arch}" | tee %{buildroot}/opt/gcc-%{version}/%{_lib}/gcc/%{gcc_target_platform}/rpmver

  # i686
%ifarch i686
  ln -sf %{_optdir}/gcc-%{version}/lib/gcc/i386-fedoraunited-linux-gnu %{buildroot}/opt/gcc-%{version}/%{_lib}/gcc/i686-fedoraunited-linux-gnu
%endif 

  # We need a script to change environment variables as follows
  install -dm 755 %{buildroot}/%{_bindir}/
  install -m 0644 %{SOURCE6} %{buildroot}/%{_bindir}/
  chmod a+x %{buildroot}/%{_bindir}/gcc49


%files 

%{_optdir}/gcc-%{version}/
%{_datadir}/licenses/%{name}/RUNTIME.LIBRARY.EXCEPTION
%{_bindir}/gcc49


%changelog

* Mon Mar 28 2016 David Vasquez <davidjeremias82@gmail.com> 4.9.3-2
- Added i686 symlink

* Sat Oct 10 2015 David Vasquez <davidjeremias82@gmail.com> 4.9.3-1
- New package

