%{?scl:%scl_package glibc}
%{!?scl:%global pkg_name %{name}}
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

%define glibcsrcdir glibc-2.12-2-gc4ccff1
%define glibcversion 2.12
%define glibcrelease 1.212%{?dist}
%define run_glibc_tests 1
%define auxarches athlon sparcv9v sparc64v alphaev6
%define xenarches i686 athlon
%ifarch %{xenarches}
%define buildxen 1
%define xenpackage 0
%else
%define buildxen 0
%define xenpackage 0
%endif
%ifarch ppc ppc64
%define buildpower6 1
%else
%define buildpower6 0
%endif
%define rtkaioarches %{ix86} x86_64 ppc ppc64 s390 s390x
%define biarcharches %{ix86} x86_64 ppc ppc64 s390 s390x
%define debuginfocommonarches %{biarcharches} alpha alphaev6 sparc sparcv9 sparcv9v sparc64 sparc64v
%define multiarcharches ppc ppc64 %{ix86} x86_64
%define systemtaparches %{ix86} x86_64 ppc ppc64 s390 s390x

Summary: The GNU libc libraries
Name: devtoolset-3-glibc
Version: %{glibcversion}
Release: %{glibcrelease}
# GPLv2+ is used in a bunch of programs, LGPLv2+ is used for libraries.
# Things that are linked directly into dynamically linked programs
# and shared libraries (e.g. crt files, lib*_nonshared.a) have an additional
# exception which allows linking it into any kind of programs or shared
# libraries without restrictions.
License: LGPLv2+ and LGPLv2+ with exceptions and GPLv2+
Group: System Environment/Libraries
URL: http://sources.redhat.com/glibc/
Source0: %{?glibc_release_url}%{glibcsrcdir}.tar.bz2
Source1: %{glibcsrcdir}-releng.tar.bz2
Patch0: glibc-fedora.patch
Patch2: glibc-rh587360.patch
Patch3: glibc-rh582738.patch
Patch4: glibc-getlogin-r.patch
Patch5: glibc-localedata.patch
Patch6: glibc-rh593396.patch
Patch7: glibc-recvmmsg.patch
Patch8: glibc-aliasing.patch
Patch9: glibc-rh593686.patch
Patch10: glibc-rh607461.patch
Patch11: glibc-rh621959.patch
Patch12: glibc-rh607010.patch
Patch13: glibc-rh630801.patch
Patch14: glibc-rh631011.patch
Patch15: glibc-rh641128.patch
Patch16: glibc-rh642584.patch
Patch17: glibc-rh643822.patch
Patch18: glibc-rh645672.patch
Patch19: glibc-rh580498.patch
Patch20: glibc-rh615090.patch
Patch21: glibc-rh623187.patch
Patch22: glibc-rh646954.patch
Patch23: glibc-rh647448.patch
Patch24: glibc-rh615701.patch
Patch25: glibc-rh652661.patch
Patch26: glibc-rh656530.patch
Patch27: glibc-rh656014.patch
Patch28: glibc-rh661982.patch
Patch29: glibc-rh601686.patch
Patch30: glibc-rh676076.patch
Patch31: glibc-rh667974.patch
Patch32: glibc-rh625893.patch
Patch33: glibc-rh681054.patch
Patch34: glibc-rh689471.patch
Patch35: glibc-rh692177.patch
Patch36: glibc-rh692838.patch
Patch37: glibc-rh703480.patch
Patch38: glibc-rh705465.patch
Patch39: glibc-rh703481.patch
Patch40: glibc-rh694386.patch
Patch41: glibc-rh676591.patch
Patch42: glibc-rh711987.patch
Patch43: glibc-rh695595.patch
Patch45: glibc-rh695963.patch
Patch46: glibc-rh713134.patch
Patch47: glibc-rh714823.patch
Patch48: glibc-rh718057.patch
Patch49: glibc-rh688980.patch
Patch50: glibc-rh712248.patch
Patch51: glibc-rh731042.patch
Patch52: glibc-rh730379.patch
Patch53: glibc-rh700507.patch
Patch54: glibc-rh699724.patch
Patch55: glibc-rh736346.patch
Patch56: glibc-rh737778.patch
Patch57: glibc-rh738665.patch
Patch58: glibc-rh738763.patch
Patch59: glibc-rh739184.patch
Patch60: glibc-rh711927.patch
Patch61: glibc-rh688720.patch
Patch62: glibc-rh726517.patch
Patch63: glibc-rh752122.patch
Patch64: glibc-rh739971.patch
Patch65: glibc-rh751750.patch
Patch66: glibc-rh740506.patch
Patch67: glibc-rh757888.patch
Patch68: glibc-rh750531.patch
Patch69: glibc-rh749188.patch
Patch70: glibc-rh767746.patch
Patch72: glibc-rh767693.patch
Patch73: glibc-rh740506-2.patch
Patch74: glibc-rh696472.patch
Patch75: glibc-rh771342.patch
Patch76: glibc-rh657572.patch
Patch77: glibc-rh767693-2.patch
Patch78: glibc-rh782585.patch
Patch79: glibc-rh784402.patch
Patch80: glibc-rh697421.patch
Patch81: glibc-rh785984.patch
Patch82: glibc-rh767146.patch
Patch83: glibc-rh766513.patch
Patch84: glibc-rh789209.patch
Patch85: glibc-rh788959.patch
Patch86: glibc-rh789189.patch
Patch88: glibc-rh789238.patch
Patch89: glibc-rh794817.patch
Patch90: glibc-rh797094-1.patch
Patch91: glibc-rh797094-2.patch
Patch92: glibc-rh789238-2.patch
Patch93: glibc-rh795498.patch
Patch94: glibc-rh794817-2.patch
Patch95: glibc-rh804689.patch
Patch96: glibc-rh809602.patch
Patch97: glibc-rh808337.patch
Patch99: glibc-rh788959-2.patch
Patch100: glibc-rh808545.patch
Patch101: glibc-rh833717.patch
Patch103: glibc-rh823909.patch
Patch104: glibc-rh826149.patch
Patch105: glibc-rh841787.patch
Patch106: glibc-rh809726.patch
Patch107: glibc-rh806404.patch
Patch108: glibc-rh832516.patch
Patch109: glibc-rh830127.patch
Patch110: glibc-rh832694.patch
Patch111: glibc-rh843673.patch
Patch112: glibc-rh847932.patch
Patch113: glibc-rh837918.patch
Patch114: glibc-rh849203.patch
Patch115: glibc-rh849651.patch
Patch116: glibc-rh827362.patch
Patch117: glibc-rh837695.patch
Patch118: glibc-rh804686.patch
Patch119: glibc-rh848082.patch
Patch120: glibc-rh846342.patch
Patch121: glibc-rh852445.patch
Patch122: glibc-rh861167.patch
Patch123: glibc-rh863453.patch
Patch124: glibc-rh864322.patch
Patch125: glibc-rh929388.patch
Patch126: glibc-rh919562.patch
Patch127: glibc-rh886968.patch
Patch128: glibc-rh966775.patch
Patch129: glibc-rh834386.patch
Patch130: glibc-rh834386-2.patch
Patch131: glibc-rh862094.patch
Patch132: glibc-rh851470.patch
Patch133: glibc-rh868808.patch
Patch134: glibc-rh552960.patch
Patch135: glibc-rh663641.patch
Patch136: glibc-rh663641-2.patch
Patch137: glibc-rh848748.patch
Patch138: glibc-rh952422.patch
Patch139: glibc-rh663641-3.patch
Patch140: glibc-rh916986.patch
Patch141: glibc-rh970776.patch
Patch142: glibc-rh966778.patch
Patch143: glibc-rh863384.patch
Patch144: glibc-rh629823.patch
Patch145: glibc-rh629823-2.patch
Patch146: glibc-rh947882.patch
Patch147: glibc-rh905874.patch
Patch148: glibc-rh929302.patch
Patch150: glibc-rh928318.patch
Patch151: glibc-rh905575.patch
Patch152: glibc-rh988931.patch
Patch153: glibc-rh970090.patch
Patch154: glibc-rh1008310.patch
Patch155: glibc-rh1022022.patch
Patch156: glibc-rh1043557.patch
Patch157: glibc-rh1039988.patch
Patch158: glibc-rh995972.patch
Patch159: glibc-rh981942.patch
Patch160: glibc-rh1032628.patch
Patch161: glibc-rh1027101.patch
Patch162: glibc-rh1025933.patch
Patch163: glibc-rh845218.patch
Patch164: glibc-rh1044628.patch
Patch165: glibc-rh1085273.patch
Patch166: glibc-rh1074342.patch
Patch167: glibc-rh1085289.patch
Patch168: glibc-rh1082379.patch
Patch169: glibc-rh1074353.patch
Patch170: glibc-rh1019916.patch
Patch171: glibc-rh1028285.patch
Patch172: glibc-rh1099025.patch
Patch173: glibc-rh1087833.patch
Patch174: glibc-rh1027261.patch
Patch175: glibc-rh905941.patch
Patch176: glibc-rh1054846.patch
Patch177: glibc-rh1111460.patch
Patch178: glibc-rh1099025-2.patch
Patch179: glibc-rh1133810-1.patch
Patch180: glibc-rh1133810-2.patch
Patch181: glibc-rh1138769.patch
Patch182: glibc-rh1171296.patch
Patch183: glibc-rh1172044.patch
Patch184: glibc-rh1154563.patch
Patch185: glibc-rh1125307.patch
Patch186: glibc-rh1176907.patch
Patch187: glibc-rh1183534.patch
Patch188: glibc-rh1159167.patch
Patch189: glibc-rh1023306.patch
Patch190: glibc-rh1085312.patch
Patch191: glibc-rh1091915.patch
Patch192: glibc-rh859965.patch
Patch193: glibc-rh1124204.patch
Patch194: glibc-rh978098.patch
Patch195: glibc-rh1144019.patch
Patch196: glibc-rh1053178.patch
Patch197: glibc-rh1144132.patch
Patch198: glibc-rh1116050.patch
Patch199: glibc-rh1116050-1.patch
Patch200: glibc-rh867679.patch
Patch201: glibc-rh1088301.patch
Patch202: glibc-rh1195453-avx512.patch
Patch203: glibc-rh1066724.patch
Patch204: glibc-rh1209376.patch
Patch205: glibc-rh1207236.patch
Patch206: glibc-rh1217186.patch
Patch207: glibc-rh1245731.patch
Patch208: glibc-rh1245731-2.patch
Patch209: glibc-rh1245731-3.patch
Patch210: glibc-rh1245731-4.patch
Patch211: glibc-rh1246656.patch
Patch212: glibc-rh1246660.patch
Patch213: glibc-rh1264189.patch
Patch214: glibc-rh1244585.patch
Patch215: glibc-rh1211098.patch
Patch216: glibc-rh1192621.patch
Patch217: glibc-rh1091334.patch
Patch218: glibc-rh1211748.patch
Patch219: glibc-rh1011900.patch
Patch220: glibc-rh1186104.patch
Patch221: glibc-rh1198802.patch
Patch222: glibc-rh1275384.patch
Patch223: glibc-rh1020263.patch
Patch224: glibc-rh1200555.patch
Patch225: glibc-rh1293464.patch
Patch226: glibc-rh1280058.patch
Patch227: glibc-rh1296031.patch
Patch228: glibc-rh1296031-0.patch
Patch229: glibc-rh1299319-0.patch
Patch230: glibc-rh1299319-1.patch
Patch231: glibc-rh1223095.patch
Patch232: glibc-rh1358014.patch
Patch233: glibc-rh1373646.patch
Patch234: glibc-rh1358011.patch
Patch235: glibc-rh1358013.patch
Patch236: glibc-rh1270950.patch
Patch237: glibc-rh1331304.patch
Patch238: glibc-rh1318380.patch
Patch239: glibc-rh1101858.patch
Patch240: glibc-rh1384281.patch
Patch241: glibc-rh1338673.patch
Patch242: glibc-rh1358015.patch
Patch243: glibc-rh1012343.patch
Patch244: glibc-rh1452717-1.patch
Patch245: glibc-rh1452717-2.patch
Patch246: glibc-rh1452717-3.patch
Patch247: glibc-rh1452717-4.patch
Patch248: glibc-rh1504810-1.patch
Patch249: glibc-rh1504810-2.patch

