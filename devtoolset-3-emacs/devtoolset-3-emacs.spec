%{?scl:%scl_package emacs}
%{!?scl:%global pkg_name emacs}

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


# This file is encoded in UTF-8.  -*- coding: utf-8 -*-

Summary: GNU Emacs text editor
Name: devtoolset-3-emacs
Epoch: 1
Version: 23.1
Release: 31%{?dist}
License: GPLv3+
URL: http://www.gnu.org/software/emacs/
Group: Applications/Editors
Source0: ftp://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.bz2
Source1: emacs.desktop
Source3: dotemacs.el
Source4: site-start.el
Source7: http://php-mode.svn.sourceforge.net/svnroot/php-mode/tags/php-mode-1.4.0/php-mode.el
Source8: php-mode-init.el
Source9: ssl.el
# rpm-spec-mode from XEmacs
Source10: rpm-spec-mode.el
Source11: rpm-spec-mode-init.el
Source13: focus-init.el
Source14: po-mode.el
Source15: po-mode-init.el
Source18: default.el
Patch0: glibc-open-macro.patch
Patch1: rpm-spec-mode.patch
Patch2: po-mode-auto-replace-date-71264.patch
Patch3: rpm-spec-mode-utc.patch
Patch4: emacs-gtk.patch
Patch5: emacs-23.1-xdg.patch
Patch6: emacs-23.1-cpp.patch
Patch7: emacs-23.1-scroll.patch
Patch8: emacs-23.1-indian.patch
# Fixed in upstream CVS
Patch9: emacs-23.1-memmove.patch
# Taken from upstream GIT repository
# http://git.savannah.gnu.org/cgit/emacs.git/diff/src/xsettings.c?id=b3a25b88e82569f916712c635207c8bdd590e13b
# rhbz#517272
Patch10: emacs-23.1-fontdpi.patch
# http://debbugs.gnu.org/cgi/bugreport.cgi?bug=4129
Patch11: emacs-23.1-spacing.patch
# Size already changed in upstream
Patch12: emacs-23.1-defaultfont.patch
Patch13: emacs-23.1-jis2004.patch
Patch14: emacs-23.1-last-tty.patch
Patch15: emacs-spellcheck.patch
Patch16: emacs-font.patch
Patch17: emacs-xrender.patch
Patch18: emacs-23.1-get-glyph-face.patch
Patch19: emacs-23.1-memory-limits.patch

Buildroot: %{_tmppath}/%{pkg_name}-%{version}-root
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
#BuildRequires: %{?scl_prefix}atk-devel, %{?scl_prefix}cairo-devel, %{?scl_prefix}desktop-file-utils, %{?scl_prefix}freetype-devel, %{?scl_prefix}fontconfig-devel, %{?scl_prefix}dbus-devel, %{?scl_prefix}giflib-devel, %{?scl_prefix}glibc-devel, %{?scl_prefix}gtk2-devel, %{?scl_prefix}libpng-devel
BuildRequires: atk-devel, cairo-devel, desktop-file-utils, freetype-devel, fontconfig-devel, dbus-devel, giflib-devel, glibc-devel, gtk2-devel, libpng-devel
#BuildRequires: %{?scl_prefix}libjpeg-devel, %{?scl_prefix}libtiff-devel, %{?scl_prefix}libX11-devel, %{?scl_prefix}libXau-devel, %{?scl_prefix}libXdmcp-devel, %{?scl_prefix}libXrender-devel, %{?scl_prefix}libXt-devel
BuildRequires: libjpeg-devel, libtiff-devel, libX11-devel, libXau-devel, libXdmcp-devel, libXrender-devel, libXt-devel
#BuildRequires: %{?scl_prefix}libXpm-devel, %{?scl_prefix}ncurses-devel, %{?scl_prefix}xorg-x11-proto-devel, %{?scl_prefix}zlib-devel
BuildRequires: libXpm-devel, ncurses-devel, xorg-x11-proto-devel, zlib-devel
#BuildRequires: %{?scl_prefix}autoconf, %{?scl_prefix}automake, %{?scl_prefix}bzip2, %{?scl_prefix}cairo, %{?scl_prefix}texinfo
BuildRequires: %{?scl_prefix}autoconf, %{?scl_prefix}automake, bzip2, cairo, texinfo
%ifarch %{ix86}
#BuildRequires: %{?scl_prefix}setarch
BuildRequires: setarch
%endif
#Requires: %{?scl_prefix}xorg-x11-fonts-ISO8859-1-100dpi, %{?scl_prefix}xorg-x11-fonts-misc
Requires: %{?scl_prefix}emacs-common = %{epoch}:%{version}-%{release}
#Requires: %{?scl_prefix}hicolor-icon-theme
# bz#507852
#BuildRequires: %{?scl_prefix}librsvg2-devel, %{?scl_prefix}m17n-lib-devel, %{?scl_prefix}libotf-devel
BuildRequires: librsvg2-devel, m17n-lib-devel, libotf-devel
#BuildRequires: %{?scl_prefix}alsa-lib-devel
BuildRequires: alsa-lib-devel
#Requires: %{?scl_prefix}librsvg2
Requires: librsvg2
# Desktop integration
#BuildRequires: %{?scl_prefix}desktop-file-utils
BuildRequires: desktop-file-utils
#Requires:      %{?scl_prefix}desktop-file-utils
Requires:      desktop-file-utils
#Conflicts: %{?scl_prefix}gettext < 0.10.40
Conflicts: gettext < 0.10.40
Provides: %{?scl_prefix}emacs(bin)
#Requires: %{?scl_prefix}m17n-db-datafiles
Requires: m17n-db-datafiles

# C and build patches

# Lisp and doc patches

%define paranoid 1
%define expurgate 1

%define site_lisp %{_datadir}/emacs/site-lisp
%define site_start_d %{site_lisp}/site-start.d
%define bytecompargs -batch --no-init-file --no-site-file -f batch-byte-compile
%define pkgconfig %{_datadir}/pkgconfig


%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package provides an emacs binary with support for X windows.


%package nox
Summary: GNU Emacs text editor without X support
Group: Applications/Editors
Requires: %{?scl_prefix}emacs-common = %{epoch}:%{version}-%{release}
Provides: %{?scl_prefix}emacs(bin)


%description nox
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package provides an emacs binary with no X windows support for running
on a terminal.


%package common
Summary: Emacs common files
Group: Applications/Editors
#Requires(preun): %{?scl_prefix}%{_sbindir}/alternatives, %{?_scl_root}/sbin/install-info, %{?scl_prefix}dev
Requires(preun): chkconfig, texinfo, dev
#Requires(posttrans): chkconfig
Requires(posttrans): chkconfig

Requires(post): texinfo, dev
Obsoletes: %{?scl_prefix}emacs-leim


%description common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package contains all the common files needed by emacs or emacs-nox.


%package el
Summary: Emacs Lisp source files included with Emacs.
Group: Applications/Editors


%description el
Emacs-el contains the emacs-elisp sources for many of the elisp
programs included with the main Emacs text editor package.

You need to install emacs-el only if you intend to modify any of the
Emacs packages or see some elisp examples.

%define emacs_libexecdir %{_libexecdir}/emacs/%{version}/%{_host}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1 -b .glibc-open-macro
%patch4 -p1 -b .gtk
%patch5 -p1 -b .xdg
%patch6 -p1
%patch7 -p1 -b .scroll
%patch8 -p1
%patch9 -p1 -b .memmove
%patch10 -p1 -b .fontdpi
%patch11 -p1 -b .spacing
%patch12 -p1 -b .defaultfont
%patch13 -p1 -b .jis2004
%patch14 -p1 -b .last-tty
%patch15 -p1 -b .spellcheck
%patch16 -p1 -b .font
%patch17 -p1 -b .xrender
%patch18 -p1 -b .glyph-face
%patch19 -p1 -b .memory-limits

# install rest of site-lisp files
( cd site-lisp
  cp %SOURCE7 %SOURCE9 %SOURCE10 %SOURCE14 .
  # rpm-spec-mode can use compilation-mode
  patch < %PATCH1
  # fix po-auto-replace-revision-date nil
  patch < %PATCH2
  # rpm-spec-mode: added rpm-change-log-uses-utc variable
  patch < %PATCH3
  )

# we prefer our emacs.desktop file
cp %SOURCE1 etc/emacs.desktop

grep -v "tetris.elc" lisp/Makefile.in > lisp/Makefile.in.new \
   && mv lisp/Makefile.in.new lisp/Makefile.in

