# rpmbuild parameters:
# --define "binutils_target arm-linux-gnu" to create arm-linux-gnu-binutils.
# --with debug: Build without optimizations and without splitting the debuginfo.
# --without testsuite: Do not run the testsuite.  Default is to run it.
# --with testsuite: Run the testsuite.  Default --with debug is not to run it.

%{?scl:%{?scl_package:%scl_package binutils}}

%global dfcommit e90f5f98179410b7262098e4a016aa26dba598af
%global dfshortcommit %(c=%{dfcommit}; echo ${c:0:7})
%global dockerfiledir %{_datadir}/%{scl_prefix}dockerfiles
%if 0%{?fedora} || 0%{?rhel} >= 7
%global brp_python_hardlink /usr/lib/rpm/brp-python-hardlink
%else
%global brp_python_hardlink /usr/lib/rpm/redhat/brp-python-hardlink
%endif
%if  0%{?rhel} == 6
%global __os_install_post /usr/lib/rpm/brp-compress \
  %{!?__debug_package:/usr/lib/rpm/brp-strip %{__strip}} \
  /usr/lib/rpm/brp-strip-static-archive %{__strip} \
  /usr/lib/rpm/brp-strip-comment-note %{__strip} %{__objdump}
%else
%global __os_install_post /usr/lib/rpm/brp-compress \
  %{!?__debug_package:/usr/lib/rpm/brp-strip %{__strip}} \
  /usr/lib/rpm/brp-strip-static-archive %{__strip} \
  /usr/lib/rpm/brp-strip-comment-note %{__strip} %{__objdump} \
  %{brp_python_hardlink}
%endif

%if 0%{!?binutils_target:1}
%define binutils_target %{_target_platform}
%define isnative 1
%define enable_shared 1
%else
%define cross %{binutils_target}-
%define isnative 0
%define enable_shared 0
%endif

Summary: A GNU collection of binary utilities
Name: devtoolset-3-binutils
Version: 2.24
Release: 18%{?dist}
License: GPLv3+
Group: Development/Tools
URL: http://sources.redhat.com/binutils

Source: ftp://ftp.kernel.org/pub/linux/devel/binutils/binutils-%{version}.tar.bz2
# The ftp.kernel.org/pub/linux/devel/binutils/ page is (temporarily) unavailable
# so we use the GNU site instead.
# Source: http://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.bz2
Source2: binutils-2.19.50.0.1-output-format.sed
Patch01: binutils-2.20.51.0.2-libtool-lib64.patch
Patch02: binutils-2.20.51.0.10-ppc64-pie.patch
Patch03: binutils-2.20.51.0.2-ia64-lib64.patch
Patch04: binutils-2.20.51.0.2-version.patch
Patch05: binutils-2.20.51.0.2-set-long-long.patch
Patch06: binutils-2.20.51.0.10-copy-osabi.patch
Patch07: binutils-2.20.51.0.10-sec-merge-emit.patch
# Enable -zrelro by default: BZ #621983
Patch08: binutils-2.22.52.0.1-relro-on-by-default.patch
# Local patch - export demangle.h with the binutils-devel rpm.
Patch09: binutils-2.22.52.0.1-export-demangle.h.patch
# Disable checks that config.h has been included before system headers.  BZ #845084
Patch10: binutils-2.22.52.0.4-no-config-h-check.patch
# Fix errors reported by version 5.0 of texinfo
Patch11: binutils-2.24-as-doc-texinfo-fixes.patch
# Picked up recent upstream patches
# Fix addr2line to use the dynamic symbol table if it could not find any ordinary symbols.
Patch12: binutils-2.23.52.0.1-addr2line-dynsymtab.patch
Patch13: binutils-2.23.2-kernel-ld-r.patch
# Correct bug introduced by patch 12
Patch14: binutils-2.23.2-aarch64-em.patch
# Fix building opcodes library with -Werror=format-security
Patch15: binutils-2.24-s390-mkopc.patch
# Import fixes for IFUNC and PLT handling for AArch64.
Patch16: binutils-2.24-elfnn-aarch64.patch
# Fix decoding of abstract instance names using DW_FORM_ref_addr.
Patch17: binutils-2.24-DW_FORM_ref_addr.patch
# Fix compiling using gcc 4.9
Patch18: binutils-2.24-set-section-macros.patch
# Fix detections of uncompressed .debug_str sections that look like they have been compressed.
Patch19: binutils-2.24-fake-zlib-sections.patch
# Fix detections little endian PPC shared libraries
Patch20: binutils-2.24-ldforcele.patch
Patch1010: binutils-2.23.51.0.3-Provide-std-tr1-hash.patch
Patch1011: binutils-rh1038339.patch
Patch1012: binutils-2.24-rh919508.patch
Patch1013: binutils-rh980613.patch
Patch1014: binutils-rh1117458.patch
Provides: bundled(libiberty)

%define gold_arches %ix86 x86_64 %arm

%ifarch %gold_arches
%define build_gold	both
%else
%define build_gold	no
%endif

%define alternatives_cmd %{!?scl:%{_sbindir}}%{?scl:%{_root_sbindir}}/alternatives
%define alternatives_cmdline %{alternatives_cmd}%{?scl: --altdir %{_sysconfdir}/alternatives --admindir %{_scl_root}/var/lib/alternatives}

%if 0%{?_with_debug:1}
# Define this if you want to skip the strip step and preserve debug info.
# Useful for testing.
%define __debug_install_post : > %{_builddir}/%{?buildsubdir}/debugfiles.list
%define debug_package %{nil}
%define run_testsuite 0%{?_with_testsuite:1}
%else
%define run_testsuite 0%{!?_without_testsuite:1}
%endif

Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: texinfo >= 4.0, gettext, flex, bison, zlib-devel
# BZ 920545: We need pod2man in order to build the manual pages.
BuildRequires: /usr/bin/pod2man
# Required for: ld-bootstrap/bootstrap.exp bootstrap with --static
# It should not be required for: ld-elf/elf.exp static {preinit,init,fini} array
%if %{run_testsuite}
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 11
BuildRequires: glibc-static, zlib-static
%endif
# relro_test.sh uses dc which is part of the bc rpm, hence its inclusion here.
BuildRequires: dejagnu, sharutils, bc
# The GOLD testsuite needs a static libc++ 
%if "%{build_gold}" == "both" 
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 20
BuildRequires: libstdc++-static
%endif
%endif
%endif
Conflicts: gcc-c++ < 4.0.0
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%ifarch ia64
Obsoletes: gnupro <= 1117-1
%endif
%{?scl:Requires:%scl_runtime}


# The higher of these two numbers determines the default ld.
%{!?ld_bfd_priority: %define ld_bfd_priority	50}
%{!?ld_gold_priority:%define ld_gold_priority	30}

%if "%{build_gold}" == "both"
Requires(post): coreutils
Requires(post): %{alternatives_cmd}
Requires(preun): %{alternatives_cmd}
%endif

# On ARM EABI systems, we do want -gnueabi to be part of the
# target triple.
%ifnarch %{arm}
%define _gnu %{nil}
%endif

%description
Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%package devel
Summary: BFD and opcodes static and dynamic libraries and header files
Group: System Environment/Libraries
Provides: binutils-static = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires: %{?scl_prefix}binutils = %{version}-%{release}
Requires: zlib-devel

%description devel
This package contains BFD and opcodes static and dynamic libraries.

The dynamic libraries are in this package, rather than a seperate
base package because they are actually linker scripts that force
the use of the static libraries.  This is because the API of the
BFD library is too unstable to be used dynamically.

The static libraries are here because they are now needed by the
dynamic libraries.

Developers starting new projects are strongly encouraged to consider
using libelf instead of BFD.

%prep
%setup -q -n binutils-%{version}
%patch01 -p0 -b .libtool-lib64~
%patch02 -p0 -b .ppc64-pie~
%ifarch ia64
%if "%{_lib}" == "lib64"
%patch03 -p0 -b .ia64-lib64~
%endif
%endif
%patch04 -p0 -b .version~
%patch05 -p0 -b .set-long-long~
%patch06 -p0 -b .copy-osabi~
%patch07 -p0 -b .sec-merge-emit~
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%patch08 -p0 -b .relro~
%endif
%patch09 -p0 -b .export-demangle-h~
%patch10 -p0 -b .no-config-h-check~
%patch11 -p1 -b .gas-texinfo~

%patch12 -p0 -b .addr2line~
%patch13 -p0 -b .kernel-ld-r~
%patch14 -p0 -b .aarch64~
%patch15 -p0 -b .mkopc~
%patch16 -p0 -b .elf-aarch64~
%patch17 -p0 -b .ref-addr~
%patch18 -p0 -b .sec-macros~
%patch19 -p0 -b .fake-zlib~
%ifarch ppc64le
%patch20 -p0 -b .ldforcele~
%endif

%patch1010 -p1 -b .provide-hash~
%patch1011 -p1 -b .manpage~
%patch1012 -p1 
%patch1013 -p1 
%patch1014 -p1 

# We cannot run autotools as there is an exact requirement of autoconf-2.59.

# On ppc64 we might use 64KiB pages
sed -i -e '/#define.*ELF_COMMONPAGESIZE/s/0x1000$/0x10000/' bfd/elf*ppc.c
# LTP sucks
perl -pi -e 's/i\[3-7\]86/i[34567]86/g' */conf*
sed -i -e 's/%''{release}/%{release}/g' bfd/Makefile{.am,.in}
sed -i -e '/^libopcodes_la_\(DEPENDENCIES\|LIBADD\)/s,$, ../bfd/libbfd.la,' opcodes/Makefile.{am,in}
# Build libbfd.so and libopcodes.so with -Bsymbolic-functions if possible.
if gcc %{optflags} -v --help 2>&1 | grep -q -- -Bsymbolic-functions; then
sed -i -e 's/^libbfd_la_LDFLAGS = /&-Wl,-Bsymbolic-functions /' bfd/Makefile.{am,in}
sed -i -e 's/^libopcodes_la_LDFLAGS = /&-Wl,-Bsymbolic-functions /' opcodes/Makefile.{am,in}
fi
# $PACKAGE is used for the gettext catalog name.
sed -i -e 's/^ PACKAGE=/ PACKAGE=%{?cross}/' */configure
# Undo the name change to run the testsuite.
for tool in binutils gas ld
do
  sed -i -e "2aDEJATOOL = $tool" $tool/Makefile.am
  sed -i -e "s/^DEJATOOL = .*/DEJATOOL = $tool/" $tool/Makefile.in