Buildroot: %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: %{?scl_prefix}glibc-profile < 2.4
#Provides: %{?scl_prefix}ldconfig
Provides: ldconfig
# The dynamic linker supports DT_GNU_HASH
#Provides: %{?scl_prefix}rtld(GNU_HASH)
Provides: rtld(GNU_HASH)
Requires: %{?scl_prefix}glibc-common = %{version}-%{release}
# Require libgcc in case some program calls pthread_cancel in its %%post
#Requires(pre): %{?scl_prefix}basesystem, %{?scl_prefix}libgcc
Requires(pre): basesystem, libgcc
# This is for building auxiliary programs like memusage, nscd
# For initial glibc bootstraps it can be commented out
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
#BuildRequires: %{?scl_prefix}gd-devel %{?scl_prefix}libpng-devel %{?scl_prefix}zlib-devel %{?scl_prefix}texinfo, %{?scl_prefix}libselinux-devel >= 1.33.4-3
BuildRequires: gd-devel libpng-devel zlib-devel texinfo, libselinux-devel >= 1.33.4-3
#BuildRequires: %{?scl_prefix}audit-libs-devel >= 1.1.3, %{?scl_prefix}sed >= 3.95, %{?scl_prefix}libcap-devel, %{?scl_prefix}gettext, %{?scl_prefix}nss-devel
BuildRequires: audit-libs-devel >= 1.1.3, sed >= 3.95, libcap-devel, gettext, nss-devel
BuildRequires: /bin/ps, /bin/kill, /bin/awk
%ifarch %{systemtaparches}
#BuildRequires: %{?scl_prefix}systemtap-sdt-devel
BuildRequires: systemtap-sdt-devel
%endif
# This is to ensure that __frame_state_for is exported by glibc
# will be compatible with egcs 1.x.y
#BuildRequires: %{?scl_prefix}gcc >= 3.2
BuildRequires: gcc >= 3.2
%define enablekernel 2.6.18
%ifarch i386
%define nptl_target_cpu i486
%else
%define nptl_target_cpu %{_target_cpu}
%endif
%ifarch %{multiarcharches}
# Need STT_IFUNC support
%ifarch ppc ppc64
BuildRequires: %{?scl_prefix}binutils >= 2.20.51.0.2
Conflicts: %{?scl_prefix}binutils < 2.20.51.0.2
%else
BuildRequires: %{?scl_prefix}binutils >= 2.19.51.0.10
Conflicts: %{?scl_prefix}binutils < 2.19.51.0.10
%endif
# Earlier releases have broken support for IRELATIVE relocations
#Conflicts: %{?scl_prefix}prelink < 0.4.2
Conflicts: prelink < 0.4.2
%else
# Need AS_NEEDED directive
# Need --hash-style=* support
BuildRequires: %{?scl_prefix}binutils >= 2.17.50.0.2-5
%endif
#BuildRequires: %{?scl_prefix}gcc >= 3.2.1-5
BuildRequires: gcc >= 3.2.1-5
%ifarch ppc s390 s390x
#BuildRequires: %{?scl_prefix}gcc >= 4.1.0-0.17
BuildRequires: gcc >= 4.1.0-0.17
%endif
%if 0%{?_enable_debug_packages}
#BuildRequires: %{?scl_prefix}elfutils >= 0.72
BuildRequires: elfutils >= 0.72
#BuildRequires: %{?scl_prefix}rpm >= 4.2-0.56
BuildRequires: rpm >= 4.2-0.56
%endif
%define __find_provides %{_builddir}/%{glibcsrcdir}/find_provides.sh
%define _filter_GLIBC_PRIVATE 1