# avoid trademark issues
%if %{paranoid}
rm -f lisp/play/tetris.el lisp/play/tetris.elc
%endif

%if %{expurgate}
rm -f etc/sex.6 etc/condom.1 etc/celibacy.1 etc/COOKIES etc/future-bug etc/JOKES
%endif

%define info_files ada-mode auth autotype calc ccmode cl dbus dired-x ebrowse ediff efaq eintr elisp emacs emacs-mime epa erc eshell eudc flymake forms gnus idlwave info mairix-el message mh-e newsticker nxml-mode org pcl-cvs pgg rcirc reftex remember sasl sc ses sieve smtpmail speedbar tramp url vip viper widget woman

if test "$(perl -e 'while (<>) { if (/^INFO_FILES/) { s/.*=//; while (s/\\$//) { s/\\//; $_ .= <>; }; s/\s+/ /g; s/^ //; s/ $//; print; exit; } }' Makefile.in)" != "%info_files"; then
  echo Please update info_files >&2
  exit 1
fi

%ifarch %{ix86}
%define setarch setarch %{_arch} -R
%else
%define setarch %{nil}
%endif
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# Remove an unpatched file as all files in the textmodes directory are
# installed.
rm lisp/textmodes/ispell.el.spellcheck

export CFLAGS="-DMAIL_USE_LOCKF $RPM_OPT_FLAGS"

#we patch configure.in so we have to do this
autoconf
%configure --with-dbus --with-gif --with-jpeg --with-png --with-rsvg \
   --with-tiff --with-xft --with-xpm --with-x-toolkit=gtk

%__make bootstrap
%{setarch} %__make %{?_smp_mflags}

# remove versioned file so that we end up with .1 suffix and only one DOC file
rm src/emacs-%{version}.*

# make sure patched lisp files get byte-compiled
TOPDIR=${PWD}
${TOPDIR}/src/emacs %{bytecompargs} site-lisp/*.el

%__make %{?_smp_mflags} -C lisp updates

rm etc/emacs3.py

# Create pkgconfig file
cat > emacs.pc << EOG
sitepkglispdir=%{site_lisp}
sitestartdir=%{site_start_d}

Name: emacs
Description: GNU Emacs text editor
Version: %{epoch}:%{version}
EOG

# Create macros.emacs RPM macro file
cat > macros.emacs << EOH
%%_emacs_version %{version}
%%_emacs_ev %{?epoch:%{epoch}:}%{version}
%%_emacs_evr %{?epoch:%{epoch}:}%{version}-%{release}
%%_emacs_sitelispdir %{site_lisp}
%%_emacs_sitestartdir %{site_start_d}
%%_emacs_bytecompile /usr/bin/emacs %bytecompargs 
EOH
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf %{buildroot}

make install INSTALL="%{__install} -p" DESTDIR=%{buildroot}

# let alternatives manage the symlink
rm %{buildroot}%{_bindir}/emacs

# rebuild without X support
# remove the versioned binary with X support so that we end up with .1 suffix for emacs-nox too
rm src/emacs-%{version}.*
%configure --without-x
%__make %{?_smp_mflags}

# install the emacs without X
install -p -m 0755 src/emacs-%{version}.1 %{buildroot}%{_bindir}/emacs-%{version}-nox

# make sure movemail isn't setgid
chmod 755 %{buildroot}%{emacs_libexecdir}/movemail

mkdir -p %{buildroot}%{site_lisp}
install -p -m 0644 %SOURCE4 %{buildroot}%{site_lisp}/site-start.el
install -p -m 0644 %SOURCE18 %{buildroot}%{site_lisp}

mv %{buildroot}%{_bindir}/{etags,etags.emacs}
mv %{buildroot}%{_mandir}/man1/{ctags.1,gctags.1}
mv %{buildroot}%{_mandir}/man1/{etags.1,etags.emacs.1}
mv %{buildroot}%{_bindir}/{ctags,gctags}

# install site-lisp files
install -p -m 0644 site-lisp/*.el{,c} %{buildroot}%{site_lisp}

mkdir -p %{buildroot}%{site_lisp}/site-start.d
install -p -m 0644 %SOURCE8 %SOURCE11 %SOURCE13 %SOURCE15 %{buildroot}%{site_lisp}/site-start.d

# default initialization file
mkdir -p %{buildroot}%{_sysconfdir}/skel
install -p -m 0644 %SOURCE3 %{buildroot}%{_sysconfdir}/skel/.emacs

# install pkgconfig file
mkdir -p %{buildroot}/%{pkgconfig}
install -p -m 0644 emacs.pc %{buildroot}/%{pkgconfig}

# install rpm macro definition file
mkdir -p %{buildroot}%{_sysconfdir}/rpm
install -p -m 0644 macros.emacs %{buildroot}%{_sysconfdir}/rpm/

# after everything is installed, remove info dir
rm -f %{buildroot}%{_infodir}/dir
rm %{buildroot}%{_localstatedir}/games/emacs/*

# install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %SOURCE1


#
# create file lists
#
rm -f *-filelist {common,el}-*-files

( TOPDIR=${PWD}
  cd %{buildroot}

  find .%{_datadir}/emacs/%{version}/lisp \
    .%{_datadir}/emacs/%{version}/leim \
    .%{_datadir}/emacs/site-lisp \( -type f -name '*.elc' -fprint $TOPDIR/common-lisp-none-elc-files \) -o \( -type d -fprintf $TOPDIR/common-lisp-dir-files "%%%%dir %%p\n" \) -o \( -name '*.el.gz' -fprint $TOPDIR/el-bytecomped-files -o -fprint $TOPDIR/common-not-comped-files \)

)

# put the lists together after filtering  ./usr to /usr
sed -i -e "s|\.%{_prefix}|%{_prefix}|" *-files
cat common-*-files > common-filelist
cat el-*-files common-lisp-dir-files > el-filelist
%{?scl:EOF}


%clean
%{?scl:scl enable %{scl} - << \EOF}
set -ex
rm -rf %{buildroot}
%{?scl:EOF}


%post
%{?scl:scl enable %{scl} - << \EOF}
set -ex
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
%{?scl:EOF}


%postun
%{?scl:scl enable %{scl} - << \EOF}
set -ex
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
%{?scl:EOF}


%preun
%{?scl:scl enable %{scl} - << \EOF}
set -ex
alternatives --remove emacs %{_bindir}/emacs-%{version} || :
%{?scl:EOF}


%posttrans
%{?scl:scl enable %{scl} - << \EOF}
set -ex
#check if there is "remainder" old version, which was not deleted
if alternatives --display emacs > /dev/null; then
VER=$(alternatives --display emacs | sed -ne 's/.*emacs-\([0-9\.]\+\).*/\1/p' | head -1)
if [ ${VER} != %{version} ]; then
alternatives --remove emacs %{_bindir}/emacs-${VER} || :
fi
fi
#end check
alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-%{version} 80 || :
%{?scl:EOF}


%preun nox
%{?scl:scl enable %{scl} - << \EOF}
set -ex
alternatives --remove emacs %{_bindir}/emacs-%{version}-nox || :
%{?scl:EOF}


%posttrans nox
%{?scl:scl enable %{scl} - << \EOF}
set -ex
#check if there is "remainder" old version, which was not deleted
if alternatives --display emacs > /dev/null; then
VER=$(alternatives --display emacs | sed -ne 's/.*emacs-\([0-9\.]\+\).*/\1/p' | head -1)
if [ ${VER} != %{version} ]; then
alternatives --remove emacs %{_bindir}/emacs-${VER}-nox || :
fi
fi
#end check
alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-%{version}-nox 70 || :
%{?scl:EOF}


%post common
%{?scl:scl enable %{scl} - << \EOF}
set -ex
for f in %{info_files}; do
  /sbin/install-info %{_infodir}/$f %{_infodir}/dir 2> /dev/null || :
done
%{?scl:EOF}


%preun common
%{?scl:scl enable %{scl} - << \EOF}
set -ex
alternatives --remove emacs.etags %{_bindir}/etags.emacs || :
if [ "$1" = 0 ]; then
  for f in %{info_files}; do
    /sbin/install-info --delete %{_infodir}/$f %{_infodir}/dir 2> /dev/null || :
  done
fi
%{?scl:EOF}