done
touch */configure

%ifarch %{power64}
%define _target_platform %{_arch}-%{_vendor}-%{_host_os}
%endif

%build
echo target is %{binutils_target}
export CFLAGS="$RPM_OPT_FLAGS"
CARGS=

case %{binutils_target} in i?86*|sparc*|ppc*|s390*|sh*|arm*|aarch64*)
  CARGS="$CARGS --enable-64-bit-bfd"
  ;;
esac

case %{binutils_target} in ia64*)
  CARGS="$CARGS --enable-targets=i386-linux"
  ;;
esac

%if 0%{?_with_debug:1}
CFLAGS="$CFLAGS -O0 -ggdb2"
%define enable_shared 0
%endif

# We could optimize the cross builds size by --enable-shared but the produced
# binaries may be less convenient in the embedded environment.
# The seemingly unncessary --with-sysroot argument is merely meant to enable
# sysroot capabilities in the resulting executables.  That allows customers
# to then use the sysroot capability to set up host-x-host build environments
# easier.
%configure \
  --build=%{_target_platform} --host=%{_target_platform} \
  --target=%{binutils_target} \
  --with-sysroot=/ \
%ifarch %gold_arches
%if "%{build_gold}" == "both"
  --enable-gold=default --enable-ld \
%else
  --enable-gold \
%endif
%endif
%if !%{isnative}
  --enable-targets=%{_host} \
  --with-sysroot=%{_prefix}/%{binutils_target}/sys-root \
  --program-prefix=%{cross} \
%endif
%if %{enable_shared}
  --enable-shared \
%else
  --disable-shared \
%endif
  $CARGS \
  --enable-plugins \
  --with-bugurl=http://bugzilla.redhat.com/bugzilla/
make %{_smp_mflags} tooldir=%{_prefix} all
make %{_smp_mflags} tooldir=%{_prefix} info

# Do not use %%check as it is run after %%install where libbfd.so is rebuild
# with -fvisibility=hidden no longer being usable in its shared form.
%if !%{run_testsuite}
echo ====================TESTSUITE DISABLED=========================
%else
make -k check < /dev/null || :
echo ====================TESTING=========================
cat {gas/testsuite/gas,ld/ld,binutils/binutils}.sum
echo ====================TESTING END=====================
for file in {gas/testsuite/gas,ld/ld,binutils/binutils}.{sum,log}
do
  ln $file binutils-%{_target_platform}-$(basename $file) || :
done
tar cjf binutils-%{_target_platform}.tar.bz2 binutils-%{_target_platform}-*.{sum,log}
uuencode binutils-%{_target_platform}.tar.bz2 binutils-%{_target_platform}.tar.bz2
rm -f binutils-%{_target_platform}.tar.bz2 binutils-%{_target_platform}-*.{sum,log}
%endif

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%if %{isnative}
make prefix=%{buildroot}%{_prefix} infodir=%{buildroot}%{_infodir} install-info

# Rebuild libiberty.a with -fPIC.
# Future: Remove it together with its header file, projects should bundle it.
make -C libiberty clean
make CFLAGS="-g -fPIC $RPM_OPT_FLAGS" -C libiberty

# Rebuild libbfd.a with -fPIC.
# Without the hidden visibility the 3rd party shared libraries would export
# the bfd non-stable ABI.
make -C bfd clean
make CFLAGS="-g -fPIC $RPM_OPT_FLAGS -fvisibility=hidden" -C bfd

# Rebuild libopcodes.a with -fPIC.
make -C opcodes clean
make CFLAGS="-g -fPIC $RPM_OPT_FLAGS" -C opcodes

install -m 644 bfd/libbfd.a %{buildroot}%{_libdir}
install -m 644 libiberty/libiberty.a %{buildroot}%{_libdir}
install -m 644 include/libiberty.h %{buildroot}%{_prefix}/include
install -m 644 opcodes/libopcodes.a %{buildroot}%{_libdir}
# Remove Windows/Novell only man pages
rm -f %{buildroot}%{_mandir}/man1/{dlltool,nlmconv,windmc,windres}*

%if %{enable_shared}
chmod +x %{buildroot}%{_libdir}/lib*.so*
%endif

# Prevent programs from linking against libbfd and libopcodes
# dynamically, as they are change far too often.
rm -f %{buildroot}%{_libdir}/lib{bfd,opcodes}.so

# Remove libtool files, which reference the .so libs
rm -f %{buildroot}%{_libdir}/lib{bfd,opcodes}.la

# Sanity check --enable-64-bit-bfd really works.
grep '^#define BFD_ARCH_SIZE 64$' %{buildroot}%{_prefix}/include/bfd.h
# Fix multilib conflicts of generated values by __WORDSIZE-based expressions.
%ifarch %{ix86} x86_64 ppc ppc64 s390 s390x sh3 sh4 sparc sparc64 arm
sed -i -e '/^#include "ansidecl.h"/{p;s~^.*$~#include <bits/wordsize.h>~;}' \
    -e 's/^#define BFD_DEFAULT_TARGET_SIZE \(32\|64\) *$/#define BFD_DEFAULT_TARGET_SIZE __WORDSIZE/' \
    -e 's/^#define BFD_HOST_64BIT_LONG [01] *$/#define BFD_HOST_64BIT_LONG (__WORDSIZE == 64)/' \
    -e 's/^#define BFD_HOST_64_BIT \(long \)\?long *$/#if __WORDSIZE == 32\
#define BFD_HOST_64_BIT long long\
#else\
#define BFD_HOST_64_BIT long\
#endif/' \
    -e 's/^#define BFD_HOST_U_64_BIT unsigned \(long \)\?long *$/#define BFD_HOST_U_64_BIT unsigned BFD_HOST_64_BIT/' \
    %{buildroot}%{_prefix}/include/bfd.h
%endif
touch -r bfd/bfd-in2.h %{buildroot}%{_prefix}/include/bfd.h

# Generate .so linker scripts for dependencies; imported from glibc/Makerules:

# This fragment of linker script gives the OUTPUT_FORMAT statement
# for the configuration we are building.
OUTPUT_FORMAT="\
/* Ensure this .so library will not be used by a link for a different format
   on a multi-architecture system.  */
$(gcc $CFLAGS $LDFLAGS -shared -x c /dev/null -o /dev/null -Wl,--verbose -v 2>&1 | sed -n -f "%{SOURCE2}")"

tee %{buildroot}%{_libdir}/libbfd.so <<EOH
/* GNU ld script */

$OUTPUT_FORMAT

/* The libz dependency is unexpected by legacy build scripts.  */
/* The libdl dependency is for plugin support.  (BZ 889134)  */
INPUT ( %{_libdir}/libbfd.a -liberty -lz -ldl )
EOH

tee %{buildroot}%{_libdir}/libopcodes.so <<EOH
/* GNU ld script */

$OUTPUT_FORMAT

INPUT ( %{_libdir}/libopcodes.a -lbfd )
EOH

%else # !%{isnative}
# For cross-binutils we drop the documentation.
rm -rf %{buildroot}%{_infodir}
# We keep these as one can have native + cross binutils of different versions.
#rm -rf %{buildroot}%{_prefix}/share/locale
#rm -rf %{buildroot}%{_mandir}
rm -rf %{buildroot}%{_libdir}/libiberty.a
%endif # !%{isnative}

# This one comes from gcc
rm -f %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_prefix}/%{binutils_target}

%find_lang %{?cross}binutils
%find_lang %{?cross}opcodes
%find_lang %{?cross}bfd
%find_lang %{?cross}gas
%find_lang %{?cross}gprof
cat %{?cross}opcodes.lang >> %{?cross}binutils.lang
cat %{?cross}bfd.lang >> %{?cross}binutils.lang
cat %{?cross}gas.lang >> %{?cross}binutils.lang
cat %{?cross}gprof.lang >> %{?cross}binutils.lang

if [ -x ld/ld-new ]; then
  %find_lang %{?cross}ld
  cat %{?cross}ld.lang >> %{?cross}binutils.lang
fi
if [ -x gold/ld-new ]; then
  %find_lang %{?cross}gold
  cat %{?cross}gold.lang >> %{?cross}binutils.lang
fi

%clean
rm -rf %{buildroot}

%post
%if "%{build_gold}" == "both"
%__rm -f %{_bindir}/%{?cross}ld
%{alternatives_cmdline} --install %{_bindir}/%{?cross}ld %{?cross}ld \
  %{_bindir}/%{?cross}ld.bfd %{ld_bfd_priority}
%{alternatives_cmdline} --install %{_bindir}/%{?cross}ld %{?cross}ld \
  %{_bindir}/%{?cross}ld.gold %{ld_gold_priority}
%{alternatives_cmdline} --auto %{?cross}ld
%endif
%if %{isnative}
/sbin/ldconfig
# For --excludedocs:
if [ -e %{_infodir}/binutils.info.gz ]
then
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/as.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/ld.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/standards.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/configure.info.gz
fi
%endif # %{isnative}
exit 0

%preun
%if "%{build_gold}" == "both"
if [ $1 = 0 ]; then
  %{alternatives_cmdline} --remove %{?cross}ld %{_bindir}/%{?cross}ld.bfd
  %{alternatives_cmdline} --remove %{?cross}ld %{_bindir}/%{?cross}ld.gold
fi
%endif
%if %{isnative}
if [ $1 = 0 ]; then
  if [ -e %{_infodir}/binutils.info.gz ]
  then
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/as.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/ld.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/standards.info.gz
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/configure.info.gz
  fi
fi
%endif
exit 0

%if %{isnative}
%postun -p /sbin/ldconfig
%endif # %{isnative}