%description
The glibc package contains standard libraries which are used by
multiple programs on the system. In order to save disk space and
memory, as well as to make upgrading easier, common system code is
kept in one place and shared between programs. This particular package
contains the most important sets of shared libraries: the standard C
library and the standard math library. Without these two libraries, a
Linux system will not function.

%if %{xenpackage}

%package xen
Summary: The GNU libc libraries (optimized for running under Xen)
Group: System Environment/Libraries
Requires: %{?scl_prefix}glibc = %{version}-%{release}, %{?scl_prefix}glibc-utils = %{version}-%{release}


%description xen
The standard glibc package is optimized for native kernels and does not
perform as well under the Xen hypervisor.  This package provides alternative
library binaries that will be selected instead when running under Xen.

Install glibc-xen if you might run your system under the Xen hypervisor.
%endif


%package devel
Summary: Object files for development using standard C libraries.
Group: Development/Libraries
Requires(pre): /sbin/install-info
Requires(pre): %{?scl_prefix}%{pkg_name}-headers
Requires: %{?scl_prefix}%{pkg_name}-headers = %{version}-%{release}
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}


%description devel
The glibc-devel package contains the object files necessary
for developing programs which use the standard C libraries (which are
used by nearly all programs).  If you are developing programs which
will use the standard C libraries, your system needs to have these
standard object files available in order to create the
executables.

Install glibc-devel if you are going to develop programs which will
use the standard C libraries.


%package static
Summary: C library static libraries for -static linking.
Group: Development/Libraries
Requires: %{?scl_prefix}%{pkg_name}-devel = %{version}-%{release}


%description static
The glibc-static package contains the C library static libraries
for -static linking.  You don't need these, unless you link statically,
which is highly discouraged.


%package headers
Summary: Header files for development using standard C libraries.
Group: Development/Libraries
Provides: %{?scl_prefix}%{pkg_name}-headers(%{_target_cpu})
%ifarch x86_64
# If both -m32 and -m64 is to be supported on AMD64, x86_64 glibc-headers
# have to be installed, not i586 ones.
#Obsoletes: %{?scl_prefix}%{pkg_name}-headers(i586)
#Obsoletes: %{?scl_prefix}%{pkg_name}-headers(i686)
%endif
#Requires(pre): %{?scl_prefix}kernel-headers
Requires(pre): kernel-headers
#Requires: %{?scl_prefix}kernel-headers >= 2.2.1, %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires: kernel-headers >= 2.2.1, %{?scl_prefix}%{pkg_name} = %{version}-%{release}
#BuildRequires: %{?scl_prefix}kernel-headers >= 2.6.22
BuildRequires: kernel-headers >= 2.6.22


%description headers
The glibc-headers package contains the header files necessary
for developing programs which use the standard C libraries (which are
used by nearly all programs).  If you are developing programs which
will use the standard C libraries, your system needs to have these
standard header files available in order to create the
executables.

Install glibc-headers if you are going to develop programs which will
use the standard C libraries.


%package common
Summary: Common binaries and locale data for glibc
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
#Requires: %{?scl_prefix}tzdata >= 2015g-4
Requires: tzdata >= 2015g-4
Group: System Environment/Base


%description common
The glibc-common package includes common binaries for the GNU libc
libraries, as well as national language (locale) support.


%package -n %{?scl_prefix}nscd
Summary: A Name Service Caching Daemon (nscd).
Group: System Environment/Daemons
#Requires: %{?scl_prefix}libselinux >= 1.17.10-1, %{?scl_prefix}audit-libs >= 1.1.3
Requires: libselinux >= 1.17.10-1, audit-libs >= 1.1.3
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires(pre): /sbin/chkconfig, /usr/sbin/useradd, /usr/sbin/userdel, sh-utils


%description -n %{?scl_prefix}nscd
Nscd caches name service lookups and can dramatically improve
performance with NIS+, and may help with DNS as well.


%package utils
Summary: Development utilities from GNU C library
Group: Development/Tools
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}


%description utils
The glibc-utils package contains memusage, a memory usage profiler,
mtrace, a memory leak tracer and xtrace, a function call tracer
which can be helpful during program debugging.

If unsure if you need this, don't install this package.

%if 0%{?_enable_debug_packages}
%define debug_package %{nil}
%define __debug_install_post %{nil}
%global __debug_package 1


%package debuginfo
Summary: Debug information for package %{pkg_name}
Group: Development/Debug
AutoReqProv: no
%ifarch %{debuginfocommonarches}
Requires: %{?scl_prefix}glibc-debuginfo-common = %{version}-%{release}
%else
%ifarch %{ix86}
Obsoletes: %{?scl_prefix}glibc-debuginfo-common
%endif
%endif


%description debuginfo
This package provides debug information for package %{pkg_name}.
Debug information is useful when developing applications that use this
package or when debugging this package.

This package also contains static standard C libraries with
debugging information.  You need this only if you want to step into
C library routines during debugging programs statically linked against
one or more of the standard C libraries.
To use this debugging information, you need to link binaries
with -static -L%{_prefix}/lib/debug%{_prefix}/%{_lib} compiler options.