%posttrans common
%{?scl:scl enable %{scl} - << \EOF}
set -ex
alternatives --install %{_bindir}/etags emacs.etags %{_bindir}/etags.emacs 80 \
       --slave %{_mandir}/man1/etags.1.gz emacs.etags.man %{_mandir}/man1/etags.emacs.1.gz
%{?scl:EOF}


%files
%defattr(-,root,root)
%{_bindir}/emacs-%{version}
%dir %{_libexecdir}/emacs
%dir %{_libexecdir}/emacs/%{version}
%dir %{emacs_libexecdir}
%{_datadir}/applications/emacs.desktop
%{_datadir}/icons/hicolor/*/apps/emacs.png
%{_datadir}/icons/hicolor/*/apps/emacs22.png
%{_datadir}/icons/hicolor/scalable/apps/emacs.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document.svg



%files nox
%defattr(-,root,root)
%{_bindir}/emacs-%{version}-nox
%dir %{_libexecdir}/emacs
%dir %{_libexecdir}/emacs/%{version}
%dir %{emacs_libexecdir}


%files -f common-filelist common
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/skel/.emacs
%config(noreplace) %{_sysconfdir}/rpm/macros.emacs
%doc etc/NEWS BUGS README
%exclude %{_bindir}/emacs-*
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/%{version}
%{_datadir}/emacs/%{version}/etc
%{_datadir}/emacs/%{version}/site-lisp
%{_libexecdir}/emacs
%attr(0644,root,root) %config(noreplace) %{_datadir}/emacs/site-lisp/default.el
%attr(0644,root,root) %config %{_datadir}/emacs/site-lisp/site-start.el


%files -f el-filelist el
%defattr(-,root,root)
%{pkgconfig}/emacs.pc
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/%{version}


%changelog
* Thu Nov 27 2014 Petr Hracek <phracek@redhat.com> - 1:23.1-28
- Remove etc/emacs3.py script
Related: #852516

* Wed Nov 26 2014 Petr Hracek <phracek@redhat.com> - 1:23.1-27
- Disable memory warnings
Resolves: #852516

* Wed Nov 26 2014 Petr Hracek <phracek@redhat.com> - 1:23.1-26
- Segfault in get_glyph_face_and_encoding
Resolves: #986989

* Tue May 07 2013 Petr Hracek <phracek@redhat.com> - 1:23.1-25
- Lucida Typewriter and Console fonts not selectable
- Resolves: #678225

* Mon Feb 27 2012 Karel Klíč <kklic@redhat.com> - 1:23.1-24
- Remove an unpatched file as all files in the textmodes directory are installed
  Related: #713600

* Tue Feb 21 2012 Karel Klíč <kklic@redhat.com> - 1:23.1-23
- Use hunspell as default ispell program
  Resolves: #713600

* Wed Dec 21 2011 Karel Klíč <kklic@redhat.com> - 1:23.1-22
- Remove check for last terminal
  Resolves: #732157

* Wed Feb  2 2011 Karel Klic <kklic@redhat.com> 1:23.1-21
- Added jis2004 patch to prefer non-JIS X 0213:2004 compliant fonts
  for Japanese texts (IPA fonts are counted as JIS X 0213:2004
  compliant)
  Resolves: #612385
- Removed dependency on aspell and hunspell
  Resolves: #613759

* Mon Jun 21 2010 Karel Klic <kklic@redhat.com> 1:23.1-20
- Changed default font size from 12pt to 10pt
  Resolves: #595899

* Mon Jun 21 2010 Karel Klic <kklic@redhat.com> 1:23.1-19
- Fixed handling of dual spacing fonts
  Resolves: #592408

* Fri Feb 26 2010 Karel Klic <kklic@redhat.com> 1:23.1-18
- Expurgate Emacs on RHEL
- Remove a macro in ChangeLog

* Tue Jan 12 2010 Karel Klic <kklic@redhat.com> 1:23.1-17
- Removed invalid URL for rpm-spec-mode.el. This mode in
  this version is no longer found on the Internet

* Thu Jan 07 2010 Karel Klic <kklic@redhat.com> 1:23.1-16
- Removed PreReq from spec file
- Fixed rhbz#517272 - emacs-23.1 update shows fonts in double the normal size

* Tue Dec  8 2009 Karel Klic <kklic@redhat.com> 1:23.1-15
- Fixed rhbz#545398 - ETags messes up filenames

* Thu Dec 03 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-14
- fix #542657 -  emacs does not display indic text

* Wed Dec 02 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-13
- fix #543046 -  Using scroll bar in emacs highlights/selects text