%files -f %{?cross}binutils.lang
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{?cross}[!l]*
%if "%{build_gold}" == "both"
%{_bindir}/%{?cross}ld.*
%ghost %{_bindir}/%{?cross}ld
%else
%{_bindir}/%{?cross}ld*
%endif
%{_mandir}/man1/*
%if %{enable_shared}
%{_libdir}/lib*.so
%exclude %{_libdir}/libbfd.so
%exclude %{_libdir}/libopcodes.so
%endif

%if %{isnative}
%{_infodir}/[^b]*info*
%{_infodir}/binutils*info*

%files devel
%defattr(-,root,root,-)
%{_prefix}/include/*
%{_libdir}/lib*.a
%{_libdir}/libbfd.so
%{_libdir}/libopcodes.so
%{_infodir}/bfd*info*

%endif # %{isnative}

%changelog
* Tue Aug 12 2014 Patsy Franklin <pfrankli@redhat.com> - 2.24-18
- Do not overwrite valid SONAME with empty string.  (#1117458)

* Tue Jul 2 2014 Jeff Law <law@redhat.com> 2.24-17
- Enable --sysroot (#1080077).

* Mon Jun 30 2014 Patsy Franklin <pfrankli@redhat.com> - 2.24-16
- Conditionalize BuldRequires of libstdc++-static.
  Resync release numbers.

* Fri May 16 2014 Patsy Franklin <pfrankli@redhat.com> - 2.24-14
- Rebase to official binutils 2.24 release and recent patches.
  - Fix detection of little endian PPC64 binaries.  (#1095885)
  - Fix detection of uncompressed .debug_str sections.  (#1082370)
  - Fix compiling using gcc 4.9  (#1087374)
  - Use %{version} in Source string.  Delete unused patches.
  - Fix decoding of abbrevs using a DW_FORM_ref_addr attribute.  (#1056797)
  - Import fixes on 2.24 branch that affect AArch64 IFUNC and PLT handling.
  - Fix building opcodes library with -Werror=format-security.  (#1037026)
  - Delete: binutils-2.23.52.0.1-64-bit-thin-archives.patch
  - Delete: binutils-rh980601.patch
  - Remove: binutils-2.23.52.0.1-revert-pr15149.patch from spec file.

* Wed Dec 11 2013 Patsy Franklin <pfrankli@redhat.com> 2.23.52.0.1-10
- Correct -v, -verbose, -version descriptions in as manpage (#1038339).

* Thu Nov  7 2013 Patsy Franklin <pfrankli@redhat.com> 2.23.52.0.1-9
- Fix assert failure with --emit-relocs and .eh_frame sections. (#980613).

* Tue Jul 16 2013 Jeff Law <law@redhat.com> 2.23.52.0.1-8
- Handle .text.unlikely.* sections properly (#980601).

* Wed May 22 2013 Jeff Law <law@redhat.com> 2.23.52.0.1-7
- Updated manpage from Jaromir Hradilek (#919508)

* Fri May 17 2013 Patsy Franklin <pfrankli@redhat.com> 2.23.52.0.1-6
- Change TH to .TH in dwp man page. (#919508)

* Wed Apr 3 2013 Jeff Law <law@redhat.com> 2.23.52.0.1-5
- Add man page for dwp (#919508)

* Fri Mar 29 2013 Jeff Law <law@redhat.com> 2.23.52.0.1-4
- Rebuild with new buildroots.

* Mon Mar 18 2013 Jeff Law <law@redhat.com> 2.23.52.0.1-3
- Resync with RHEL7/Fedora19.  Primarily to pick up the bits needed
  to resolve #866547.
  Use ppc64 not %{power64} when fixing up multilib stuff
  Remove windmc man page again

* Tue Jan 29 2013 Patsy Franklin <pfranki@redhat.com> - 2.23.51.0.8-1
- Rebase on 2.23.51.0.8 release.
  - Provides bundled (libiberty)
  - Rename ARM LDRALT instruction to LDALT.  (#869025) PR/14575
  - Retire binutils-2.23.51.0.3-arm-ldralt.patch
  - Rebase on 2.23.51.0.6 release.  (#880508)
  - Rebase on 2.23.51.0.7 release.  (#889432)
  - Rebase on 2.23.51.0.8 release.  (#890382)
  - Add dependency upon libdl.  (#889134)

* Fri Jan 25 2013 Marek Polacek <polacek@redhat.com> - 2.23.51.0.3-4
- Just bump the version.

* Mon Oct 29 2012 Marek Polacek <polacek@redhat.com> - 2.23.51.0.3-3
- Fix gas manual page.  (#870032)
- Never mark linker generated dynamic symbols undefined.  (#860777)

* Tue Oct 16 2012 Marek Polacek <polacek@redhat.com> - 2.23.51.0.3-2
- Fix again building of gold with 4.1.2-RH.

* Mon Oct 15 2012 Marek Polacek <polacek@redhat.com> - 2.23.51.0.3-1
- Rebase on 2.23.51.0.3 release.  (#858560)

* Thu Sep 13 2012 Marek Polacek <polacek@redhat.com> - 2.23.51.0.2-1
- Rebase on 2.23.51.0.2 release.  (#856119)
- Remove windmc manpage.  (#850829)

* Wed Aug 08 2012 Nick Clifton <nickc@redhat.com> - 2.23.51.0.1-1
- Rebase on 2.23.51.0.1 release.  (#846433)

* Wed Jul  4 2012 Jakub Jelinek <jakub@redhat.com> - 2.22.52.0.4-2.4
- Add scl macros.
- Fix building of gold with gcc 4.1.2-RH (Dodji Seketeli, PR gold/14309).
- Add spu-unknown-elf target instead of just spu on ppc*.

* Tue Jun 19 2012 Jakub Jelinek <jakub@redhat.com> - 2.22.52.0.4-2
- Add minimal dwz -m support.

* Wed Jun 06 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.4-1
- Rebase on 2.22.52.0.4 release.  (#829027)

* Tue May 08 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.3-1
- Rebase on 2.22.52.0.3 release.  (#819823)

* Mon Apr 30 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.2-1
- Rebase on 2.22.52.0.2 release.  (#816514)
- Retire binutils-2.22.52.0.1-weakdef.patch, binutils-2.22.52.0.1-ld-13621.patch, binutils-rh797752.patch, binutils-2.22.52.0.1-x86_64-hidden-ifunc.patch, binutils-2.22.52.0.1-tsx.patch and binutils-2.22.52.0.1-hidden-ifunc.patch.
- Update binutils-2.22.52.0.1-reloc-on-by-default.patch.

* Fri Apr 27 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.1-12
- Include demangle.h in the devel rpm.

%if 0%{?rhel} >= 7
* Tue Apr 03 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.1-11
- Enable -zrelro by default for RHEL 7+. (#807831)
%endif

* Fri Mar 16 2012 Jakub Jelinek <jakub@redhat.com> - 2.22.52.0.1-10
- Fix up handling of hidden ifunc relocs on i?86

* Tue Mar 13 2012 Jeff Law <law@redhat.com> - 2.22.52.0.1-9
- Fix c++filt docs (2nd instance) (#797752)

* Wed Mar 07 2012 Jakub Jelinek <jakub@redhat.com> - 2.22.52.0.1-8
- Fix up handling of hidden ifunc relocs on x86_64
- Add Intel TSX support

%if 0%{?fedora} >= 18
* Tue Mar 06 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.1-7
- Enable -zrelro by default. (#621983 #807831)
%endif

* Mon Feb 27 2012 Jeff Law <law@redhat.com> - 2.22.52.0.1-6
- Fix c++filt docs (#797752)

* Tue Feb 14 2012 Mark Wielaard <mjw@redhat.com> - 2.22.52.0.1-5
- Add upstream ld/13621 'dangling global hidden symbol in symtab' patch.

* Wed Feb 08 2012 Adam Williamson <awilliam@redhat.com> - 2.22.52.0.1-4
- Actually apply the patch

* Wed Feb 08 2012 Adam Williamson <awilliam@redhat.com> - 2.22.52.0.1-3
- Add upstream weakdef.patch to fix RH #788107

* Wed Feb 01 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.1-2
- Drat - forgot to upload the new tarball.  Now done.

* Wed Feb 01 2012 Nick Clifton <nickc@redhat.com> - 2.22.52.0.1-1
- Rebase on 2.22.52 release.
- Remove build-id.patch and gold-casts.patch as they are included in the 2.22.52 sources.

* Fri Jan 13 2012 Nick Clifton <nickc@redhat.com> - 2.22-4
- Fix bug in GOLD sources parsing signed integers in command line options. 

* Fri Jan 13 2012 Nick Clifton <nickc@redhat.com> - 2.22-3
- Add casts for building gold with 4.7 version of gcc.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  22 2011 Nick Clifton <nickc@redhat.com> - 2.22-1
- Rebase on 2.22 release.

* Fri Sep  30 2011 Ricky Zhou <ricky@fedoraproject.org> - 2.21.53.0.2-2
- Rebuild libopcodes.a with -fPIC.

* Mon Aug  08 2011 Nick Clifton <nickc@redhat.com> - 2.21.53.0.2-1
- Rebase on 2.21.53.0.2 tarball.  Delete unneeded patches.  (BZ 728677)

* Tue Aug  02 2011 Nick Clifton <nickc@redhat.com> - 2.21.53.0.1-3
- Update libiberty demangling.  (BZ 727453)

* Wed Jul  27 2011 Nick Clifton <nickc@redhat.com> - 2.21.53.0.1-2
- Import Jakub Jelinek's patch to add support for displaying the contents of .debug_macro sections.

* Tue Jul  19 2011 Nick Clifton <nickc@redhat.com> - 2.21.53.0.1-1
- Rebase on 2.21.53.0.1 tarball.  Delete unneeded patches.  (BZ 712668)

* Fri Jun  24 2011 Nick Clifton <nickc@redhat.com> - 2.21.52.0.1-5
- Import fix for PR ld/12921.

* Fri Jun  24 2011 Nick Clifton <nickc@redhat.com> - 2.21.52.0.1-4
- Run "alternatives --auto" to restore ld symbolic link if it was manually configured.  (BZ 661247)

* Thu Jun  16 2011 Nick Clifton <nickc@redhat.com> - 2.21.52.0.1-3
- Fix seg-fault attempting to find a function name without a symbol table.  (BZ 713471)

* Fri Jun  10 2011 Nick Clifton <nickc@redhat.com> - 2.21.52.0.1-2
- Import fix for PR ld/12851 (BZ 711268)

* Thu Jun  09 2011 Nick Clifton <nickc@redhat.com> - 2.21.52.0.1-1
- Rebase on 2.21.52.0.1 tarball.  (BZ 712025)

* Thu May  19 2011 Nick Clifton <nickc@redhat.com> - 2.21.51.0.9-1
- Rebase on 2.21.51.0.9 tarball.  (BZ 703105)

* Mon May   2 2011 Peter Robinson <pbrobinson@gmail.com> - 2.21.51.0.8-3
- Add ARM to BFD checks

* Mon Apr  11 2011 Nick Clifton <nickc@redhat.com> - 2.21.51.0.8-2
- Delete plugins patch - enable plugins via configure option.

* Mon Apr  11 2011 Nick Clifton <nickc@redhat.com> - 2.21.51.0.8-1
- Rebase on 2.21.51.0.8 tarball.

* Thu Mar  17 2011 Nick Clifton <nickc@redhat.com> - 2.21.51.0.7-1
- Rebase on 2.21.51.0.7 tarball.

* Tue Mar  08 2011 Nick Clifton <nickc@redhat.com> - 2.21.51.0.6-2
- Enable gold plugins.  (BZ 682852)

* Thu Feb  10 2011 Nick Clifton <nickc@redhat.com> - 2.21.51.0.6-1
- Rebase on 2.21.51.0.6 tarball.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21.51.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  28 2011 Jakub Jelinek <jakub@redhat.com> - 2.21.51.0.5-3
- Readd --build-id fix patch.  (PR ld/12451)

* Thu Jan   6 2011 Dan Horák <dan[at]danny.cz> - 2.21.51.0.5-2
- fix build on non-gold arches like s390(x) where both ld and ld.bfd is installed

* Wed Jan   5 2011 Nick Clifton <nickc@redhat.com> - 2.21.51.0.5-1
- Rebase on 2.21.51.0.5 tarball.
- Delete redundant patches.
- Fix gold+ld configure command line option.

* Thu Nov   4 2010 Dan Horák <dan[at]danny.cz> - 2.20.51.0.12-2
- "no" is not valid option for --enable-gold

* Thu Oct  28 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.12-1
- Rebase on 2.20.51.0.12 tarball.  (BZ 582160)

* Fri Sep  10 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.11-1
- Rebase on 2.20.51.0.11 tarball.  (BZ 631771)

* Fri Aug  20 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.10-3
- Allow ^ and ! characters in linker script wildcard patterns.  (BZ 621742)

* Fri Aug  20 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.10-2
- Fix seg fault in sec_merge_emit().  (BZ 623687)

* Tue Aug  10 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.10-1
- Rebase on 2.20.51.0.10 tarball.
- Import GOLD sources from binutils mainline as of 10 Aug 2010. 

* Wed Jun  30 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.7-5
- Rename the binutils-static package to binutils-devel in line with the Fedora packaging guidelines.

* Wed Jun   9 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.7-4
- Allow GOLD linker to parse "-l<name>" directives inside INPUT statements in linker scripts. (BZ 600553)

* Tue May   4 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.7-3
- Allow unique symbols in archive maps.

* Tue Apr  20 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.7-2
- Merge binutils-devel package into binutils-static package.  (BZ 576300)

* Thu Apr   8 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.7-1
- Rebase on 2.20.51.0.7 tarball.
- Delete redundant patches:
  binutils-2.20.51.0.2-add-needed.patch,
  binutils-2.20.51.0.2-do-not-set-ifunc.patch,
  binutils-2.20.51.0.2-enable-gold.patch,
  binutils-2.20.51.0.2-gas-expr.patch,
  binutils-2.20.51.0.2-ifunc-ld-s.patch,
  binutils-2.20.51.0.2-lwp.patch,
  binutils-2.20.51.0.2-ppc-hidden-plt-relocs.patch,
  binutils-2.20.51.0.2-x86-hash-table.patch,
- Do not allow unique symbols to be bound locally.  (PR ld/11434)
- Add support for DWARF4 debug information.

* Thu Mar   4 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-17
- Do not set ELFOSABI_LINUX on binaries which just link to IFUNC using DSOs.  (BZ 568941)

* Tue Mar   2 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-16
- Copy the OSABI field in ELF headers, if set.  (BZ 568921)

* Fri Feb  12 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-15
- Create separate static and devel sub-packages.  (BZ 556040)

* Tue Feb   2 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-14
- Fix seg-fault when linking mixed x86 and x86_64 binaries.  (BZ 487472)

* Fri Jan  22 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-13
- Add a requirement for the coreutils.  (BZ 557006)

* Wed Jan  20 2010 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-12
- Fix --no-copy-dt-needed so that it will not complain about weak references.

* Fri Dec  18 2009 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-11
- Add missing part of PR 11088 patch.

* Thu Dec  17 2009 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-10
- Apply patch for PR 11088.  (BZ 544149)

* Wed Dec  9 2009 Nick Clifton <nickc@redhat.com> - 2.20.51.0.2-9
- Apply patch for PR 10856.  (BZ 544358)

* Tue Dec  1 2009 Roland McGrath <roland@redhat.com> - 2.20.51.0.2-8
- Build gold only for x86 flavors until others are tested.

* Tue Nov 24 2009 Roland McGrath <roland@redhat.com> - 2.20.51.0.2-7
- Add support for building gold.

* Mon Nov  9 2009 Jakub Jelinek <jakub@redhat.com> 2.20.51.0.2-5
- Fix up --copy-dt-needed-entries default.  (Nick Clifton)

* Mon Nov  9 2009 Jakub Jelinek <jakub@redhat.com> 2.20.51.0.2-4
- Fix ld -s with IRELATIVE relocations.  (BZ 533321, PR ld/10911)
- Add AMD Orochi LWP support, fix FMA4 support.

* Thu Nov 05 2009 Nick CLifton <nickc@redhat.com> 2.20.51.0.2-3
- Rename --add-needed to --copy-dt-needed-entries and improve error message about unresolved symbols in DT_NEEDED DSOs.

* Tue Oct 27 2009 Jan Kratochvil <jan.kratochvil@redhat.com> 2.20.51.0.2-2
- Fix rpm --excludedocs (BZ 515922).
- Fix spurious scriplet errors by `exit 0'. (BZ 517979, Nick Clifton)

* Mon Oct 12 2009 Nick Clifton <nickc@redhat.com> 2.20.51.0.2-1
- Rebase on 2.20 tarball.
- Remove redundant moxie patch.
- Remove redundant unique is global patch.
- Remove redundant cxxfilt java doc patch.

* Tue Sep 29 2009 Jan Kratochvil <jan.kratochvil@redhat.com> 2.19.51.0.14-32
- Remove spurious description of nonexistent --java switch for cxxfilt.

* Thu Aug  6 2009 Jakub Jelinek <jakub@redhat.com> 2.19.51.0.14-31
- Fix strip on objects with STB_GNU_UNIQUE symbols. (BZ 515700, PR binutils/10492)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.51.0.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.11-28
- Rebase sources on 2.19.51.0.14 tarball.  Gain fixes for PRs 10429 and 10433.

* Wed Jul 22 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.11-28
- Rebase sources on 2.19.51.0.13 tarball.  Remove redundant orphan section placement patch. (BZ 512937)

* Tue Jul 14 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.11-27
- Add patch to allow moxie target to build, and hence --enable-targets=all to work.

* Tue Jul 14 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.11-26
- Import orphan section placement patch from mainline.  (BZ 510384)

* Tue Jul 14 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.11-25
- Fix build-id patch to avoid memory corruption.  (BZ 501582)

* Sat Jul 11 2009 Jan Kratochvil <jan.kratochvil@redhat.com> 2.19.51.0.11-24
- Provide uuencode output of the testsuite results.

* Tue Jun 30 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.11-23
- Rebase sources on the 2.19.51.0.11 tarball.

* Mon Jun 22 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.10-22
- Rebase sources on the 2.19.51.0.10 tarball.

* Thu Jun 11 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.2-21
- Do not attempt to set execute permission on non-regular files.  (BZ 503426)

* Tue Jun  9 2009 Jakub Jelinek <jakub@redhat.com> 2.19.51.0.2-20
- Fix .cfi_* skip over >= 64KB of code.  (PR gas/10255)

* Wed May 27 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.2-19
- Import fix for binutils PR #9938.  (BZ 500295)

* Wed Apr 15 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.2-18
- Update IBM Power 7 support patch to fix tlbilx opcode.  (BZ 494718)

* Tue Mar 17 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.2-17
- Add glibc-static to BuildRequires when running the testsuite.

* Thu Mar 05 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.2-16
- Add IBM Power7 support.  (BZ 487887)

* Mon Mar 02 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.2-15
- Add IFUNC support.  (BZ 465302)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.51.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Jan Kratochvil <jan.kratochvil@redhat.com> 2.19.50.0.2-13
- Rediff the symbolic-envvar-revert patch to comply with rpm patch --fuzz=0.

* Thu Feb  5 2009 Nick Clifton <nickc@redhat.com> 2.19.51.0.2-12
- Rebase sources on 2.19.51.0.2 tarball.  Remove linkonce-r-discard and
  gcc-expect-table patches.

* Mon Feb  2 2009 Jan Kratochvil <jan.kratochvil@redhat.com> 2.19.50.0.1-11
- Fix .eh_frame_hdr build also for .gcc_except_table LSDA refs (BZ 461675).

* Fri Jan 23 2009 Nick Clifton <nickc@redhat.com> 2.19.50.0.1-10
- Only require dejagnu if the testsuites are going to be run.  (BZ 481169)

* Sat Nov 29 2008 Nick Clifton <nickc@redhat.com> 2.19.50.0.1-8
- Add build-id patch to ensure that section contents are incorporated
  into a build id.  (BZ 472152)

* Fri Nov 21 2008 Nick Clifton <nickc@redhat.com> 2.19.50.0.1
- Rebase sources on 2.19.50.0.1 tarball.  Update all patches, trimming
  those that are no longer needed.

* Thu Oct 30 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.9-7
- Fix %%{_prefix}/include/bfd.h on 32-bit hosts due the 64-bit BFD target
  support from 2.18.50.0.8-2 (BZ 468495).

* Thu Oct 30 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.9-6
- binutils-devel now requires zlib-devel (BZ 463101 comment 5).
- Fix complains on .gnu.linkonce.r relocations to their discarded
  .gnu.linkonce.t counterparts.

* Mon Sep 22 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.9-5
- Remove %%makeinstall to comply with the spu-binutils review (BZ 452211).

* Mon Sep 22 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.9-4
- Fix *.so scripts for multilib linking (BZ 463101, suggested by Jakub Jelinek).

* Sun Sep 21 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.9-3
- Provide libbfd.so and libopcodes.so for automatic dependencies (BZ 463101).
- Fix .eh_frame_hdr build on C++ files with discarded common groups (BZ 458950).
- Provide --build and --host to fix `rpmbuild --target' biarch builds.
- Include %%{binutils_target}- filename prefix for binaries for cross builds.
- Fix multilib conflict on %%{_prefix}/include/bfd.h's BFD_HOST_64BIT_LONG_LONG.

* Mon Sep 15 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.9-2
- Package review, analysed by Jon Ciesla and Patrice Dumas (BZ 225615).
 - build back in the sourcedir without problems as gasp is no longer included.
 - Fix the install-info requirement.
 - Drop the needless gzipping of the info files.
 - Provide Obsoletes versions.
 - Use the %%configure macro.

* Sat Aug 30 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.9-1
- Update to 2.18.50.0.9.
  - Drop the ppc-only spu target pre-build stage (BZ 455242).
  - Drop parsing elf64-i386 files for kdump PAE vmcore dumps (BZ 457189).
- New .spec BuildRequires zlib-devel (/-static) for compressed sections.
- Update .spec Buildroot to be more unique.

* Fri Aug  1 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.8-2
- Fix parsing elf64-i386 files for kdump PAE vmcore dumps (BZ 457189).
- Turn on 64-bit BFD support for i386, globally enable AC_SYS_LARGEFILE.
- `--with debug' builds now with --disable-shared.
- Removed a forgotten unused ld/eelf32_spu.c workaround from 2.18.50.0.8-1.

* Thu Jul 31 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.8-1
- Update to 2.18.50.0.8.
  - Drop the .clmul -> .pclmul renaming backport.
- Add %%{binutils_target} macro to support building cross-binutils.
  (David Woodhouse)
- Support `--without testsuite' to suppress the testsuite run.
- Support `--with debug' to build without optimizations.
- Refresh the patchset with fuzz 0 (for new rpmbuild).
- Enable the spu target on ppc/ppc64 (BZ 455242).

* Wed Jul 16 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.6-4
- include the `dist' tag in the Release number
- libbfd.a symbols visibility is now hidden (for #447426, suggested by Jakub)

* Wed Jul 16 2008 Jan Kratochvil <jan.kratochvil@redhat.com> 2.18.50.0.6-3
- rebuild libbfd.a with -fPIC for inclusion into shared libraries (#447426)

* Tue Apr  8 2008 Jakub Jelinek <jakub@redhat.com> 2.18.50.0.6-2
- backport .clmul -> .pclmul renaming

* Fri Apr  4 2008 Jakub Jelinek <jakub@redhat.com> 2.18.50.0.6-1
- update to 2.18.50.0.6
  - Intel AES, CLMUL, AVX/FMA support

* Mon Mar  3 2008 Jakub Jelinek <jakub@redhat.com> 2.18.50.0.4-2
- revert aranges optimization (Alan Modra, BZ#5303, BZ#5755)
- fix ld-shared testcase for GCC 4.3 (H.J. Lu)

* Fri Feb 29 2008 Jakub Jelinek <jakub@redhat.com> 2.18.50.0.4-1
- update to 2.18.50.0.4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 2.18.50.0.3-2
- Autorebuild for GCC 4.3

* Wed Dec 12 2007 Jakub Jelinek <jakub@redhat.com> 2.18.50.0.3-1
- update to 2.18.50.0.3
  - fix build with recent makeinfo (#415271)

* Thu Aug 16 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.18-1
- update to 2.17.50.0.18
  - GPLv3+
  - preserve .note.gnu.build-id in objcopy --only-keep-debug (#251935)
  - fix sparc64/alpha broken by --build-id patch (#252936)
- update License tag
- fix ld crash with --build-id and non-ELF output format (Alan Modra, BZ#4923)

* Tue Jul 31 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.17-7
- fix ppc32 secure PLT detection (Alan Modra)

* Wed Jul 25 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.17-6
- rebuilt to make sure even libbfd.so and libopcodes.so aren't
  broken by #249435

* Tue Jul 24 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.17-5
- add .note.gnu.build-id into default linker script (#249435)

* Tue Jul 24 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.17-4
- don't kill the %%{_gnu} part of target name on arm
  (Lennert Buytenhek, #243516)
- create just one PT_NOTE segment header for all consecutive SHT_NOTE
  sections

* Wed Jul 18 2007 Roland McGrath <roland@redhat.com> 2.17.50.0.17-3
- fix for ld --build-id

* Sun Jul 15 2007 Roland McGrath <roland@redhat.com> 2.17.50.0.17-2
- ld --build-id support

* Wed Jun 27 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.17-1
- update to 2.17.50.0.17

* Tue Jun 12 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.16-1
- update to 2.17.50.0.16

* Sat Apr 14 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.12-4
- fix linking non-ELF input objects into ELF output (#235747)

* Wed Mar 14 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.12-3
- don't require matching ELF_OSABI for target vecs with ELFOSABI_NONE,
  only prefer specific osabi target vecs over the generic ones
  (H.J.Lu, #230964, BZ#3826)
- build libbfd.so and libopcodes.so with -Bsymbolic-functions

* Fri Mar  2 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.12-2
- ignore install-info errors from scriptlets (#223678)

* Thu Mar  1 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.12-1
- update to 2.17.50.0.12
- revert the misdesigned LD_SYMBOLIC{,_FUNCTIONS} env var support,
  only support -Bsymbolic/-Bsymbolic-functions/--dynamic-list*

* Mon Jan  8 2007 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.9-1
- update to 2.17.50.0.9
- fix tekhex reader

* Sat Dec 23 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.8-2
- fix --as-needed on ppc64 (#219629)

* Sun Dec  3 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.8-1
- update to 2.17.50.0.8
- initialize frch_cfi_data (BZ#3607)

* Fri Dec  1 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.7-1
- update to 2.17.50.0.7
  - .cfi_personality and .cfi_lsda directives, per subsection .cfi_*
    directives, better .eh_frame CIE merging

* Thu Nov  9 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.6-3
- fix popcnt instruction assembly and disassembly on amd64 (#214767)

* Mon Oct 23 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.6-2
- update to 2.17.50.0.6
  - fix for section relative linker script defined symbols in
    empty sections (#207598, BZ#3267)
  - fix handling of DW_CFA_set_loc in .eh_frame optimizations
  - fix R_PPC_{PLT,GOT{,_TLSGD,_TLSLD,_TPREL,_DTPREL}}16_HA relocation
    handling with weak undefined symbols (Alan Modra, #211094)

* Tue Sep 12 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.3-6
- fix multilib conflict in %%{_prefix}/include/bfd.h

* Tue Sep 12 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.3-5
- fix efi-app-ia64 magic number (#206002, BZ#3171)

* Tue Sep  5 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.3-4
- link libopcodes*.so against libbfd*.so (#202327)
- split *.a and header files into binutils-devel

* Fri Aug 18 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.3-3
- on ppc and ppc64 increase default -z commonpagesize to 64K (#203001)

* Fri Jul 28 2006 Alexandre Oliva <aoliva@redhat.com> 2.17.50.0.3-2
- do not infer x86 arch implicitly based on instruction in the input
  (#200330)

* Mon Jul 17 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.3-1
- update to 2.17.50.0.3

* Fri Jul 14 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.2-8
- add support for new AMDFAM10 instructions (#198281, IT#97662)
- add -march=/-mtune= gas support on x86/x86-64
- x86/x86-64 nop insn improvements
- fix DT_GNU_HASH shift count value computation

* Tue Jul 11 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.2-7
- add DT_GNU_HASH support (--hash-style=gnu and --hash-style=both
  ld options)

* Thu Jun 29 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.2-4
- fix i?86 TLS GD->IE transition in executables (#196157, BZ#2513)

* Mon Jun 19 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.2-3
- fix two places in ld that misbehaved with MALLOC_PERTURB_=N
- fix .tls_common handling in relocatable linking

* Mon Jun  5 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.2-2
- fix --as-needed (Alan Modra, #193689, BZ#2721)

* Thu Jun  1 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.2-1
- update to 2.17.50.0.2
- update from CVS to 20060601
- speed up the ELF linker by caching the result of kept section check
  (H.J. Lu)

* Tue May  9 2006 Jakub Jelinek <jakub@redhat.com> 2.17.50.0.1-1
- update to 2.17.50.0.1

* Fri Mar 31 2006 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.6-6
- fix ld error message formatting, so that collect2 parser can
  parse it again for g++ -frepo (#187142)

* Thu Mar  9 2006 Alexandre Oliva <aoliva@redhat.com> 2.16.91.0.6-4
- fix relaxation of TLS GD to LE on PPC (#184590)

* Fri Mar  3 2006 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.6-3
- support DW_CFA_val_{offset,offset_sf,expression} in readelf/objdump

* Tue Feb 28 2006 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.6-2
- add MNI support on i?86/x86_64 (#183080)
- support S signal frame augmentation flag in .eh_frame,
  add .cfi_signal_frame support (#175951, PR other/26208, BZ#300)

* Tue Feb 14 2006 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.6-1
- update to 2.16.91.0.6
  - fix ppc64 --gc-sections
  - disassembler fixes for x86_64 cr/debug regs
  - fix linker search order for DT_NEEDED libs

* Mon Jan 02 2006 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.5-1
- update to 2.16.91.0.5
- don't error about .toc1 references to discarded sectiosn on ppc64
  (#175944)

* Wed Dec 14 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.3-2
- put .gnu.linkonce.d.rel.ro.* sections into relro region

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.3-1
- update to 2.16.91.0.3
- add .weakref support (Alexandre Oliva, #115157, #165728)

* Thu Aug 18 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.2-4
- install-info also configure.info
- update standards.texi from gnulib (#165530)

* Tue Aug 16 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.2-3
- update to 20050816 CVS
- better fix for ld-cdtest
- fix symbol version script parsing

* Fri Jul 29 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.2-2
- don't complain about relocs to discarded sections in ppc32
  .got2 sections (Alan Modra, PR target/17828)

* Fri Jul 22 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.2-1
- update to 2.16.91.0.2

* Thu Jul 21 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.1-3
- fix buffer overflow in readelf ia64 unwind printing code
- use vsnprintf rather than vsprintf in gas diagnostics (Tavis Ormandy)
- fix ld-cdtest when CFLAGS contains -fexceptions

* Wed Jul 20 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.1-2
- update to 20050720 CVS

* Mon Jul 11 2005 Jakub Jelinek <jakub@redhat.com> 2.16.91.0.1-1
- update to 2.16.91.0.1 plus 20050708 CVS

* Wed Jun 15 2005 Jakub Jelinek <jakub@redhat.com> 2.16.90.0.3-1
- update to 2.16.90.0.3
- update to 20050615 CVS
  - ppc32 secure PLT support (Alan Modra)
- further bfd/readelf robustification

* Sat Jun 11 2005 Jakub Jelinek <jakub@redhat.com> 2.15.94.0.2.2-4
- further bfd robustification (CAN-2005-1704, #158680)

* Fri Jun 10 2005 Jakub Jelinek <jakub@redhat.com> 2.15.94.0.2.2-3
- further objdump and readelf robustification (CAN-2005-1704, #158680)

* Wed May 25 2005 Jakub Jelinek <jakub@redhat.com> 2.15.94.0.2.2-2
- bfd and readelf robustification (CAN-2005-1704, #158680)

* Tue Mar 29 2005 Jakub Jelinek <jakub@redhat.com> 2.15.94.0.2.2-1
- update to 2.15.94.0.2.2
- speed up walk_wild_section (Robert O'Callahan)

* Mon Mar  7 2005 Jakub Jelinek <jakub@redhat.com> 2.15.94.0.2-4
- rebuilt with GCC 4

* Mon Feb 28 2005 Jakub Jelinek <jakub@redhat.com> 2.15.94.0.2-3
- fix buffer overflows in readelf (#149506)
- move c++filt to binutils from gcc-c++, conflict with gcc-c++ < 4.0 (#86333)

* Thu Feb 10 2005 Jakub Jelinek <jakub@redhat.com> 2.15.94.0.2-1
- update to 2.15.94.0.2
- fix .note.GNU-stack/PT_GNU_STACK computation in linker on ppc64 (#147296)
- fix stripping of binaries/libraries that have empty sections right before
  .dynamic section (with the same starting address; #144038)
- handle AS_NEEDED (...) in linker script INPUT/GROUP

* Tue Dec 14 2004 Jakub Jelinek <jakub@redhat.com> 2.15.92.0.2-11
- fix a longstanding -z relro bug

* Mon Dec 13 2004 Jakub Jelinek <jakub@redhat.com> 2.15.92.0.2-10
- avoid unnecessary gap with -z relro showing on i686 libc.so
- ppc64 --emit-relocs fix (Alan Modra)
- don't crash if STT_SECTION symbol has incorrect st_shndx (e.g. SHN_ABS,
  as created by nasm; #142181)
- don't try to make absptr LSDAs relative if they don't have relocations
  against them (Alan Modra, #141162)

* Wed Oct 27 2004 Jakub Jelinek <jakub@redhat.com> 2.15.92.0.2-5.EL4
- fix ar xo (#104344)

* Wed Oct 20 2004 Jakub Jelinek <jakub@redhat.com> 2.15.92.0.2-5
- fix --just-symbols on ppc64 (Alan Modra, #135498)

* Fri Oct 15 2004 Jakub Jelinek <jakub@redhat.com> 2.15.92.0.2-4
- fix code detecting matching linkonce and single member comdat
  group sections (#133078)

* Mon Oct 11 2004 Jakub Jelinek <jakub@redhat.com> 2.15.92.0.2-3
- revert Sep 09 change to make ppc L second argument e.g. for tlbie
  non-optional
- fix stripping of prelinked binaries and libraries (#133734)
- allow strings(1) on 32-bit arches to be used again with > 2GB
  files (#133555)

* Mon Oct  4 2004 Jakub Jelinek <jakub@redhat.com> 2.15.92.0.2-2
- update to 2.15.92.0.2
- change ld's ld.so.conf parser to match ldconfig's (#129340)

* Mon Sep 20 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-9
- avoid almost 1MB (sparse) gaps in the middle of -z relro
  libraries on x86-64 (Andreas Schwab)
- fix -z relro to make sure end of PT_GNU_RELRO segment is always
  COMMONPAGESIZE aligned

* Mon Aug 16 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-8
- fix linker segfaults on input objects with SHF_LINK_ORDER with
  incorrect sh_link (H.J.Lu, Nick Clifton, #130198, BZ #290)

* Mon Aug 16 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-7
- resolve all undefined ppc64 .* syms to the function bodies through
  .opd, not just those used in brach instructions (Alan Modra)

* Mon Aug 16 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-6
- fix ppc64 ld --dotsyms (Alan Modra)

* Mon Aug 16 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-5
- various ppc64 make check fixes when using non-dot-syms gcc (Alan Modra)
- fix --gc-sections
- on ia64 create empty .gnu.linkonce.ia64unw*.* sections for
  .gnu.linkonce.t.* function doesn't need unwind info

* Mon Aug 16 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-4
- kill ppc64 dot symbols (Alan Modra)
- objdump -d support for objects without dot symbols
- support for overlapping ppc64 .opd entries

* Mon Aug 9 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-3
- fix a newly introduced linker crash on x86-64

* Sun Aug 8 2004 Alan Cox <alan@redhat.com> 2.15.91.0.2-2
- BuildRequire bison and macroise buildroot - from Steve Grubb

* Fri Jul 30 2004 Jakub Jelinek <jakub@redhat.com> 2.15.91.0.2-1
- update to 2.15.91.0.2
- BuildRequire flex (#117763)

* Wed May 19 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.3-7
- use lib64 instead of lib directories on ia64 if %%{_lib} is
  set to lib64 by rpm

* Sat May 15 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.3-6
- fix a bug introduced in the ++/-- rejection patch
  from 2.15.90.0.3 (Alan Modra)

* Tue May  4 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.3-5
- fix s390{,x} .{,b,p2}align handling
- ppc/ppc64 testsuite fix

* Mon May  3 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.3-4
- -z relro ppc/ppc64/ia64 fixes
- change x86-64 .plt symbol st_size handling to match ia32
- prettify objdump -d output

* Tue Apr 20 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.3-3
- several SPARC fixes

* Sun Apr 18 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.3-2
- yet another fix for .tbss handling

* Fri Apr 16 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.3-1
- update to 2.15.90.0.3

* Fri Mar 26 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.1.1-2
- update to 20040326 CVS
  - fix ppc64 weak .opd symbol handling (Alan Modra, #119086)
- fix .tbss handling bug introduced

* Fri Mar 26 2004 Jakub Jelinek <jakub@redhat.com> 2.15.90.0.1.1-1
- update to 2.15.90.0.1.1

* Sat Feb 21 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-8
- with -z now without --enable-new-dtags create DT_BIND_NOW
  dynamic entry in addition to DT_FLAGS_1 with DF_1_NOW bit set

* Fri Feb 20 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-7
- fix -pie on ppc32

* Fri Feb 20 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-6
- clear .plt sh_entsize on sparc32
- put whole .got into relro area with -z now -z relro

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 22 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-4
- fix -pie on IA64

* Mon Jan 19 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-3
- fix testcases on s390 and s390x

* Fri Jan 16 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-2
- fix testcases on AMD64
- fix .got's sh_entsize on IA32/AMD64
- set COMMONPAGESIZE on s390/s390x
- set COMMONPAGESIZE on ppc32 (Alan Modra)

* Fri Jan 16 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.8-1
- update to 2.14.90.0.8

* Tue Jan 13 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.7-4
- fix -z relro on 64-bit arches

* Mon Jan 12 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.7-3
- fix some bugs in -z relro support

* Fri Jan  9 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.7-2
- -z relro support, reordering of RW sections

* Fri Jan  9 2004 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.7-1
- update to 2.14.90.0.7

* Mon Nov 24 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-4
- fix assembly parsing of foo=(.-bar)/4 (Alan Modra)
- fix IA-64 assembly parsing of (p7) hint @pause

* Tue Sep 30 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-3
- don't abort on some linker warnings/errors on IA-64

* Sat Sep 20 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-2
- fix up merge2.s to use .p2align instead of .align

* Sat Sep 20 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.6-1
- update to 2.14.90.0.6
- speed up string merging (Lars Knoll, Michael Matz, Alan Modra)
- speed up IA-64 local symbol handling during linking

* Fri Sep  5 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-7
- avoid ld -s segfaults introduced in 2.14.90.0.5-5 (Dmitry V. Levin,
  #103180)

* Fri Aug 29 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-6
- build old demangler into libiberty.a (#102268)
- SPARC .cfi* support

* Tue Aug  5 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-5
- fix orphan section placement

* Tue Jul 29 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-4
- fix ppc64 elfvsb linker tests
- some more 64-bit cleanliness fixes, give ppc64 fdesc symbols
  type and size (Alan Modra)

* Tue Jul 29 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-3
- fix 64-bit unclean code in ppc-opc.c

* Mon Jul 28 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-2
- fix 64-bit unclean code in tc-ppc.c

* Mon Jul 28 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.5-1
- update to 2.14.90.0.5
- fix ld -r on ppc64 (Alan Modra)

* Fri Jul 18 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-23
- rebuilt

* Thu Jul 17 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-22
- fix elfNN_ia64_dynamic_symbol_p (Richard Henderson, #86661)
- don't access memory beyond what was allocated in readelf
  (Richard Henderson)

* Thu Jul 10 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-21
- add .cfi_* support on ppc{,64} and s390{,x}

* Tue Jul  8 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-20
- remove lib{bfd,opcodes}.la (#98190)

* Mon Jul  7 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-19
- fix -pie support on amd64, s390, s390x and ppc64
- issue relocation overflow errors for s390/s390x -fpic code when
  accessing .got slots above 4096 bytes from .got start

* Thu Jul  3 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-18
- rebuilt

* Thu Jul  3 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-17
- fix ia64 -pie support
- require no undefined non-weak symbols in PIEs like required for normal
  binaries

* Wed Jul  2 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-16
- fix readelf -d on IA-64
- build libiberty.a with -fPIC, so that it can be lined into shared
  libraries

* Wed Jun 25 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-15
- rebuilt

* Wed Jun 25 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-14
- added support for Intel Prescott instructions
- fix hint@pause for ia64
- add workaround for LTP sillyness (#97934)

* Wed Jun 18 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-13
- update CFI stuff to 2003-06-18
- make sure .eh_frame is aligned to 8 bytes on 64-bit arches,
  remove padding within one .eh_frame section

* Tue Jun 17 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-12
- rebuilt

* Tue Jun 17 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-11
- one more fix for the same patch

* Tue Jun 17 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-10
- fix previous patch

* Mon Jun 16 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-9
- ensure R_PPC64_{RELATIVE,ADDR64} have *r_offset == r_addend
  and the other relocs have *r_offset == 0

* Tue Jun 10 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-8
- remove some unnecessary provides in ppc64 linker script
  which were causing e.g. empty .ctors/.dtors section creation

* Fri Jun  6 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-7
- some CFI updates/fixes
- don't create dynamic relocations against symbols defined in PIE
  exported from its .dynsym

* Wed Jun  4 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-6
- update gas to 20030604
- PT_GNU_STACK support

* Mon Jun  2 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-5
- buildrequire gettext (#91838)

* Sat May 31 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-4
- fix shared libraries with >= 8192 .plt slots on ppc32

* Thu May 29 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-3
- rebuilt

* Thu May 29 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-2
- rename ld --dynamic option to --pic-executable or --pie
- fix ld --help output
- document --pie/--pic-executable in ld.info and ld.1

* Wed May 28 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.4-1
- update to 2.14.90.0.4-1
- gas CFI updates (Richard Henderson)
- dynamic executables (Ulrich Drepper)

* Tue May 20 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.2-2
- fix ELF visibility handling
- tidy plt entries on IA-32, ppc and ppc64

* Mon May 19 2003 Jakub Jelinek <jakub@redhat.com> 2.14.90.0.2-1
- update to 2.14.90.0.2-1

* Tue May 13 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-8
- fix bfd_elf_hash on 64-bit arches (Andrew Haley)

* Wed Apr 30 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-7
- rebuilt

* Mon Apr 14 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-6
- optimize DW_CFA_advance_loc4 in gas even if there is 'z' augmentation
  with size 0 in FDE

* Fri Apr 11 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-5
- fix SPARC build

* Thu Apr  3 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-4
- fix ppc32 plt reference counting
- don't include %%{_prefix}/%%{_lib}/debug in the non-debuginfo package
  (#87729)

* Mon Mar 31 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-3
- make elf64ppc target native extra on ppc and elf32ppc native extra
  on ppc64.

* Fri Mar 28 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-2
- fix TLS on IA-64 with ld relaxation

* Sat Mar 22 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.20-1
- update to 2.13.90.0.20

* Mon Feb 24 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-9
- rebuilt

* Mon Feb 24 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-8
- don't strip binaries in %%install, so that there is non-empty
  debuginfo

* Mon Feb 24 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-7
- don't optimize .eh_frame during ld -r

* Thu Feb 13 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-6
- don't clear elf_link_hash_flags in the .symver patch
- only use TC_FORCE_RELOCATION in s390's TC_FORCE_RELOCATION_SUB_SAME
  (Alan Modra)

* Mon Feb 10 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-5
- fix the previous .symver change
- remove libbfd.so and libopcodes.so symlinks, so that other packages
  link statically, not dynamically against libbfd and libopcodes
  whose ABI is everything but stable

* Mon Feb 10 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-4
- do .symver x, x@FOO handling earlier
- support .file and .loc on s390*

* Mon Feb 10 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-3
- handle .symver x, x@FOO in ld such that relocs against x become
  dynamic relocations against x@FOO (#83325)
- two PPC64 TLS patches (Alan Modra)

* Sun Feb 09 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-2
- fix SEARCH_DIR on x86_64/s390x
- fix Alpha --relax
- create DT_RELA{,SZ,ENT} on s390 even if there is just .rela.plt
  and no .rela.dyn section
- support IA-32 on IA-64 (#83752)
- .eh_frame_hdr fix (Andreas Schwab)

* Thu Feb 06 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.18-1
- update to 2.13.90.0.18 + 20030121->20030206 CVS diff

* Tue Feb 04 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-8
- alpha TLS fixes
- use .debug_line directory table to make the section tiny bit smaller
- libtool fix from Jens Petersen

* Sun Feb 02 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-7
- sparc32 TLS

* Fri Jan 24 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-6
- s390{,x} TLS and two other mainframe patches

* Fri Jan 17 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-5
- fix IA-64 TLS IE in shared libs
- .{preinit,init,fini}_array compat hack from Alexandre Oliva

* Thu Jan 16 2003 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-4
- IA-64 TLS fixes
- fix .plt sh_entsize on Alpha
- build with %%_smp_mflags

* Sat Nov 30 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-3
- fix strip on TLS binaries and libraries

* Fri Nov 29 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-2
- fix IA-64 ld bootstrap

* Thu Nov 28 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.16-1
- update to 2.13.90.0.16
- STT_TLS SHN_UNDEF fix

* Wed Nov 27 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.10-4
- pad .rodata.cstNN sections at the end if they aren't sized to multiple
  of sh_entsize
- temporary patch to make .eh_frame and .gcc_except_table sections
  readonly if possible (should be removed when AUTO_PLACE is implemented)
- fix .PPC.EMB.apuinfo section flags

* Wed Oct 23 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.10-3
- fix names and content of alpha non-alloced .rela.* sections (#76583)
- delete unpackaged files from the buildroot

* Tue Oct 15 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.10-2
- enable s390x resp. s390 emulation in linker too

* Mon Oct 14 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.10-1
- update to 2.13.90.0.10
- add a bi-arch patch for sparc/s390/x86_64
- add --enable-64-bit-bfd on sparc, s390 and ppc

* Thu Oct 10 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.4-3
- fix combreloc testcase

* Thu Oct 10 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.4-2
- fix orphan .rel and .rela section placement with -z combreloc (Alan Modra)
- skip incompatible linker scripts when searching for libraries

* Tue Oct  1 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.4-1
- update to 2.13.90.0.4
- x86-64 TLS support
- some IA-32 TLS fixes
- some backported patches from trunk
- include opcodes, ld, gas and bfd l10n too

* Thu Sep 19 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.2-3
- allow addends for IA-32 TLS @tpoff, @ntpoff and @dtpoff
- clear memory at *r_offset of dynamic relocs on PPC
- avoid ld crash if accessing non-local symbols through LE relocs
- new IA-32 TLS relocs, bugfixes and testcases
- use brl insn on IA-64 (Richard Henderson)
- fix R_IA64_PCREL21{M,F} handling (Richard Henderson)
- build in separate builddir, so that gasp tests don't fail
- include localization

* Thu Aug  8 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.2-2
- fix R_386_TPOFF32 addends (#70824)

* Sat Aug  3 2002 Jakub Jelinek <jakub@redhat.com> 2.13.90.0.2-1
- update to 2.13.90.0.2
  - fix ld TLS assertion failure (#70084)
  - fix readelf --debug-dump= handling to match man page and --help
    (#68997)
- fix _GLOBAL_OFFSET_TABLE gas handling (#70241)

* Wed Jul 24 2002 Jakub Jelinek <jakub@redhat.com> 2.12.90.0.15-1
- update to 2.12.90.0.15
- TLS .tbss fix
- don't use rpm %%configure macro, it is broken too often (#69366)

* Thu May 30 2002 Jakub Jelinek <jakub@redhat.com> 2.12.90.0.9-1
- update to 2.12.90.0.9
  - TLS support
- remove gasp.info from %%post/%%preun (#65400)

* Mon Apr 29 2002 Jakub Jelinek <jakub@redhat.com> 2.12.90.0.7-1
- update to 2.12.90.0.7
- run make check

* Mon Apr 29 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-12
- fix .hidden handling on SPARC (Richard Henderson)
- don't crash when linking -shared non-pic code with SHF_MERGE
- fix .eh_frame_hdr for DW_EH_PE_aligned
- correctly adjust DW_EH_PE_pcrel encoded personalities in CIEs

* Fri Apr  5 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-11
- don't emit dynamic R_SPARC_DISP* relocs against STV_HIDDEN symbols
  into shared libraries

* Thu Mar 21 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-10
- don't merge IA-64 unwind info sections together during ld -r

* Mon Mar 11 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-9
- fix DATA_SEGMENT_ALIGN on ia64/alpha/sparc/sparc64

* Fri Mar  8 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-8
- don't crash on SHN_UNDEF local dynsyms (Andrew MacLeod)

* Thu Mar  7 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-7
- fix bfd configury bug (Alan Modra)

* Tue Mar  5 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-6
- don't copy visibility when equating symbols
- fix alpha .text/.data with .previous directive bug

* Tue Mar  5 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-5
- fix SHF_MERGE crash with --gc-sections (#60369)
- C++ symbol versioning patch

* Fri Feb 22 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-4
- add DW_EH_PE_absptr -> DW_EH_PE_pcrel optimization for shared libs,
  if DW_EH_PE_absptr cannot be converted that way, don't build the
  .eh_frame_hdr search table

* Fri Feb 15 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-3
- fix ld -N broken by last patch

* Tue Feb 12 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-2
- trade one saved runtime page for data segment (=almost always not shared)
  for up to one page of disk space where possible

* Fri Feb  8 2002 Jakub Jelinek <jakub@redhat.com> 2.11.93.0.2-1
- update to 2.11.93.0.2
- use %%{ix86} instead of i386 for -z combreloc default (#59086)

* Thu Jan 31 2002 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-10
- don't create SHN_UNDEF STB_WEAK symbols unless there are any relocations
  against them

* Wed Jan 30 2002 Bill Nottingham <notting@redhat.com> 2.11.92.0.12-9.1
- rebuild (fix ia64 miscompilation)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 28 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-8
- two further .eh_frame patch fixes

* Wed Dec 19 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-7
- as ld is currently not able to shrink input sections to zero size
  during discard_info, build a fake minimal CIE in that case
- update elf-strtab patch to what was commited

* Mon Dec 17 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-6
- one more .eh_frame patch fix
- fix alpha .eh_frame handling
- optimize elf-strtab finalize

* Sat Dec 15 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-5
- yet another fix for the .eh_frame patch

* Fri Dec 14 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-4
- Alan Modra's patch to avoid crash if there is no dynobj

* Thu Dec 13 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-3
- H.J.'s patch to avoid crash if input files are not ELF
- don't crash if a SHF_MERGE for some reason could not be merged
- fix objcopy/strip to preserve SHF_MERGE sh_entsize
- optimize .eh_frame sections, add PT_GNU_EH_FRAME support
- support anonymous version tags in version script

* Tue Nov 27 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-2
- fix IA-64 SHF_MERGE handling

* Tue Nov 27 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.12-1
- update to 2.11.92.0.12
  - optimize .dynstr and .shstrtab sections (#55524)
  - fix ld.1 glitch (#55459)
- turn relocs against SHF_MERGE local symbols with zero addend
  into STT_SECTION + addend
- remove man pages for programs not included (nlmconv, windres, dlltool;
  #55456, #55461)
- add BuildRequires for texinfo

* Thu Oct 25 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.7-2
- duh, fix strings on bfd objects (#55084)

* Sat Oct 20 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.7-1
- update to 2.11.92.0.7
- remove .rel{,a}.dyn from output if it is empty

* Thu Oct 11 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.5-2
- fix strings patch
- use getc_unlocked in strings to speed it up by 50% on large files

* Wed Oct 10 2001 Jakub Jelinek <jakub@redhat.com> 2.11.92.0.5-1
- update to 2.11.92.0.5
  - binutils localization (#45148)
  - fix typo in REPORT_BUGS_TO (#54325)
- support files bigger than 2GB in strings (#54406)

* Wed Sep 26 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-12
- on IA-64, don't mix R_IA64_IPLTLSB relocs with non-PLT relocs in
  .rela.dyn section.

* Tue Sep 25 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-11
- add iplt support for IA-64 (Richard Henderson)
- switch to new section flags for SHF_MERGE and SHF_STRINGS, put
  in compatibility code
- "s" section flag for small data sections on IA-64 and Alpha
  (Richard Henderson)
- fix sparc64 .plt[32768+] handling
- don't emit .rela.stab on sparc

* Mon Sep 10 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-10
- fix SHF_MERGE on Sparc

* Fri Aug 31 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-9
- on Alpha, copy *r_offset to R_ALPHA_RELATIVE's r_addend

* Thu Aug 30 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-8
- on IA-64, put crtend{,S}.o's .IA_64.unwind section last in
  .IA_64.unwind output section (for compatibility with 7.1 eh)

* Fri Aug 24 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-7
- put RELATIVE relocs first, not last
- enable -z combreloc by default on IA-{32,64}, Alpha, Sparc*

* Thu Aug 23 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-6
- support for -z combreloc
- remove .dynamic patch, -z combreloc patch does this better
- set STT_FUNC default symbol sizes in .endp directive on IA-64

* Mon Jul 16 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-5
- fix last patch (H.J.Lu)

* Fri Jul 13 2001 Jakub Jelinek <jakub@redhat.com> 2.11.90.0.8-4
- fix placing of orphan sections

* Sat Jun 23 2001 Jakub Jelinek <jakub@redhat.com>
- fix SHF_MERGE support on Alpha

* Fri Jun  8 2001 Jakub Jelinek <jakub@redhat.com>
- 2.11.90.0.8
  - some SHF_MERGE suport fixes
- don't build with tooldir /usrusr instead of /usr (#40937)
- reserve few .dynamic entries for prelinking

* Mon Apr 16 2001 Jakub Jelinek <jakub@redhat.com>
- 2.11.90.0.5
  - SHF_MERGE support

* Tue Apr  3 2001 Jakub Jelinek <jakub@redhat.com>
- 2.11.90.0.4
  - fix uleb128 support, so that CVS gcc bootstraps
  - some ia64 fixes

* Mon Mar 19 2001 Jakub Jelinek <jakub@redhat.com>
- add -Bgroup support from Ulrich Drepper

* Fri Mar  9 2001 Jakub Jelinek <jakub@redhat.com>
- hack - add elf_i386_glibc21 emulation

* Fri Feb 16 2001 Jakub Jelinek <jakub@redhat.com>
- 2.10.91.0.2

* Fri Feb  9 2001 Jakub Jelinek <jakub@redhat.com>
- 2.10.1.0.7
- remove ExcludeArch ia64
- back out the -oformat, -omagic and -output change for now

* Fri Dec 15 2000 Jakub Jelinek <jakub@redhat.com>
- Prereq /sbin/install-info

* Tue Nov 21 2000 Jakub Jelinek <jakub@redhat.com>
- 2.10.1.0.2

* Tue Nov 21 2000 Jakub Jelinek <jakub@redhat.com>
- add one more alpha patch

* Wed Nov 15 2000 Jakub Jelinek <jakub@redhat.com>
- fix alpha visibility as problem
- add support for Ultra-III

* Fri Sep 15 2000 Jakub Jelinek <jakub@redhat.com>
- and one more alpha patch

* Fri Sep 15 2000 Jakub Jelinek <jakub@redhat.com>
- two sparc patches

* Mon Jul 24 2000 Jakub Jelinek <jakub@redhat.com>
- 2.10.0.18

* Mon Jul 10 2000 Jakub Jelinek <jakub@redhat.com>
- 2.10.0.12

* Mon Jun 26 2000 Jakub Jelinek <jakub@redhat.com>
- 2.10.0.9

* Thu Jun 15 2000 Jakub Jelinek <jakub@redhat.com>
- fix ld -r

* Mon Jun  5 2000 Jakub Jelinek <jakub@redhat.com>
- 2.9.5.0.46
- use _mandir/_infodir/_lib

* Mon May  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.9.5.0.41

* Wed Apr 12 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.9.5.0.34

* Wed Mar 22 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.9.5.0.31

* Fri Feb 04 2000 Cristian Gafton <gafton@redhat.com>
- man pages are compressed
- apply kingdon's patch from #5031

* Wed Jan 19 2000 Jeff Johnson <jbj@redhat.com>
- Permit package to be built with a prefix other than /usr.

* Thu Jan 13 2000 Cristian Gafton <gafton@redhat.com>
- add pacth from hjl to fix the versioning problems in ld

* Tue Jan 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add sparc patches from Jakub Jelinek <jakub@redhat.com>
- Add URL:

* Tue Dec 14 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.9.5.0.22

* Wed Nov 24 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.9.5.0.19

* Sun Oct 24 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.9.5.0.16

* Mon Sep 06 1999 Jakub Jelinek <jj@ultra.linux.cz>
- make shared non-pic libraries work on sparc with glibc 2.1.

* Fri Aug 27 1999 Jim Kingdon
- No source/spec changes, just rebuilding with egcs-1.1.2-18 because
  the older egcs was miscompling gprof.

* Mon Apr 26 1999 Cristian Gafton <gafton@redhat.com>
- back out very *stupid* sparc patch done by HJLu. People, keep out of
  things you don't understand.
- add alpha relax patch from rth

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- version  2.9.1.0.23
- patch to make texinfo documentation compile
- auto rebuild in the new build environment (release 2)

* Tue Feb 23 1999 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.1.0.21
- merged with UltraPenguin

* Mon Jan 04 1999 Cristian Gafton <gafton@redhat.com>
- added ARM patch from philb
- version 2.9.1.0.19a
- added a patch to allow arm* arch to be identified as an ARM

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.1.0.14.

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.13.

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.1.0.12

* Thu Jul  2 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.7.

* Wed Jun 03 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.6.

* Tue Jun 02 1998 Erik Troan <ewt@redhat.com>
- added patch from rth to get right offsets for sections in relocateable
  objects on sparc32

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- version 2.9.1.0.4 is out; even more, it is public !

* Tue May 05 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.9.1.0.3.

* Mon Apr 20 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.9.0.3

* Tue Apr 14 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.9.0.2

* Sun Apr 05 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8.1.0.29 (HJ warned me that this thing is a moving target...
  :-)
- "fixed" the damn make install command so that all tools get installed

* Thu Apr 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded again to 2.8.1.0.28 (at least on alpha now egcs will compile)
- added info packages handling

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.8.1.0.23

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8.1.0.15 (required to compile the newer glibc)
- all patches are obsoleted now

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added 2.8.1.0.1 patch from hj
- added patch for alpha palcode form rth