%ifarch %{debuginfocommonarches}


%package debuginfo-common
Summary: Debug information for package %{pkg_name}
Group: Development/Debug
AutoReqProv: no


%description debuginfo-common
This package provides debug information for package %{pkg_name}.
Debug information is useful when developing applications that use this
package or when debugging this package.

%endif
%endif


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -q -n %{glibcsrcdir} -b1
%patch0 -E -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch228 -p1
%patch229 -p1
%patch230 -p1
%patch231 -p1
%patch232 -p1
%patch233 -p1
%patch234 -p1
%patch235 -p1
%patch236 -p1
%patch237 -p1
%patch238 -p1
%patch239 -p1
%patch240 -p1
%patch241 -p1
%patch242 -p1
%patch243 -p1
%patch244 -p1
%patch245 -p1
%patch246 -p1
%patch247 -p1
%patch248 -p1
%patch249 -p1

# A lot of programs still misuse memcpy when they have to use
# memmove. The memcpy implementation below is not tolerant at
# all.
rm -f sysdeps/alpha/alphaev6/memcpy.S
%if %{buildpower6}
# On powerpc32, hp timing is only available in power4/power6
# libs, not in base, so pre-power4 dynamic linker is incompatible
# with power6 libs.
rm -f sysdeps/powerpc/powerpc32/power4/hp-timing.[ch]
%endif