* Mon Nov 30 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-12
- fixed FTBFS in F12 and higher (#540921)

* Wed Oct 14 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1:23.1-11
- Bump release to fix tagging problem

* Wed Oct 14 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1:23.1-10
- Update macros.xemacs to treat epoch correctly and be consistent with xemacs package
- Use site_start_d macro consistently
 
* Thu Sep 24 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-9
- use xdg-open(1) for opening URLs (#316131)

* Wed Sep 23 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-8
- updated rpm-spec-mode.el to latest upstream version (#524851)

* Tue Sep 22 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-7
- updated %%info_files (#510750)

* Mon Aug 31 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-6
- fixed buffer menu (#515722)

* Wed Aug 26 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-5
- correct BuildRequires for libotf (#519151)

* Tue Aug 25 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-4
- alsa-lib-devel added to BuildRequires (#518659)

* Thu Aug 13 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-3
- fixed Name and GenericName in desktop file (#514599)

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:23.1-2
- Use bzipped upstream tarball.

* Fri Jul 31 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.1-1
- new upstream version 23.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:23.0.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.0.93-6
- removed dependency to bitmap fonts: emacs version 23 does not need them

* Thu Jun 25 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.0.93-5
- revoked default.el change (#508033)
- added build dependency: librsvg2-devel (#507852)
- added dependency: aspell (#443549) 

* Wed Jun 24 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.0.93-4
- added xorg-x11-fonts-misc to dependencies (#469220)

* Fri Jun 19 2009 Jens Petersen <petersen@redhat.com> - 1:23.0.93-3
- drop igrep since lgrep and rgrep are maintained in emacs now
- specify the list of *-init.el files to be install explicitly

* Thu Jun 11 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.0.93-2
- fix bz#505083 - rpm-add-change-log-entry date format rejected by rpmbuild

* Mon May 18 2009 Daniel Novotny <dnovotny@redhat.com> 1:23.0.93-1
- new upstream version

* Fri Apr 10 2009 Daniel Novotny <dnovotny@redhat.com> 1:22.3-11
- fix bz#443549 -  spell-buffer, flyspell-mode do not work

* Fri Mar 27 2009 Daniel Novotny <dnovotny@redhat.com> 1:22.3-10
- fix segfaults when emacsclient connects to a tcp emacs server (#489066)

* Thu Mar 12 2009 Daniel Novotny <dnovotny@redhat.com> 1:22.3-9
- implement UTC change log option in rpm-spec-mode.el (#489829)

* Wed Mar  4 2009 Michel Salim <salimma@fedoraproject.org> - 1:22.3-8
- Use desktop-file-utils to handle desktop file
- Update icon cache if GTK2 is installed

* Wed Feb 25 2009 Daniel Novotny <dnovotny@redhat.com> 1:22.3-7
- site-lisp/default.el is now config(noreplace)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:22.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Daniel Novotny <dnovotny@redhat.com> 1:22.3-5
- fix #474578 - /usr/bin/emacs link not updated on upgrade
  (added a script to scan the alternatives and update them)

* Mon Feb 09 2009 Daniel Novotny <dnovotny@redhat.com> 1:22.3-4
- fix bz#484309 (alternatives error message)

* Sun Jan 18 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1:22.3-3
- Add /etc/rpm/macros.emacs file

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:22.3-2
- Rebuild for Python 2.6

* Sat Nov  8 2008 Jens Petersen <petersen@redhat.com> - 1:22.3-1
- update to 22.3 (#461448)
- emacs-22.1.50-sparc64.patch and emacs-22.1.50-regex.patch no longer needed
- update rpm-spec-mode.el to look for fields at bol (#466407)

* Thu May 01 2008 Tom "spot" Callaway <tcallawa@redhat.com>
- fix requires to include epoch

* Thu May 01 2008 Dennis Gilmore <dennis@ausil.us> 1:22.2-4
- add patch from bz#435767

* Thu May 01 2008 Dennis Gilmore <dennis@ausil.us> 1:22.2-3
- add epoch
- put epoch in .pc file

* Thu Apr 24 2008 Dennis Gilmore <dennis@ausil.us> 22.2-2
- add patch fixing libdir on sparc64

* Tue Apr 22 2008 Chip Coldwell <coldwell@redhat.com> 22.2-1
- revert back to emacs-22.2 (bz443639)
- update to php-mode-1.4.0
- update to rpm-spec-mode.el v0.12.1x (bz432209)
- patch rpm-spec-mode to use compilation mode (bz227418)
- fix the Release tag (bz440624)
- drop superfluous configure options
- move the new icons into the right destination directory
- the heuristics for detecting address space randomization in the emacs dumper
  seem insufficient, so bring back setarch -R

* Fri Apr 18 2008 Chip Coldwell <coldwell@redhat.com> 23.0.60-2
- New upstream tarball (fixes bz435767)
- configure tweaks
- drop files.el patch (now upstream)
- drop parallel build patch (now upstream)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 22.1.50-4
- Autorebuild for GCC 4.3

* Wed Jan  2 2008 Chip Coldwell <coldwell@redhat.com> 22.1.50-3.1
- parallel build patch from Dan Nicolaescu <dann@ics.uci.edu>

* Fri Dec  7 2007 Chip Coldwell <coldwell@redhat.com> 22.1.50-3
- scriptlets shouldn't fail needlessly.
- new upstream tarball

* Thu Dec  6 2007 Chip Coldwell <coldwell@redhat.com> 22.1.50-2
- drop -DSYSTEM_PURESIZE_EXTRA=16777216 (bz409581)

* Mon Nov 19 2007 Chip Coldwell <coldwell@redhat.com> 22.1.50-1
- pulled sources from GNU CVS

* Mon Nov 19 2007 Chip Coldwell <coldwell@redhat.com> 22.1-9
- fixup alternatives mess (bz239745, bz246540)

* Tue Nov  6 2007 Chip Coldwell <coldwell@redhat.com> 22.1-8
- fix insufficient safe-mode checks (Resolves: bz367601)

* Thu Nov  1 2007 Chip Coldwell <coldwell@redhat.com> 22.1-7
- Update rpm-spec-mode to the current upstream, drop compat patch (bz306841)

* Wed Oct 24 2007 Jeremy Katz <katzj@redhat.com> - 22.1-6
- Update rpm-spec-mode to the current upstream (#306841)

* Wed Sep 12 2007 Chip Coldwell <coldwell@redhat.com> - 22.1-5
- require xorg-x11-fonts-ISO8859-1-100dpi instead of 75dpi (Resolves: bz281861)
- drop broken python mode (Resolves: bz262801)

* Mon Sep 10 2007 Chip Coldwell <coldwell@redhat.com> - 22.1-4
- fix pkgconfig path (from pkg-config to pkgconfig (Jonathan Underwood)
- use macro instead of variable style for buildroot.

* Tue Aug 28 2007 Chip Coldwell <coldwell@redhat.com> - 22.1-3
- change group from Development to Utility

* Mon Aug 13 2007 Chip Coldwell <coldwell@redhat.com> - 22.1-2
- add pkgconfig file for emacs-common and virtual provides (Resolves: bz242176)
- glibc-open-macro.patch to deal with glibc turning "open" into a macro.
- leave emacs info pages in default section (Resolves: bz199008) 

* Wed Jun  6 2007 Chip Coldwell <coldwell@redhat.com> - 22.1-1
- move alternatives install to posttrans scriptlet (Resolves: bz239745)
- new release tarball from FSF (Resolves: bz245303)
- new php-mode 1.2.0

* Wed May 23 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.990-2
- revert all spec file changes since 22.0.95-1 (Resolves: bz239745)
- new pretest tarball from FSF (Resolves: bz238234)
- restore php-mode (Resolves: bz235941)

* Mon May 21 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.990-1
- new pretest tarball from FSF
- removed Ulrich Drepper's patch to prevent mmapped pages during dumping
  removed BuildRequires: glibc >= 2.5.90-22
  (bug traced to glibc Resolves: bz239344)
- fix alternatives removal scriptlet (Resolves: bz239745)

* Thu May 17 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.99-4
- format of freed blocks changed between glibc 2.5.90-21 and 2.5.90-22
- BuildRequires: glibc >= 2.5.90-22 (Ulrich Drepper)

* Sun May 13 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.99-2
- prevent mmapped pages during dumping (Ulrich Drepper Resolves: bz239344)

* Tue Apr 24 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.99-1
- new (last?) pretest tarball from FSF
- update to php-mode-1.2.0 (Ville Skyttä Resolves: bz235941)
- use /etc/alternatives instead of wrapper script

* Tue Mar  6 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.95-1
- new pretest tarball from FSF

* Mon Feb 26 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.94-1
- new pretest tarball obsoletes loaddefs.el dependencies patch

* Fri Feb 23 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.93-7
- fix po-mode-init.el (Kjartan Maraas #228143)

* Tue Feb 13 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.93-6
- remove --without-xim configure flag to fix dead keys (Alexandre Oliva #224626)

* Fri Jan 26 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.93-5
- remove Tetris to avoid trademark problems (Ville Skyttä #224627)

* Thu Jan 25 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.93-4
- fixup loaddefs.el dependencies (Dan Nicolaescu #176171)
- add BuildRequires: automake (changes to Makefile.in)

* Wed Jan 24 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.93-3
- po-mode.el was being left out

* Tue Jan 23 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.93-1
- new pretest version
- removed setarch since new dumper copes with execshield
- clean up site initialization files (varions #176171)

* Tue Jan  2 2007 Chip Coldwell <coldwell@redhat.com> - 22.0.92-1
- new pretest version
- removed almost all emacs 21 patches from emacs 22
- clean up spec file,
- many new BuildRequires (David Woodhouse #221250)

* Tue Nov 14 2006 Chip Coldwell <coldwell@redhat.com> - 22.0.90-1
- first pretest rpm build

* Mon Nov  6 2006 Chip Coldwell <coldwell@redhat.com> - 21.4-19
- BuildRequires: sendmail (Wolfgang Rupprecht #213813)

* Thu Aug  3 2006 Chip Coldwell <coldwell@redhat.com> - 21.4-18
- non-CJK text broken by default for Western locale (James Ralston #144707)

* Thu Aug  3 2006 Chip Coldwell <coldwell@redhat.com> - 21.4-17
- use UTF-8 keyboard input encoding on terminals that support it (Axel Thimm #185399)

* Thu Aug  3 2006 Chip Coldwell <coldwell@redhat.com> - 21.4-16
- fix German spell checking for UTF-8 encoded buffers (Daniel Hammer #197737)

* Wed Jul 26 2006 Chip Coldwell <coldwell@redhat.com> - 21.4-15
- fix src/unexelf.c to build on PowerPC64 (backport from emacs-22, #183304)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 21.4-14.1.1
- rebuild

* Tue Apr 18 2006 Chip Coldwell <coldwell@redhat.com> - 21.4-14.1
- don't clobber site-lisp/default.el (Ritesh Khadgaray, 180153)

* Tue Mar  7 2006 Jens Petersen <petersen@redhat.com> - 21.4-14
- bring back setarch for i386 with -R option in spec file and drop
  emacs-21-personality-linux32-101818.patch since it no longer seems
  sufficient with recent kernels (Sam Peterson, #174736)
- buildrequire giflib-devel instead of libungif-devel

* Thu Mar  2 2006 Jens Petersen <petersen@redhat.com>
- avoid backup for fix-x-vs-no-x-diffs.dpatch (Ian Collier, #183503)
- remove the old ccmode info manual (#182084)

* Mon Feb 27 2006 Jens Petersen <petersen@redhat.com> - 21.4-13
- buildrequire libXaw-devel for menus and scrollbar
- pass -R to setarch to disable address randomization during dumping
  (Sam Peterson, #174736)
- install cc-mode.info correctly (Sam Peterson, #182084)
- fix sort-columns not to use deprecated non-posix sort key syntax
  with sort-columns-posix-key-182282.patch (Richard Ryniker, #182282)
- use system-name function not variable when setting frame-title-format in
  /etc/skel/.emacs for XEmacs users hitting .emacs

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 21.4-12.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 21.4-12.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb  3 2006 Jens Petersen <petersen@redhat.com> - 21.4-12
- add mule-cmd.el-X11-locale.alias-173781.patch to correct location of X11
  locale.alias file (Paul Dickson, #173781)
- fix autoload of php-mode in php-mode-init.el (Christopher Beland, #179484)

* Wed Dec 14 2005 Jens Petersen <petersen@redhat.com> - 21.4-11
- avoid building with -fstack-protector on i386 to prevent crashing
  (Jonathan Kamens, #174730)
- require xorg-x11-fonts-ISO8859-1-75dpi instead of xorg-x11-fonts-75dpi
  for modular X (#174614)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 25 2005 Jens Petersen <petersen@redhat.com> - 21.4-10
- fix missing parenthesis in lang-coding-systems-init.el

* Tue Nov 22 2005 Jens Petersen <petersen@redhat.com> - 21.4-9
- fix keyboard-coding-system on console for utf-8 (Dawid Gajownik, #173855)
- update etags to latest cvs (Hideki Iwamoto, #173023)
  - replace etags-14.21-17.11-diff.patch with etags-update-to-cvs.patch
- update smtpmail.el to latest cvs version for better authentication support
  with smtpmail-cvs-update.patch (Alberto Brizio, #167804)

* Mon Nov 14 2005 Jeremy Katz <katzj@redhat.com> - 21.4-8
- update dep for new xorg fonts packages

* Wed Aug 24 2005 Jens Petersen <petersen@redhat.com>
- fix name of aspell-es dictionary (#147964)
  - update emacs-21.3-lisp-textmodes-ispell-languages.patch

* Thu Jul 14 2005 Jens Petersen <petersen@redhat.com> - 21.4-7
- update rpm-spec-mode.el to cvs revision 1.17 (Ville Skyttä)
  - fixes expansion of %%{?dist}
- replace emacs-21.4-setarch_for_loadup-101818.patch with backport
  emacs-21-personality-linux32-101818.patch from cvs (Jan Djärv)
  which also turns off address randomization during dumping (Masatake Yamato)
  - no longer need to pass SETARCH to make on i386 (#160814)
- move ownership of %%{_datadir}/emacs/ and %%{_datadir}/emacs/%%{version}/
  from emacs to emacs-el and emacs-leim subpackages
- don't build tramp html and dvi documentation
- drop src/config.in part of bzero-and-have-stdlib.dpatch to avoid
  compiler warnings

* Thu Jun 23 2005 Jens Petersen <petersen@redhat.com> - 21.4-6
- merge in changes from emacs22.spec conditionally
  - define emacs21 rpm macro switch to control major version and use it
- update tramp to 2.0.49

* Fri Jun 17 2005 Jens Petersen <petersen@redhat.com>
- set arg0 to emacs in wrapper script (Peter Oliver, 149512#3)

* Mon May 30 2005 Jens Petersen <petersen@redhat.com>
- move setting of require-final-newline from default.el to a comment in default
  .emacs (Ralph Loader, 119141)

* Wed May 18 2005 Jens Petersen <petersen@redhat.com> - 21.4-5
- update cc-mode to 5.30.9 stable release to address font-lock problems
  (126165,148977,150197,155292,158044)

* Mon May 16 2005 Jens Petersen <petersen@redhat.com> - 21.4-4
- don't accidently exclude emacsclient from common package
  (Jonathan Kamens, #157808)
- traditional Chinese desktop file translation (Wei-Lun Chao, #157287)

* Wed Apr 20 2005 Jens Petersen <petersen@redhat.com> - 21.4-3
- add igrep.el and init file

* Mon Apr 11 2005 Jens Petersen <petersen@redhat.com> - 21.4-2
- update etags to 17.11 (idht4n@hotmail.com, 151390)
  - add etags-14.21-17.11-diff.patch
- replace i386 setarch redefinitions of __make and makeinstall with
  emacs-21.4-setarch_for_loadup-101818.patch and setting SETARCH on i386
  (Jason Vas Dias, 101818)

* Sun Apr 10 2005 Jens Petersen <petersen@redhat.com> - 21.4-1
- update to 21.4 movemail vulnerability release
  - no longer need movemail-CAN-2005-0100.patch
- replace %%{_bindir}/emacs alternatives with a wrapper script (Warren Togami)
  to prevent it from disappearing when upgrading (Michal Jaegermann, 154326)
  - suffix the X emacs binaries with -x and the no X binaries with -nox
  - the wrapper script %%{_bindir}/emacs-%%version runs emacs-x if installed or
    otherwise emacs-nox.  %%{_bindir}/emacs is a symlink to the wrapper
- make emacs and emacs-nox own the subdirs in %%{_libexecdir}
- add a bunch of fixes from debian's emacs21_21.4a-1 patch:
    battery-acpi-support.dpatch, bzero-and-have-stdlib.dpatch,
    coding-region-leak.dpatch, detect-coding-iso2022.dpatch,
    fix-batch-mode-signal-handling.dpatch, pcl-cvs-format.dpatch,
    python-completion-ignored-extensions.dpatch,
    remote-files-permissions.dpatch, save-buffer.dpatch, scroll-margin.dpatch,
    xfree86-4.3-modifiers.dpatch
  - add fix-x-vs-no-x-diffs.dpatch
    - define emacs_libexecdir
    - build both emacs and emacs-nox as %%{version}.1 and move common DOC file
      to emacs-common
    - suffix version in fns-%%{version}.1.el with -x and -nox respectively
- add 100 to elisp patches

* Wed Apr  6 2005 Jens Petersen <petersen@redhat.com> - 22.0.50-0.20050406
- update to snapshot of current cvs 
  - configure xim support off by default
  - bootstrap snapshot

* Wed Apr  6 2005 Jens Petersen <petersen@redhat.com> - 21.3-27
- use alternatives to switch _bindir/emacs between emacs and emacs-nox
  (Henning Schmiedehausen, #151067)
  - remove emacs and emacs-nox from bindir
  - prereq alternatives for emacs and emacs-nox
  - add post and postun scripts to handle alternatives
- buildrequire xorg-x11-devel instead of XFree86-devel
- really include and apply emacs-21.3-latex-mode-hook-144083.patch
- make emacs and emacs-nox own _datadir/emacs/version too

* Wed Mar  9 2005 Jens Petersen <petersen@redhat.com> - 21.3-26
- rebuild with gcc 4.0
  - add emacs-21.3-gcc4.patch for emacsclient

* Mon Feb 28 2005 Jens Petersen <petersen@redhat.com> - 21.3-25
- add tramp-2.1.3 to site-lisp (David Woodhouse, 149703)
  - move removal of info dir to after its installation
  - add tramp-init.el to put tramp into load-path

* Thu Feb 24 2005 Jens Petersen <petersen@redhat.com> - 21.3-24
- mark default.el as a noreplace config file (Pawel Salek, 149310)
- only set keyboard-coding-system in xterms to fix problem with input
  Latin characters becoming prefixes and making emacs loop
  (Eddahbi Karim, 126007)
- make emacs-el own its lisp directories
- run latex-mode-hook in latex-mode (Martin Biely, 144083)
  - add emacs-21.3-latex-mode-hook-144083.patch

* Fri Feb 18 2005 Jens Petersen <petersen@redhat.com> - 21.3-23
- install %%{_bindir}/emacs-nox as a hardlink of the versioned binary
- drop explicit lib requirements
- use sed instead of perl to fix up filelists

* Mon Feb 14 2005 Jens Petersen <petersen@redhat.com> - 21.3-22
- use prereq instead of contexts for common script requirements
  (Axel Thimm, 147791)
- move emacs.png from common to main package

* Fri Feb  4 2005 Jens Petersen <petersen@redhat.com> - 21.3-21
- fix CAN-2005-0100 movemail vulnerability with movemail-CAN-2005-0100.patch
  (Max Vozeler, 146701)

* Fri Jan 14 2005 Jens Petersen <petersen@redhat.com> - 21.3-20
- workaround xorg-x11 modifier key problem with
  emacs-21.3-xterm-modifiers-137868.patch (Thomas Woerner, 137868)

* Mon Nov 29 2004 Jens Petersen <petersen@redhat.com> - 21.3-19
- prefer XIM status under-the-window for now to stop xft httx from dying
  (125413): add emacs-xim-status-under-window-125413.patch
- default diff to unified format in .emacs

* Wed Nov 10 2004 Jens Petersen <petersen@redhat.com> - 21.3.50-0.20041111
- initial packaging of cvs emacs
  - leim and elisp manual now in main tarball
  - no leim subpackage anymore, so make common obsolete it
  - no longer need MuleUCS, nor rfc1345.el
  - buildrequire and use autoconf rather autoconf213
  - no longer need emacs-21.2-x86_64.patch,
    editfns.c-Fformat-multibyte-davej.patch
  - bring back game for now
  - TODO: some patches still need updating
  - fns.el no longer installed
  - remove /var/games for now
  - update filelist generation to single sweep
  - update info_files list

* Thu Nov  4 2004 Jens Petersen <petersen@redhat.com> - 21.3-18
- show emacs again in the desktop menu (132567)
- require fonts-xorg-75dpi to prevent empty boxes at startup due to missing
  fonts (Johannes Kaiser, 137060)

* Mon Oct 18 2004 Jens Petersen <petersen@redhat.com> - 21.3-17
- fix etag alternatives removal when uninstalling (Karsten Hopp, 136137)

* Fri Oct 15 2004 Jens Petersen <petersen@redhat.com> - 21.3-16
- do not setup frame-title-format in default.el, since it will override
  setting by users (Henrik Bakken, 134520)
- emacs-el no longer requires emacs for the sake of -nox users
  (Lars Hupfeldt Nielsen, 134479)
- condition calling of global-font-lock-mode in default .emacs
  in case xemacs should happen to load it

* Wed Sep 29 2004 Jens Petersen <petersen@redhat.com> - 21.3-15
- cleanup and update .desktop file
- make emacs not appear in the desktop menu (Seth Nickell,132567)
- move the desktop file from -common to main package
- go back to using just gctags for ctags
- etags is now handled by alternatives (92256)
- improve the default frame title by prefixing the buffer name
  (Christopher Beland, 128110)
- fix the names of some European aspell languages with
  emacs-21.3-lisp-textmodes-ispell-languages.patch (David Jansen, 122618)
- fixing running "libtool gdb program" in gud with
  emacs-21.3-gud-libtool-fix.patch (Dave Malcolm, 130955)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 30 2004 Jens Petersen <petersen@redhat.com> - 21.3-13
- unset focus-follows-mouse in default.el to make switching frames work for
  click-to-focus (Theodore Belding,114736)

* Thu Apr 15 2004 Jens Petersen <petersen@redhat.com> - 21.3-12
- update php-mode to 1.1.0
- add emacs-21.3-no-rpath.patch so that /usr/X11R6/lib is not rpath'ed
- require /bin/ln for %%post (Tim Waugh, 119817)
- move prereq for dev and /sbin/install-info to emacs-common
- leim no longer requires emacs
- use source site-lisp dir in %%prep to setup site files
- define and use site_lisp for buildroot in %%install
- default ispell dictionary to "english" for CJK locale
- add comment to top of site-start.el about load order
- turn on auto-compression-mode in default.el (114808)
- set require-final-newline with setq (David Olsson,119141)
  and remove redundant next-line-add-newlines setting
- update info_file list (Reuben Thomas,114729)

* Tue Mar 16 2004 Mike A. Harris <mharris@redhat.com> 21.3-11
- Removed bogus Requires: XFree86-libs that was added in 21.3-8, as rpm
  find-requires will automatically pick up the dependancies on any runtime
  libraries, and such hard coded requires is not X11 implementation
  agnostic (#118471)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jan 24 2004 Jens Petersen <petersen@redhat.com> - 21.3-9
- bring back emacs-nox subpackage (emacs built without X support) (#113001)
  [suggested by Frank Kruchio]
- base emacs package now only contains emacs binary built with X support
  and no longer obsoletes emacs-nox
- all the common files required by emacs and emacs-nox are now in emacs-common
- update php-mode.el to 1.0.5
- add missing rfc1345.el leim input method
- update po-compat.el to version in gettext-0.13.1
- update base package summary
- add url for python-mode.el and php-mode.el
- gctags is now a symlink to ctags.emacs

* Wed Jan 14 2004 Jens Petersen <petersen@redhat.com> - 21.3-8
- comment out setting transient-mark-mode in skel .emacs (#102441,#90193)
  [reported by mal@gromco.com, Jonathan Kamens]
- improve lang-coding-systems-init.el to set-language-environment for CJK
  utf-8 locale too and use utf-8 for default-coding-systems and
  terminal-coding-system (#111172) [Yoshinori Kuniga]
- update rpm-spec-mode.el to newer one in xemacs package cvs (#105888) [Dams]
- rename etags to etags.emacs and make etags a symlink to it at install time
  if it doesn't exist (#92256) [marc_soft@merlins.org]
- apply editfns.c-Fformat-multibyte-davej.patch to fix multibyte code typo
  in Fformat [patch from Dave Jones]
- add runtime requirements for XFree86-libs, image libraries, ncurses and zlib
- improve -el and -leim package summaries
- no longer configure build with redundant --with-gcc

* Tue Nov 25 2003 Jens Petersen <petersen@redhat.com>
- buildrequire autoconf213 (#110741) [reported by mvd@mylinux.com.ua]

* Mon Oct 27 2003 Jens Petersen <petersen@redhat.com> - 21.3-7
- use "setarch i386" to build on ix86 (#101818) [reported by Michael Redinger]
- use __make to %%build and %%install
- set keyboard coding-system for utf-8 in lang-coding-systems-init.el (#106929)
  [reported with fix by Axel Thimm]
- add source url for MuleUCS
- update base package description (#103551) [reported by Tim Landscheidt]

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May  7 2003 Jens Petersen <petersen@redhat.com> - 21.3-5
- move transient-mark-mode and global-font-lock-mode setting from default.el
  back to dotemacs, so as not to surprise old users (#90193)
  [reported by jik@kamens.brookline.ma.us]
- change require-final-newline to query (default.el)
- don't make a backup when applying browse-url-htmlview-84262.patch (#90226)
  [reported by mitr@volny.cz]

* Fri May  2 2003 Elliot Lee <sopwith@redhat.com>
- Add emacs-21.3-ppc64.patch

* Fri Apr 25 2003 Jens Petersen <petersen@redhat.com> - 21.3-3
- use Mule-UCS utf-8 coding-system for CJK subprocess IO
- no need to set fontset anymore in CJK locale

* Wed Apr 16 2003 Jens Petersen <petersen@redhat.com> - 21.3-2
- add Mule-UCS for CJK utf-8 support (suggested by Akira Tagoh)
  and use it by default in CJK UTF-8 locale
- move emacs-asian startup files into new lang-coding-systems-init.el
- utf-8 setup in site-start.el is no longer needed in Emacs 21.3
- generate filelist for site-lisp automatically like base lisp and leim
- don't setup aspell in site-start.el
- rename dotemacs to dotemacs.el and move former contents to new default.el

* Mon Apr  7 2003 Jens Petersen <petersen@redhat.com> - 21.3-1
- update to 21.3
- no longer set compound-text-with-extensions in dotemacs, since it is now
  the default
- emacs-21.2-pop.patch is no longer needed
- update php-mode to 1.0.4

* Thu Feb 20 2003 Jens Petersen <petersen@redhat.com> - 21.2-33
- default browse-url to use htmlview (#84262)
- remove info dir file rather than excluding it

* Sat Feb  8 2003 Jens Petersen <petersen@redhat.com> - 21.2-32
- set X copy'n'paste encoding to extended compound-text (#74100)
  by default in .emacs file [suggested by olonho@hotmail.com]
- .emacs file cleanup (xemacs now has a separate init file)

* Fri Feb  7 2003 Jens Petersen <petersen@redhat.com> - 21.2-31
- block input in allocate_vectorlike to prevent malloc hangs (#83600)
  [thanks to Jim Blandy]
- set startup wmclass notify in desktop file

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Jens Petersen <petersen@redhat.com> 21.2-29
- update to newer po-mode.el and po-compat.el from gettext-0.11.4
- patch po-mode's po-replace-revision-date for when
  po-auto-replace-revision-date is nil (#71264)
- update po-mode-init.el
- examine LC_ALL before LC_CTYPE in site-start.el for utf-8 (#79535)
- don't install etc/DOC files explicitly by hand
- make sure all lisp .elc files are up to date
- pass _smp_mflags to make
- remove games that we shouldn't ship

* Mon Jan 13 2003 Karsten Hopp <karsten@redhat.de> 21.2-28
- s390x lib64 fix

* Fri Jan  3 2003 Jens Petersen <petersen@redhat.com> 21.2-27
- look at LANG after LC_CTYPE when checking for UTF-8 locale encoding
  in site-start.el (#79535)
- don't set desktop file config(noreplace)

* Fri Dec 20 2002 Jens Petersen <petersen@redhat.com> 21.2-26
- unset the sticky bit of emacs in bindir (#80049)

* Wed Dec 18 2002 Jens Petersen <petersen@redhat.com> 21.2-25
- no need to patch config.{sub,guess}

* Tue Dec  3 2002 Tim Waugh <twaugh@redhat.com>
- Fix python-mode-init.el (bug #78910).

* Sun Dec  1 2002 Jens Petersen <petersen@redhat.com> 21.2-24
- rpm-spec-mode update fixes
  - patch in XEmacs compat functions rather than defining them with apel
    macros in init file (#78764)
  - autoload "rpm-spec-mode" not "rpm-spec-mode.el" in same file
- let emacs base also own leim dir to avoid startup warning about missing dir
  when -el and -leim aren't installed (#78764)

* Thu Nov 28 2002 Jens Petersen <petersen@redhat.com>
- use LC_CTYPE rather than LANG to determine default encoding (#78678)
  [reported by starback@stp.ling.uu.se]

* Wed Nov 27 2002 Jens Petersen <petersen@redhat.com> 21.2-23
- set transient-mark-mode in dotemacs for Emacs not XEmacs (#75440)
- update rpm-spec-mode.el to 0.12
  - define needed XEmacs compat functions in new rpm-spec-mode-init.el
- tidy site-start.el
  - move python-mode setup to python-mode
- don't build with sbin in path
- use _libexecdir, _bindir and _sysconfdir
- don't gzip info files explicitly
- use tar's C and j options
- generate lisp file-lists in single find sweeps over lisp and leim dirs
  - use -fprint and -fprintf
  - correct more dir ownerships

* Sun Nov 24 2002 Florian La Roche <Florian.LaRoche@redhat.de> 21.2-22
- add correct alloca defines for s390

* Wed Nov  6 2002 Jens Petersen <petersen@redhat.com> 21.2-21
- uses patches for x86_64 and s390 support and config.{guess,sub} updating

* Tue Nov  5 2002 Jens Petersen <petersen@redhat.com> 21.2-20
- add support for x86_64 and merge in s390 support from cvs
- add alloca defines to amdx86-64.h (from SuSE)

* Wed Oct 30 2002 Jens Petersen <petersen@redhat.com> 21.2-19
- own our libexec dir (#73984)
- only set transient-mark-mode in dotemacs for Emacs (#75440)
- update to latest config.{guess,sub}
- use _datadir macro

* Wed Aug 28 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-18
- Desktop file fix - add Application to make it show up
- DNS lookup fix for pop (#64802)

* Tue Aug 27 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-17
- Fix gdb arrow when used in non-windowed mode (#56890)

* Fri Aug  9 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-16
- Handle UTF-8 input (#70855).

* Tue Aug  6 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-15
- Don't use canna by default (#70870)

* Thu Aug  1 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-14
- Fixes to desktop file (add encoding, add missing a ";")
- Update s390 patch

* Wed Jul 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-13
- rpm -> rpmbuild for rpmspec mode (#68185)

* Mon Jul 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-12
- desktop file changes (#69385)

* Mon Jul  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-11
- Fix php-mode to not initialize on e.g.  foophp.c (#67592)

* Thu Jun 27 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-10
- Downgrade po-mode

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-8
- #66808

* Wed May 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-7
- Rebuild

* Mon May 20 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-6
- Prereq dev

* Thu May 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-5
- Update the elisp manual and po-mode

* Tue May  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-4
- php-mode 1.0.2

* Thu Apr 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-3
- Update po-mode to the one from gettext 0.11.1

* Mon Apr  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-2
- Tweak mouse init process (#59757)

* Mon Mar 18 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.2-1
- 21.2

* Fri Mar  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.1.95-1
- 21.1.95

* Fri Feb  8 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.1.90-2
- Upgrade po-mode to the version bundled with gettext 0.11
- Upgrade rpm-spec-mode to 0.11h

* Thu Jan 31 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.1.90-1
- 21.1.90

* Fri Jan 18 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.1.80-2
- Add ebrowse
- Set transient-mode to t in /etc/skel/.emacs

* Mon Jan 14 2002 Trond Eivind Glomsrød <teg@redhat.com> 21.1.80-1
- 21.1.80

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Dec  6 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.1-3
- Increase recursive-load-depth-limit from 10 to 50

* Wed Dec  5 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.1-2
- Make it conflict with old versions of gettext

* Thu Nov 29 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.1-1
- rpm-spec-mode 0.11h, should fix #56748

* Tue Nov  6 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.1-0.4
- php mode 1.0.1. Should fix some speedbar problems.

* Tue Oct 23 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.1-0.3
- Minor cleanups
- add ssl.el

* Mon Oct 22 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.1-0.2
- Add more files from the libexec directory (#54874, #54875)

* Sun Oct 21 2001 Trond Eivind Glomsrød <teg@redhat.com> 21.1-0.1
- 21.1
- Build on IA64 again - the default config now handles it
- Drop all old patches
- Misc cleanups
- Update the elisp manual to 21-2.7
- Deprecate the emacs-nox and emacs-X11 subpackages. 
  Simplify build procedure to match. 
- Update php-mode to 1.0.0

* Mon Oct 15 2001 Trond Eivind Glomsrød <teg@redhat.com> 20.7-43
- Add php-mode 0.9.9
- Add URL (#54603)
- don't run autoconf/libtoolize during build - they're broken
- don't build on IA64 until they are fixed

* Sun Sep 16 2001 Trond Eivind Glomsrød <teg@redhat.com> 20.7-42
- Update python-mode to the version in the python 2.2a3
- Include po-mode in emacs, instead of including in gettext

* Mon Jul 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Minor fix to make-mode fontify regexp (#50010)
- Build without emacs being installed (#49085)

* Tue Jun 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Much cleaner site-start.d sourcing
- Add more build dependencies
- Add the emacs lisp reference info pages (RFE #44577)
- Don't require tamago - just plug it in for Japanese support

* Mon Jun 18 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add Xaw3d-devel to buildrequires (#44736)

* Mon Jun 18 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- merged s390x patch from <oliver.paukstadt@millenux.com>

* Mon Jun  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New rpm-spec-mode.el, which fixes #43323

* Thu Apr 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix linker problem on s390 (fix by Than Ngo than@redhat.com)

* Wed Apr 25 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Make sure that mwheel is initialized for XEmacs (#37451)

* Fri Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New locale.alias file for emacs-nox

* Tue Mar  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- update rpm-spec-mode.el to 0.11e - this should fix #30702

* Fri Feb 16 2001 Preston Brown <pbrown@redhat.com>
- require tamago, or japanese cannot be input (#27932).

* Sat Jan 27 2001 Jakub Jelinek <jakub@redhat.com>
- Preprocess Makefiles as if they were assembly, not C source.

* Wed Jan 24 2001 Yukihiro Nakai <ynakai@redhat.com>
- Fix the fontset problem when creating a new frame.

* Thu Jan 18 2001 Trond Eivind Glomsrød <teg@redhat.com>
- add Japanese support from Yukihiro Nakai <ynakai@redhat.com>

* Thu Jan 04 2001 Preston Brown <pbrown@redhat.com>
- do not remove etags, only ctags, per Tom Tromey's suggestion.

* Wed Dec 27 2000 Tim Powers <timp@redhat.com>
- bzipped sources to conserve space

* Mon Dec 18 2000 Trond Eivind Glomsrød <teg@redhat.com>
- add /usr/share/emacs/locale.alias , which had gone AWOL
- update rpm-spec-mode to 0.11a, fresh from the author
  (Stig Bjorlykke <stigb@tihlde.org>). The changes we made 
  are integrated.

* Fri Dec 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- prereq fileutils for emacs-nox

* Mon Dec 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- do locale.alias fix for emacs-nox only, as it somehow
  broke the subject line in gnus. Weird.
- update to gnus 5.8.7

* Fri Dec 08 2000 Than Ngo <than@redhat.com>
- add support s390 machine

* Thu Dec 07 2000 Trond Eivind Glomsrød <teg@redhat.com>
- add rpm-spec-mode after modifying (use Red Hat groups,
  from /usr/share/doc/rpm-version/GROUPS) and fixing
  colours(don't specify "yellow" on "bright") Also, 
  use gpg, not pgp.
- use it (site-start.el)
- add mwheel 
- use it, in /etc/skel/.emacs

* Thu Nov 30 2000 Trond Eivind Glomsrød <teg@redhat.com>
- add /usr/share/emacs/site-lisp/site-start.d
- change site-start.el so files in the above directory
  are automatically run on startup
- don't set the ispell name in site-start.el, use the
  above directory instead  

* Thu Oct 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fix icon name in the .desktop file
- don't have site-start.el "noreplace"
- load psgml-init (if present) in the default site-start.el
  to avoid psgml modifying the file

* Tue Oct 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new and better emacs.desktop file

* Tue Oct 10 2000 Trond Eivind Glomsrød <teg@redhat.com>
- remove ctags.1 and etags.1 from the emacs etc directory
  (#18011)
- fix the emacs-nox not to use the locale.alias in XFree86
  (#18548)... copy it into /usr/share/emacs and patch
  the startup files to use it. Argh.

* Wed Oct 04 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fix initialization of python mode (require it before
  customizing it)

* Fri Sep 22 2000 Bill Nottingham <notting@redhat.com>
- don't use bcopy without a prototype

* Thu Aug 24 2000 Trond Eivind Glomsrød <teg@redhat.com>
- define MAIL_USE_LOCKF 
- remove setgid on movemail

* Mon Aug 07 2000 Trond Eivind Glomsrød <teg@redhat.com>
- add /usr/share/emacs/site-lisp/subdirs.el (#15639)

* Tue Jul 25 2000 Trond Eivind Glomsrød <teg@redhat.com>
- remove "-b" option from manpage

* Fri Jul 21 2000 Trond Eivind Glomsrød <teg@redhat.com>
- remove Japanese support

* Mon Jul 17 2000 Matt Wilson <msw@redhat.com>
- updated .desktop entry and icon

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jul 07 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fix some typos in spec file

* Sun Jul 02 2000 Trond Eivind Glomsrød <teg@redhat.com>
- make /etc/skel/.emacs 0644

* Wed Jun 28 2000 Trond Eivind Glomsrød <teg@redhat.com>
- include python mode and change in site-start.el related to this
- some changes to the default .emacs 

* Mon Jun 26 2000 Matt Wilson <msw@redhat.com>
- don't build with -O2 on alpha until we can track down the compiler
  bug that causes crashes in the garbage collector
- removed all the nox Japanese packages

* Mon Jun 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- include site-start.el as a a config file
- add aspell support via the above

* Fri Jun 16 2000 Trond Eivind Glomsrød <teg@redhat.com>
- (from MSW) different compression on IA64 to avoid hangs
- remove etags/ctags - use a separate package. Disable patch1

* Wed Jun 14 2000 Matt Wilson <msw@redhat.com>
- edited japanese patch not to patch configure
- fixed a missing escaped " in a wc string
- merge japanese support to head of development

* Tue Jun 13 2000 Trond Eivind Glomsrød <teg@redhat.com>
- Version 20.7
- Add requirement for final newline to the default .emacs
- redid the Xaw3d patch
- checked all patches, discarded those we've upstreamed

* Wed Jun 07 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_mandir} and %%{_infodir}

* Fri Jun  2 2000 Bill Nottingham <notting@redhat.com>
- add yet another ia64 patch

* Mon May 22 2000 Bill Nottingham <notting@redhat.com>
- add another ia64 patch

* Fri May 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- Disabled the compile patch for 20.6

* Thu May 18 2000 Bill Nottingham <notting@redhat.com>
- add in ia64 patch

* Thu May 18 2000 Trond Eivind Glomsrød <teg@redhat.com>
- don't apply the unexelf patch - use a new unexelf.c file
  from the 21 source tree (this will go into the 20.7 tree)

* Wed May 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added patch by jakub to make it work with glibc2.2

* Mon May 08 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fixed a problem with ange-ftp and kerberized ftp

* Mon May 08 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with new Xaw3d

* Thu Apr 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- let the build system handle gzipping man pages and stripping
- added patch to increase keyboard buffer size

* Thu Apr 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- gzip man pages

* Thu Apr 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added a security patch from RUS-CERT, which fixes 
  bugs mentioned in "Advisory 200004-01: GNU Emacs 20"

* Tue Apr 18 2000 Trond Eivind Glomsrød <teg@redhat.com>
- patched to detect bash2 scripts. 

* Thu Apr 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- removed configuraton file status from /usr/share/pixmaps/emacs.png

* Fri Mar 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- update to 20.6 and make it compile

* Mon Feb 21 2000 Preston Brown <pbrown@redhat.com>
- add .emacs make the delete key work to delete forward character for X ver.

* Wed Feb 16 2000 Cristian Gafton <gafton@redhat.com>
- fix bug #2988
- recompile patched .el files (suggested by Pavel.Janik@linux.cz)
- prereq /sbin/install-info

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig gone

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- fix descriptions and summary
- fix permissions for emacs niaries (what the hell does 1755 means for a
  binary?)
- added missing, as per emacs Changelog, NCURSES_OSPEED_T compilation
  flag; without it emacs on Linux is making global 'ospeed' short which
  is not the same as 'speed_t' expected by libraries. (reported by Michal
  Jaegermann <michal@harddata.com>)

* Mon Jan 10 2000 David S. Miller <davem@redhat.com>
- Revert src/unexecelf.c to 20.4 version, fixes SPARC problems.

* Sun Jan  9 2000 Matt Wilson <msw@redhat.com>
- strip emacs binary
- disable optimizations for now, they cause illegal instructions on SPARC.

* Sun Jan 09 2000 Paul Fisher <pnfisher@redhat.com>
- upgrade to 20.5a
- remove python-mode, wheelmouse support, and auctex menu
- import emacs.desktop with icon from GNOME

* Wed Dec 08 1999 Ngo Than <than@redhat.de>
- added python-mode, wheelmouse support and auctex menu
- added Comment[de] in emacs.desktop

* Sat Sep 25 1999 Preston Brown <pbrown@redhat.com>
- added desktop entry

* Thu Sep 23 1999 Preston Brown <pbrown@redhat.com>
- tried to fix triggers, hopefully working now.

* Wed Sep 01 1999 Preston Brown <pbrown@redhat.com>
- added trigger for making symlink to /usr/bin/emacs in emacs-nox package

* Thu Jul 22 1999 Paul Fisher <pnfisher@redhat.com>
- upgrade to 20.4
- cleaned up spec

* Fri Apr 16 1999 Owen Taylor <otaylor@redhat.com>
- replace bad xemacs compiled .elc file for mh-e with one compiled
  on emacs

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- make sure movemail doesn't get %%defattr()'d to root.root

* Wed Apr 14 1999 Cristian Gafton <gafton@redhat.com>
- patch to make it work with dxpc

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- updated mh-utils emacs lisp file to match our nmh path locations

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Fri Feb 26 1999 Cristian Gafton <gafton@redhat.com>
- linker scripts hack to make it build on the alpha

* Fri Jan  1 1999 Jeff Johnson <jbj@redhat.com>
- add leim package (thanks to Pavel.Janik@inet.cz).

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Wed Sep 30 1998 Cristian Gafton <gafton@redhat.com>
- backed up changes to uncompress.el (it seems that the one from 20.2 works
  much better)

* Mon Sep 28 1998 Jeff Johnson <jbj@redhat.com>
- eliminate /tmp race in rcs2log

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 20.3

* Tue Jun  9 1998 Jeff Johnson <jbj@redhat.com>
- add --with-pop to X11 compile.
- include contents of /usr/share/.../etc with main package.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Mon Jun 01 1998 David S. Miller <davem@dm.cobaltmicro.com>
- fix signals when linked with glibc on non-Intel architectures
  NOTE: This patch is not needed with emacs >20.2

* Thu May 07 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- added /usr/lib/emacs/20.2/*-redhat-linux directory in the filelist

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- alpha started to like emacs-nox again :-)

* Thu Nov  6 1997 Michael Fulbright <msf@redhat.com>
- alpha just doesnt like emacs-nox, taking it out for now

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added multibyte support back into emacs 20.2
- added wmconfig for X11 emacs
- fixed some errant buildroot references

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- joy a new version of emacs! Of note - no lockdir any more.
- use post/preun sections to handle numerous GNU info files

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- stopped stripping it as it seems to break things

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- turned off ecoff support on the Alpha (which doesn't build anymore)

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved ctags to gctags to fit in the more powerful for C (but less
  general) exuberant ctags as the binary /usr/bin/ctags and the
  man page /usr/man/man1/ctags.1