find . -type f -size 0 -o -name "*.orig" -exec rm -f {} \;
cat > find_provides.sh <<EOF
#!/bin/sh
/usr/lib/rpm/find-provides | grep -v GLIBC_PRIVATE
exit 0
EOF
chmod +x find_provides.sh
touch `find . -name configure`
touch locale/programs/*-kw.h
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# Log system information
uname -a
cat /proc/cpuinfo
cat /proc/meminfo
df || true

GCC=gcc
GXX=g++
%ifarch %{ix86}
BuildFlags="-march=%{nptl_target_cpu} -mtune=generic"
%endif
%ifarch i686
BuildFlags="-march=i686 -mtune=generic"
%endif
%ifarch i386 i486 i586
BuildFlags="$BuildFlags -mno-tls-direct-seg-refs"
%endif
%ifarch x86_64
BuildFlags="-mtune=generic"
%endif
%ifarch alphaev6
BuildFlags="-mcpu=ev6"
%endif
%ifarch sparc
BuildFlags="-fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparcv9
BuildFlags="-mcpu=ultrasparc -fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparcv9v
BuildFlags="-mcpu=niagara -fcall-used-g6"
GCC="gcc -m32"
GXX="g++ -m32"
%endif
%ifarch sparc64
BuildFlags="-mcpu=ultrasparc -mvis -fcall-used-g6"
GCC="gcc -m64"
GXX="g++ -m64"
%endif
%ifarch sparc64v
BuildFlags="-mcpu=niagara -mvis -fcall-used-g6"
GCC="gcc -m64"
GXX="g++ -m64"
%endif
%ifarch ppc64
BuildFlags="-mno-minimal-toc"
GCC="gcc -m64"
GXX="g++ -m64"
%endif

BuildFlags="$BuildFlags -fasynchronous-unwind-tables"
# Add -DNDEBUG unless using a prerelease
case %{version} in
  *.*.9[0-9]*) ;;
  *)
     BuildFlags="$BuildFlags -DNDEBUG"
     ;;
esac
EnableKernel="--enable-kernel=%{enablekernel}"
echo "$GCC" > Gcc
AddOns=`echo */configure | sed -e 's!/configure!!g;s!\(linuxthreads\|nptl\|rtkaio\|powerpc-cpu\)\( \|$\)!!g;s! \+$!!;s! !,!g;s!^!,!;/^,\*$/d'`
%ifarch %{rtkaioarches}
AddOns=,rtkaio$AddOns
%endif

build_nptl()
{
builddir=build-%{nptl_target_cpu}-$1
shift
rm -rf $builddir
mkdir $builddir ; cd $builddir
build_CFLAGS="$BuildFlags -g -O3 $*"
../configure CC="$GCC" CXX="$GXX" CFLAGS="$build_CFLAGS" \
	--prefix=%{_prefix} \
	--enable-add-ons=nptl$AddOns --without-cvs $EnableKernel \
	--with-headers=%{_prefix}/include --enable-bind-now \
	--with-tls --with-__thread --build %{nptl_target_cpu}-redhat-linux \
	--host %{nptl_target_cpu}-redhat-linux \
%ifarch %{multiarcharches}
	--enable-multi-arch \
%endif
%ifarch %{systemtaparches}
	--enable-systemtap \
%endif
	--disable-profile --enable-experimental-malloc --enable-nss-crypt

make %{?_smp_mflags} -r CFLAGS="$build_CFLAGS"

cd ..
}

build_nptl linuxnptl

%if %{buildxen}
build_nptl linuxnptl-nosegneg -mno-tls-direct-seg-refs
%endif

%if %{buildpower6}
(
platform=`LD_SHOW_AUXV=1 /bin/true | sed -n 's/^AT_PLATFORM:[[:blank:]]*//p'`
if [ "$platform" != power6 ]; then
  mkdir -p power6emul/{lib,lib64}
  $GCC -shared -O2 -fpic -o power6emul/%{_lib}/power6emul.so releng/power6emul.c -Wl,-z,initfirst
%ifarch ppc
  gcc -shared -nostdlib -O2 -fpic -m64 -o power6emul/lib64/power6emul.so -xc - </dev/null
%endif
%ifarch ppc64
  gcc -shared -nostdlib -O2 -fpic -m32 -o power6emul/lib/power6emul.so -xc - < /dev/null
%endif
  export LD_PRELOAD=`pwd`/power6emul/\$LIB/power6emul.so
fi
AddOns="$AddOns --with-cpu=power6"
GCC="$GCC -mcpu=power6"
GXX="$GXX -mcpu=power6"
build_nptl linuxnptl-power6
)
%endif

cd build-%{nptl_target_cpu}-linuxnptl
$GCC -static -L. -Os -g ../releng/glibc_post_upgrade.c -o glibc_post_upgrade.%{_target_cpu} \
  -DNO_SIZE_OPTIMIZATION \
%ifarch i386 i486 i586
  -DARCH_386 \
%endif
  '-DLIBTLS="/%{_lib}/tls/"' \
  '-DGCONV_MODULES_DIR="%{_prefix}/%{_lib}/gconv"' \
  '-DLD_SO_CONF="/etc/ld.so.conf"' \
  '-DICONVCONFIG="%{_sbindir}/iconvconfig.%{_target_cpu}"'
cd ..
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
GCC=`cat Gcc`

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make -j1 install_root=$RPM_BUILD_ROOT install -C build-%{nptl_target_cpu}-linuxnptl
chmod +x $RPM_BUILD_ROOT%{_prefix}/libexec/pt_chown
%ifnarch %{auxarches}
cd build-%{nptl_target_cpu}-linuxnptl && \
  make %{?_smp_mflags} install_root=$RPM_BUILD_ROOT install-locales -C ../localedata objdir=`pwd` && \
  cd ..
%endif

librtso=`basename $RPM_BUILD_ROOT/%{_lib}/librt.so.*`

%ifarch %{rtkaioarches}
rm -f $RPM_BUILD_ROOT{,%{_prefix}}/%{_lib}/librtkaio.*
rm -f $RPM_BUILD_ROOT%{_prefix}/%{_lib}/librt.so.*
mkdir -p $RPM_BUILD_ROOT/%{_lib}/rtkaio
mv $RPM_BUILD_ROOT/%{_lib}/librtkaio-*.so $RPM_BUILD_ROOT/%{_lib}/rtkaio/
rm -f $RPM_BUILD_ROOT/%{_lib}/$librtso
ln -sf `basename $RPM_BUILD_ROOT/%{_lib}/librt-*.so` $RPM_BUILD_ROOT/%{_lib}/$librtso
ln -sf `basename $RPM_BUILD_ROOT/%{_lib}/rtkaio/librtkaio-*.so` $RPM_BUILD_ROOT/%{_lib}/rtkaio/$librtso
%endif

%if %{buildxen}
%define nosegneg_subdir_base i686
%define nosegneg_subdir i686/nosegneg
%define nosegneg_subdir_up ../..
cd build-%{nptl_target_cpu}-linuxnptl-nosegneg
destdir=$RPM_BUILD_ROOT/%{_lib}/%{nosegneg_subdir}
mkdir -p $destdir
for lib in libc math/libm nptl/libpthread rt/librt nptl_db/libthread_db
do
  libbase=${lib#*/}
  libbaseso=$(basename $RPM_BUILD_ROOT/%{_lib}/${libbase}-*.so)
  # Only install if different from base lib
  if cmp -s ${lib}.so ../build-%{nptl_target_cpu}-linuxnptl/${lib}.so; then
    ln -sf %{nosegneg_subdir_up}/$libbaseso $destdir/$libbaseso
  else
    cp -a ${lib}.so $destdir/$libbaseso
  fi
  ln -sf $libbaseso $destdir/$(basename $RPM_BUILD_ROOT/%{_lib}/${libbase}.so.*)
done
%ifarch %{rtkaioarches}
destdir=$RPM_BUILD_ROOT/%{_lib}/rtkaio/%{nosegneg_subdir}
mkdir -p $destdir
librtkaioso=$(basename $RPM_BUILD_ROOT/%{_lib}/librt-*.so | sed s/librt-/librtkaio-/)
if cmp -s rtkaio/librtkaio.so ../build-%{nptl_target_cpu}-linuxnptl/rtkaio/librtkaio.so; then
  ln -s %{nosegneg_subdir_up}/$librtkaioso $destdir/$librtkaioso
else
  cp -a rtkaio/librtkaio.so $destdir/$librtkaioso
fi
ln -sf $librtkaioso $destdir/$librtso
%endif
cd ..
%endif

%if %{buildpower6}
cd build-%{nptl_target_cpu}-linuxnptl-power6
destdir=$RPM_BUILD_ROOT/%{_lib}/power6
mkdir -p ${destdir}
for lib in libc math/libm nptl/libpthread rt/librt nptl_db/libthread_db
do
  libbase=${lib#*/}
  libbaseso=$(basename $RPM_BUILD_ROOT/%{_lib}/${libbase}-*.so)
  cp -a ${lib}.so $destdir/$libbaseso
  ln -sf $libbaseso $destdir/$(basename $RPM_BUILD_ROOT/%{_lib}/${libbase}.so.*)
done
mkdir -p ${destdir}x
pushd ${destdir}x
ln -sf ../power6/*.so .
cp -a ../power6/*.so.* .
popd
%ifarch %{rtkaioarches}
destdir=$RPM_BUILD_ROOT/%{_lib}/rtkaio/power6
mkdir -p $destdir
librtkaioso=$(basename $RPM_BUILD_ROOT/%{_lib}/librt-*.so | sed s/librt-/librtkaio-/)
cp -a rtkaio/librtkaio.so $destdir/$librtkaioso
ln -sf $librtkaioso $destdir/$librtso
mkdir -p ${destdir}x
pushd ${destdir}x
ln -sf ../power6/*.so .
cp -a ../power6/*.so.* .
popd
%endif
cd ..
%endif

# Remove the files we don't want to distribute
rm -f $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libNoVersion*
rm -f $RPM_BUILD_ROOT/%{_lib}/libNoVersion*

# NPTL <bits/stdio-lock.h> is not usable outside of glibc, so include
# the generic one (#162634)
cp -a bits/stdio-lock.h $RPM_BUILD_ROOT%{_prefix}/include/bits/stdio-lock.h
# And <bits/libc-lock.h> needs sanitizing as well.
cp -a releng/libc-lock.h $RPM_BUILD_ROOT%{_prefix}/include/bits/libc-lock.h

if [ -d $RPM_BUILD_ROOT%{_prefix}/info -a "%{_infodir}" != "%{_prefix}/info" ]; then
  mkdir -p $RPM_BUILD_ROOT%{_infodir}
  mv -f $RPM_BUILD_ROOT%{_prefix}/info/* $RPM_BUILD_ROOT%{_infodir}
  rm -rf $RPM_BUILD_ROOT%{_prefix}/info
fi

gzip -9nvf $RPM_BUILD_ROOT%{_infodir}/libc*

ln -sf libbsd-compat.a $RPM_BUILD_ROOT%{_prefix}/%{_lib}/libbsd.a

install -p -m 644 releng/nsswitch.conf $RPM_BUILD_ROOT/etc/nsswitch.conf

mkdir -p $RPM_BUILD_ROOT/etc/default
install -p -m 644 nis/nss $RPM_BUILD_ROOT/etc/default/nss

# This is for ncsd - in glibc 2.2
install -m 644 nscd/nscd.conf $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 nscd/nscd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/nscd

# Don't include ld.so.cache
rm -f $RPM_BUILD_ROOT/etc/ld.so.cache

# Include ld.so.conf
echo 'include ld.so.conf.d/*.conf' > $RPM_BUILD_ROOT/etc/ld.so.conf
> $RPM_BUILD_ROOT/etc/ld.so.cache
chmod 644 $RPM_BUILD_ROOT/etc/ld.so.conf
mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
> $RPM_BUILD_ROOT/etc/sysconfig/nscd
> $RPM_BUILD_ROOT/etc/gai.conf

# Include %{_prefix}/%{_lib}/gconv/gconv-modules.cache
> $RPM_BUILD_ROOT%{_prefix}/%{_lib}/gconv/gconv-modules.cache
chmod 644 $RPM_BUILD_ROOT%{_prefix}/%{_lib}/gconv/gconv-modules.cache

# Install the upgrade program
install -m 700 build-%{nptl_target_cpu}-linuxnptl/glibc_post_upgrade.%{_target_cpu} \
  $RPM_BUILD_ROOT/usr/sbin/glibc_post_upgrade.%{_target_cpu}

strip -g $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.o

%if 0%{?_enable_debug_packages}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/debug%{_prefix}/%{_lib}
cp -a $RPM_BUILD_ROOT%{_prefix}/%{_lib}/*.a \
  $RPM_BUILD_ROOT%{_prefix}/lib/debug%{_prefix}/%{_lib}/
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/debug%{_prefix}/%{_lib}/*_p.a
%endif

# rquota.x and rquota.h are now provided by quota
rm -f $RPM_BUILD_ROOT%{_prefix}/include/rpcsvc/rquota.[hx]

# Create archive of locale files
%ifnarch %{auxarches}
olddir=`pwd`
pushd ${RPM_BUILD_ROOT}%{_prefix}/lib/locale
rm locale-archive || :
# Intentionally we do not pass --alias-file=, aliases will be added
# by build-locale-archive.
$olddir/build-%{nptl_target_cpu}-linuxnptl/elf/ld.so \
  --library-path $olddir/build-%{nptl_target_cpu}-linuxnptl/ \
  $olddir/build-%{nptl_target_cpu}-linuxnptl/locale/localedef \
    --prefix ${RPM_BUILD_ROOT} --add-to-archive \
    *_*
rm -rf *_*
mv locale-archive{,.tmpl}
popd
%endif

rm -f ${RPM_BUILD_ROOT}/%{_lib}/libnss1-*
rm -f ${RPM_BUILD_ROOT}/%{_lib}/libnss-*.so.1

# Ugly hack for buggy rpm
ln -f ${RPM_BUILD_ROOT}%{_sbindir}/iconvconfig{,.%{_target_cpu}}

# In F7+ this is provided by rpcbind rpm
rm -f $RPM_BUILD_ROOT%{_sbindir}/rpcinfo

# BUILD THE FILE LIST
{
  find $RPM_BUILD_ROOT \( -type f -o -type l \) \
       \( \
	 -name etc -printf "%%%%config " -o \
	 -name gconv-modules \
	 -printf "%%%%verify(not md5 size mtime) %%%%config(noreplace) " -o \
	 -name gconv-modules.cache \
	 -printf "%%%%verify(not md5 size mtime) " \
	 , \
	 ! -path "*/lib/debug/*" -printf "/%%P\n" \)
  find $RPM_BUILD_ROOT -type d \
       \( -path '*%{_prefix}/share/*' ! -path '*%{_infodir}' -o \
	  -path "*%{_prefix}/include/*" \
       \) -printf "%%%%dir /%%P\n"
} | {

  # primary filelist
  SHARE_LANG='s|.*/share/locale/\([^/_]\+\).*/LC_MESSAGES/.*\.mo|%lang(\1) &|'
  LIB_LANG='s|.*/lib/locale/\([^/_]\+\)|%lang(\1) &|'
  # rpm does not handle %lang() tagged files hardlinked together accross
  # languages very well, temporarily disable
  LIB_LANG=''
  sed -e "$LIB_LANG" -e "$SHARE_LANG" \
      -e '\,/etc/\(localtime\|gai\.conf\|nsswitch.conf\|ld\.so\.conf\|ld\.so\.cache\|default\),d' \
      -e '\,/%{_lib}/lib\(pcprofile\|memusage\)\.so,d' \
      -e '\,bin/\(memusage\|mtrace\|xtrace\|pcprofiledump\),d'
} | sort > rpm.filelist

mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{_lib}
mv -f $RPM_BUILD_ROOT/%{_lib}/lib{pcprofile,memusage}.so $RPM_BUILD_ROOT%{_prefix}/%{_lib}
for i in $RPM_BUILD_ROOT%{_prefix}/bin/{xtrace,memusage}; do
  sed -e 's~=/%{_lib}/libpcprofile.so~=%{_prefix}/%{_lib}/libpcprofile.so~' \
      -e 's~=/%{_lib}/libmemusage.so~=%{_prefix}/%{_lib}/libmemusage.so~' \
      -e 's~='\''/\\\$LIB/libpcprofile.so~='\''%{_prefix}/\\$LIB/libpcprofile.so~' \
      -e 's~='\''/\\\$LIB/libmemusage.so~='\''%{_prefix}/\\$LIB/libmemusage.so~' \
      -i $i
done

grep '%{_infodir}' < rpm.filelist | grep -v '%{_infodir}/dir' > devel.filelist
grep '%{_prefix}/include/gnu/stubs-[32164]\+\.h' < rpm.filelist >> devel.filelist || :

grep '%{_prefix}/include' < rpm.filelist |
  egrep -v '%{_prefix}/include/(linuxthreads|gnu/stubs-[32164]+\.h)' \
	> headers.filelist

sed -i -e '\|%{_prefix}/%{_lib}/lib.*_p.a|d' \
       -e '\|%{_prefix}/include|d' \
       -e '\|%{_infodir}|d' rpm.filelist

grep '%{_prefix}/%{_lib}/lib.*\.a' < rpm.filelist \
  | grep '/lib\(\(c\|pthread\|nldbl\)_nonshared\|bsd\(\|-compat\)\|g\|ieee\|mcheck\|rpcsvc\)\.a$' \
  >> devel.filelist
grep '%{_prefix}/%{_lib}/lib.*\.a' < rpm.filelist \
  | grep -v '/lib\(\(c\|pthread\|nldbl\)_nonshared\|bsd\(\|-compat\)\|g\|ieee\|mcheck\|rpcsvc\)\.a$' \
  > static.filelist
grep '%{_prefix}/%{_lib}/.*\.o' < rpm.filelist >> devel.filelist
grep '%{_prefix}/%{_lib}/lib.*\.so' < rpm.filelist >> devel.filelist

sed -i -e '\|%{_prefix}/%{_lib}/lib.*\.a|d' \
       -e '\|%{_prefix}/%{_lib}/.*\.o|d' \
       -e '\|%{_prefix}/%{_lib}/lib.*\.so|d' \
       -e '\|%{_prefix}/%{_lib}/linuxthreads|d' \
       -e '\|nscd|d' rpm.filelist

grep '%{_prefix}/bin' < rpm.filelist >> common.filelist
#grep '%{_prefix}/lib/locale' < rpm.filelist | grep -v /locale-archive.tmpl >> common.filelist
#grep '%{_prefix}/libexec/pt_chown' < rpm.filelist >> common.filelist
grep '%{_prefix}/sbin/[^gi]' < rpm.filelist >> common.filelist
grep '%{_prefix}/share' < rpm.filelist | \
  grep -v -e '%{_prefix}/share/zoneinfo' -e '%%dir %{prefix}/share' \
       >> common.filelist

sed -i -e '\|%{_prefix}/bin|d' \
       -e '\|%{_prefix}/lib/locale|d' \
       -e '\|%{_prefix}/libexec/pt_chown|d' \
       -e '\|%{_prefix}/sbin/[^gi]|d' \
       -e '\|%{_prefix}/share|d' rpm.filelist

> nosegneg.filelist
%if %{xenpackage}
grep '/%{_lib}/%{nosegneg_subdir}' < rpm.filelist >> nosegneg.filelist
sed -i -e '\|/%{_lib}/%{nosegneg_subdir}|d' rpm.filelist
%endif

echo '%{_prefix}/sbin/build-locale-archive' >> common.filelist
echo '%{_prefix}/sbin/nscd' > nscd.filelist

cat >> rpm.filelist <<EOF
%{_prefix}/%{_lib}/libmemusage.so
%{_prefix}/%{_lib}/libpcprofile.so
EOF

cat > utils.filelist <<EOF
%{_prefix}/bin/memusage
%{_prefix}/bin/memusagestat
%{_prefix}/bin/mtrace
%{_prefix}/bin/pcprofiledump
%{_prefix}/bin/xtrace
EOF

rm -rf $RPM_BUILD_ROOT%{_prefix}/share/zoneinfo

# Make sure %config files have the same timestamp
touch -r releng/glibc.spec.in $RPM_BUILD_ROOT/etc/ld.so.conf
touch -r sunrpc/etc.rpc $RPM_BUILD_ROOT/etc/rpc

cd releng
$GCC -Os -g -static -o build-locale-archive build-locale-archive.c \
  ../build-%{nptl_target_cpu}-linuxnptl/locale/locarchive.o \
  ../build-%{nptl_target_cpu}-linuxnptl/locale/md5.o \
  -DDATADIR=\"%{_datadir}\" -DPREFIX=\"%{_prefix}\" \
  -L../build-%{nptl_target_cpu}-linuxnptl
install -m 700 build-locale-archive $RPM_BUILD_ROOT/usr/sbin/build-locale-archive
cd ..

# the last bit: more documentation
rm -rf documentation
mkdir documentation
cp crypt/README.ufc-crypt documentation/README.ufc-crypt
cp timezone/README documentation/README.timezone
cp ChangeLog{,.15,.16} documentation
bzip2 -9 documentation/ChangeLog*
cp posix/gai.conf documentation/

%ifarch s390x
# Compatibility symlink
mkdir -p $RPM_BUILD_ROOT/lib
ln -sf /%{_lib}/ld64.so.1 $RPM_BUILD_ROOT/lib/ld64.so.1
%endif

%if %{run_glibc_tests}

PLTCMD='/^Relocation section .*\(\.rela\?\.plt\|\.rela\.IA_64\.pltoff\)/,/^$/p'
echo ====================PLT RELOCS LD.SO================
readelf -Wr $RPM_BUILD_ROOT/%{_lib}/ld-*.so | sed -n -e "$PLTCMD"
echo ====================PLT RELOCS LIBC.SO==============
readelf -Wr $RPM_BUILD_ROOT/%{_lib}/libc-*.so | sed -n -e "$PLTCMD"
echo ====================PLT RELOCS END==================

%endif

pushd $RPM_BUILD_ROOT/usr/%{_lib}/
$GCC -r -nostdlib -o libpthread.o -Wl,--whole-archive ./libpthread.a
rm libpthread.a
ar rcs libpthread.a libpthread.o
rm libpthread.o
popd

%if 0%{?_enable_debug_packages}

# The #line directives gperf generates do not give the proper
# file name relative to the build directory.
(cd locale; ln -s programs/*.gperf .)
(cd iconv; ln -s ../locale/programs/charmap-kw.gperf .)

ls -l $RPM_BUILD_ROOT/usr/bin/getconf
ls -l $RPM_BUILD_ROOT/usr/libexec/getconf
eu-readelf -hS $RPM_BUILD_ROOT/usr/bin/getconf $RPM_BUILD_ROOT/usr/libexec/getconf/*

find_debuginfo_args='--strict-build-id -g'
%ifarch %{debuginfocommonarches}
echo %{_prefix}/libexec/pt_chown > workaround.filelist
find_debuginfo_args="$find_debuginfo_args \
  -l common.filelist -l utils.filelist -l nscd.filelist -l workaround.filelist \
  -p '.*/(sbin|libexec)/.*' \
  -o debuginfocommon.filelist \
  -l rpm.filelist -l nosegneg.filelist \
"
%endif
eval /usr/lib/rpm/find-debuginfo.sh "$find_debuginfo_args" -o debuginfo.filelist

list_debug_archives()
{
  local dir=%{_prefix}/lib/debug%{_prefix}/%{_lib}
  find $RPM_BUILD_ROOT$dir -name "*.a" -printf "$dir/%%P\n"
}

%ifarch %{debuginfocommonarches}

sed -i '\#^%{_prefix}/src/debug/#d' debuginfocommon.filelist
find $RPM_BUILD_ROOT%{_prefix}/src/debug \
     \( -type d -printf '%%%%dir ' \) , \
     -printf '%{_prefix}/src/debug/%%P\n' > debuginfocommon.sources

%ifarch %{biarcharches}

cat debuginfocommon.sources >> debuginfo.filelist

%else

%ifarch %{ix86}
%define basearch i686
%endif
%ifarch alpha alphaev6
%define basearch alpha
%endif
%ifarch sparc sparcv9
%define basearch sparc
%endif

# auxarches get only these few source files
auxarches_debugsources=\
'/(generic|linux|%{basearch}|nptl(_db)?)/|/%{glibcsrcdir}/build|/dl-osinfo\.h'

egrep "$auxarches_debugsources" debuginfocommon.sources >> debuginfo.filelist

egrep -v "$auxarches_debugsources" \
  debuginfocommon.sources >> debuginfocommon.filelist
%ifnarch %{auxarches}
# non-aux arches when there is a debuginfo-common
# all the sources go into debuginfo-common
#cat debuginfocommon.sources >> debuginfocommon.filelist
%endif

%endif

list_debug_archives >> debuginfocommon.filelist

%else

# already found by find-debuginfo
#list_debug_archives >> debuginfo.filelist

%endif

%endif

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%ifarch %{auxarches}

echo Cutting down the list of unpackaged files
>> debuginfocommon.filelist
sed -e '/%%dir/d;/%%config/d;/%%verify/d;s/%%lang([^)]*) //;s#^/*##' \
    common.filelist devel.filelist static.filelist headers.filelist \
    utils.filelist nscd.filelist debuginfocommon.filelist |
(cd $RPM_BUILD_ROOT; xargs --no-run-if-empty rm -f 2> /dev/null || :)

%else

mkdir -p $RPM_BUILD_ROOT/var/{db,run}/nscd
touch $RPM_BUILD_ROOT/var/{db,run}/nscd/{passwd,group,hosts,services}
touch $RPM_BUILD_ROOT/var/run/nscd/{socket,nscd.pid}
%endif

%ifnarch %{auxarches}
> $RPM_BUILD_ROOT/%{_prefix}/lib/locale/locale-archive
%endif

mkdir -p $RPM_BUILD_ROOT/var/cache/ldconfig
> $RPM_BUILD_ROOT/var/cache/ldconfig/aux-cache
%{?scl:EOF}


#%post -p /usr/sbin/glibc_post_upgrade.%{_target_cpu}
#%{?scl:scl enable %{scl} - << \EOF}
#set -ex
#%{?scl:EOF}


%postun 
%{?scl:scl enable %{scl} - << \EOF}
set -ex
/sbin/ldconfig
%{?scl:EOF}


%post common
%{?scl:scl enable %{scl} - << \EOF}
set -ex
/usr/sbin/build-locale-archive
%{?scl:EOF}


%post devel
%{?scl:scl enable %{scl} - << \EOF}
set -ex
/sbin/install-info %{_infodir}/libc.info.gz %{_infodir}/dir > /dev/null 2>&1 || :
%{?scl:EOF}


%pre headers
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# this used to be a link and it is causing nightmares now
if [ -L %{_prefix}/include/scsi ] ; then
  rm -f %{_prefix}/include/scsi
fi
%{?scl:EOF}


%preun devel
%{?scl:scl enable %{scl} - << \EOF}
set -ex
if [ "$1" = 0 ]; then
  /sbin/install-info --delete %{_infodir}/libc.info.gz %{_infodir}/dir > /dev/null 2>&1 || :
fi
%{?scl:EOF}


%post utils
%{?scl:scl enable %{scl} - << \EOF}
set -ex
/sbin/ldconfig
%{?scl:EOF}


%postun utils
%{?scl:scl enable %{scl} - << \EOF}
set -ex
/sbin/ldconfig
%{?scl:EOF}


%pre -n %{?scl_prefix}nscd
%{?scl:scl enable %{scl} - << \EOF}
set -ex
getent group nscd >/dev/null || /usr/sbin/groupadd -g 28 -r nscd
getent passwd nscd >/dev/null ||
  /usr/sbin/useradd -M -o -r -d / -s /sbin/nologin \
		    -c "NSCD Daemon" -u 28 -g nscd nscd
%{?scl:EOF}


%post -n %{?scl_prefix}nscd
%{?scl:scl enable %{scl} - << \EOF}
set -ex
/sbin/chkconfig --add nscd
%{?scl:EOF}


%preun -n %{?scl_prefix}nscd
%{?scl:scl enable %{scl} - << \EOF}
set -ex
if [ $1 = 0 ] ; then
  service nscd stop > /dev/null 2>&1
  /sbin/chkconfig --del nscd
fi
%{?scl:EOF}


%postun -n %{?scl_prefix}nscd
%{?scl:scl enable %{scl} - << \EOF}
set -ex
if [ $1 = 0 ] ; then
  /usr/sbin/userdel nscd > /dev/null 2>&1 || :
fi
if [ "$1" -ge "1" ]; then
  service nscd condrestart > /dev/null 2>&1 || :
fi
%{?scl:EOF}


%if %{xenpackage}
%post xen
set -ex
/sbin/ldconfig
%{?scl:EOF}


%postun xen
%{?scl:scl enable %{scl} - << \EOF}
set -ex
/sbin/ldconfig
%{?scl:EOF}
%endif


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf "$RPM_BUILD_ROOT"
rm -f *.filelist*
%{?scl:EOF}


%files -f rpm.filelist
%defattr(-,root,root)
%ifarch %{rtkaioarches}
%dir /%{_lib}/rtkaio
%endif
%if %{buildxen} && !%{xenpackage}
%dir /%{_lib}/%{nosegneg_subdir_base}
%dir /%{_lib}/%{nosegneg_subdir}
%ifarch %{rtkaioarches}
%dir /%{_lib}/rtkaio/%{nosegneg_subdir_base}
%dir /%{_lib}/rtkaio/%{nosegneg_subdir}
%endif
%endif
%if %{buildpower6}
%dir /%{_lib}/power6
%dir /%{_lib}/power6x
%ifarch %{rtkaioarches}
%dir /%{_lib}/rtkaio/power6
%dir /%{_lib}/rtkaio/power6x
%endif
%endif
%ifarch s390x
/lib/ld64.so.1
%endif
%verify(not md5 size mtime) %config(noreplace) /etc/rpc
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/localtime
%verify(not md5 size mtime) %config(noreplace) /etc/nsswitch.conf
%verify(not md5 size mtime) %config(noreplace) /etc/ld.so.conf
%dir /etc/ld.so.conf.d
%dir %{_prefix}/libexec/getconf
%dir %{_prefix}/%{_lib}/gconv
%dir %attr(0700,root,root) /var/cache/ldconfig
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/cache/ldconfig/aux-cache
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/ld.so.cache
%doc README NEWS INSTALL FAQ BUGS NOTES PROJECTS CONFORMANCE
%doc COPYING COPYING.LIB README.libm LICENSES
%doc hesiod/README.hesiod
%attr(0644,root,root) %verify(not md5 size mtime) %config(missingok,noreplace) /etc/gai.conf

%if %{xenpackage}

%files -f nosegneg.filelist xen
%defattr(-,root,root)
%dir /%{_lib}/%{nosegneg_subdir_base}
%dir /%{_lib}/%{nosegneg_subdir}
%endif

%ifnarch %{auxarches}

%files -f common.filelist common
%defattr(-,root,root)
%attr(0644,root,root) %verify(not md5 size mtime) %{_prefix}/lib/locale/locale-archive.tmpl
%attr(0644,root,root) %verify(not md5 size mtime mode) %ghost %config(missingok,noreplace) %{_prefix}/lib/locale/locale-archive
%dir %attr(755,root,root) /etc/default
%verify(not md5 size mtime) %config(noreplace) /etc/default/nss
%attr(4711,root,root) %{_prefix}/libexec/pt_chown
%doc documentation/*


%files -f devel.filelist devel
%defattr(-,root,root)


%files -f static.filelist static
%defattr(-,root,root)


%files -f headers.filelist headers
%defattr(-,root,root)


%files -f utils.filelist utils
%defattr(-,root,root)


%files -f nscd.filelist -n nscd
%defattr(-,root,root)
%config(noreplace) /etc/nscd.conf
%config /etc/rc.d/init.d/nscd
%dir %attr(0755,root,root) /var/run/nscd
%dir %attr(0755,root,root) /var/db/nscd
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/nscd.pid
%attr(0666,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/socket
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/passwd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/group
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/hosts
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/run/nscd/services
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/db/nscd/passwd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/db/nscd/group
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/db/nscd/hosts
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/db/nscd/services
%ghost %config(missingok,noreplace) /etc/sysconfig/nscd
%endif

%if 0%{?_enable_debug_packages}

%files debuginfo -f debuginfo.filelist
%defattr(-,root,root)
%ifarch %{debuginfocommonarches}
%ifnarch %{auxarches}

%files debuginfo-common -f debuginfocommon.filelist
%defattr(-,root,root)
%endif
%endif
%endif


%changelog
* Fri Nov 17 2017 Patsy Franklin <pfrankli@redhat.com> - 2.12-1.212
- CVE-2017-15670: glob: Fix one-byte overflow with GLOB_TILDE (#1504810)
- CVE-2017-15804: glob: Fix buffer overflow in GLOB_TILDE unescaping (#1504810)
