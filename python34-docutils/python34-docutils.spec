%global srcname docutils

Name:           python34-%{srcname}
Version:        0.14
Release:        1%{?dist}
Summary:        System for processing plaintext documentation

# See COPYING.txt for information
License:        Public Domain and BSD and Python and GPLv3+
URL:            http://docutils.sourceforge.net
Source0:        http://downloads.sourceforge.net/docutils/%{srcname}-%{version}.tar.gz
# Sometimes we need snapshots.  Instructions below:
# svn co -r 7687 svn://svn.code.sf.net/p/docutils/code/trunk/docutils
# cd docutils
# python setup.py sdist
# The tarball is in dist/docutils-VERSION.tar.gz
#Source0:        %{srcname}-%{version}.tar.gz

BuildArch:       noarch

BuildRequires:  python-tools
BuildRequires:  python34
BuildRequires:  python34-devel

%description
The Docutils project specifies a plaintext markup language, reStructuredText,
which is easy to read and quick to write.  The project includes a python
library to parse rST files and transform them into other useful formats such
as HTML, XML, and TeX as well as commandline tools that give the enduser
access to this functionality.

Currently, the library supports parsing rST that is in standalone files and
PEPs (Python Enhancement Proposals).  Work is underway to parse rST from
Python inline documentation modules and packages.

#%package -n python%{python3_pkgversion}-%{srcname}
#Summary:        System for processing plaintext documentation for python %{python3_version}

# This isn't yet packaged for EPEL, but it should mostly work without it
#Requires:       python%{python3_pkgversion}-pillow

#%description -n python%{python3_pkgversion}-%{srcname}
#The Docutils project specifies a plaintext markup language, reStructuredText,
#which is easy to read and quick to write.  The project includes a python
#library to parse rST files and transform them into other useful formats such
#as HTML, XML, and TeX as well as commandline tools that give the enduser
#access to this functionality.
#
#Currently, the library supports parsing rST that is in standalone files and
#PEPs (Python Enhancement Proposals).  Work is underway to parse rST from
#Python inline documentation modules and packages.
#
#This package contains the module, ported to run under python %{python3_version}.
#
#%if 0%{?python3_other_pkgversion}
#%package -n python%{python3_other_pkgversion}-%{srcname}
#Summary:        System for processing plaintext documentation for python %{python3_other_version}
#BuildRequires:  python%{python3_other_pkgversion}-devel
# This isn't yet packaged for EPEL, but it should mostly work without it
#Requires:       python%{python3_other_pkgversion}-pillow
#
#%description -n python%{python3_other_pkgversion}-%{srcname}
#The Docutils project specifies a plaintext markup language, reStructuredText,
#which is easy to read and quick to write.  The project includes a python
#library to parse rST files and transform them into other useful formats such
#as HTML, XML, and TeX as well as commandline tools that give the enduser
#access to this functionality.
#
#Currently, the library supports parsing rST that is in standalone files and
#PEPs (Python Enhancement Proposals).  Work is underway to parse rST from
#Python inline documentation modules and packages.
#
#This package contains the module, ported to run under python %{python3_other_version}.
#%endif # python3_other_pkgversion


%package doc
Summary:        Documentation for python-%{srcname}

%description doc
Documentation for python-%{srcname}


%prep
%setup -q -n %{srcname}-%{version}

# Remove shebang from library files
for file in docutils/utils/{code_analyzer.py,punctuation_chars.py,error_reporting.py,smartquotes.py} docutils/utils/math/{latex2mathml.py,math2html.py} docutils/writers/xetex/__init__.py; do
sed -i -e '/#! *\/usr\/bin\/.*/{1D}' $file
done

iconv -f ISO88592 -t UTF8 tools/editors/emacs/IDEAS.rst > tmp
mv tmp tools/editors/emacs/IDEAS.rst


%build
  CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python3.4 setup.py  build --executable="/usr/bin/python3.4 -sP"
###%#py3_build
###%#{?python3_other_pkgversion: %py3_other_build}


%install
  CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
  /usr/bin/python3.4 setup.py  install -O1 --skip-build --root %{buildroot} --prefix /usr 
  rm -rfv %{buildroot}/usr/bin/__pycache__
###%#py3_install

# docutils setup.py runs 2to3 on a copy of the tests and puts it in sitelib.
rm -rf %{buildroot}/usr/lib/python3.4/site-packages/test

for file in %{buildroot}/%{_bindir}/*.py; do
    mv $file `dirname $file`/`basename $file .py`-3.4
    ln -s `basename $file .py`-3.4 `dirname $file`/`basename $file .py`-3
done

###%#if 0%{?python3_other_pkgversion}
###%#py3_other_install \
#    --install-scripts %{_bindir}/%{python3_other_pkgversion}
#
## docutils setup.py runs 2to3 on a copy of the tests and puts it in sitelib.
#rm -rf %{buildroot}%{python3_other_sitelib}/test
#
#for file in %{buildroot}/%{_bindir}/%{python3_other_pkgversion}/*.py; do
#    mv $file `dirname $file`/../`basename $file .py`-%{python3_other_version}
#done
#
#rmdir %{buildroot}%{_bindir}/%{python3_other_pkgversion}
####%#endif # python3_other_pkgversion

# We want the licenses but don't need this build file
rm -f licenses/docutils.conf

# Flash file is used for testing docutils but shouldn't be in the installed package.
mv docs/user/rst/images/biohazard.swf ./biohazard.swf


%files -n python34-%{srcname}
 /usr/bin/rst2html-3
/usr/bin/rst2html-3.4
/usr/bin/rst2html4-3
/usr/bin/rst2html4-3.4
/usr/bin/rst2html5-3
/usr/bin/rst2html5-3.4
/usr/bin/rst2latex-3
/usr/bin/rst2latex-3.4
/usr/bin/rst2man-3
/usr/bin/rst2man-3.4
/usr/bin/rst2odt-3
/usr/bin/rst2odt-3.4
/usr/bin/rst2odt_prepstyles-3
/usr/bin/rst2odt_prepstyles-3.4
/usr/bin/rst2pseudoxml-3
/usr/bin/rst2pseudoxml-3.4
/usr/bin/rst2s5-3
/usr/bin/rst2s5-3.4
/usr/bin/rst2xetex-3
/usr/bin/rst2xetex-3.4
/usr/bin/rst2xml-3
/usr/bin/rst2xml-3.4
/usr/bin/rstpep2html-3
/usr/bin/rstpep2html-3.4
#%license COPYING.txt licenses
#%doc BUGS.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt 
#%doc THANKS.txt tools/editors
#%{_bindir}/*-3.4
#%{_bindir}/*-3
/usr/lib/python3.4/site-packages/*

#%if 0%{?python3_other_pkgversion}
#%files -n python%{python3_other_pkgversion}-%{srcname}
#%license COPYING.txt licenses
#%doc BUGS.txt FAQ.txt HISTORY.txt README.txt RELEASE-NOTES.txt
#%doc THANKS.txt tools/editors
#%{_bindir}/*-%{python3_other_version}
#%{python3_other_sitelib}/*
#%endif # python3_other_pkgversion

%files doc
%license COPYING.txt licenses
#%doc docs/*

%changelog
* Mon Apr 15 2019 Orion Poplawski <orion@nwra.com> - 0.14-1
- Update to 0.14
- Provide *-3 symlinks in /usr/bin (bugz#1700061)

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 0.12-0.10.20140510svn7747
- Rebuilt to change main python from 3.4 to 3.6

* Wed Jan 16 2019 Scott K Logan <logans@cottsay.net> - 0.12-0.9.20140510svn7747
- Add Python 3.6 sub-package

* Sun Nov 27 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12-0.8.20140510svn7747
- Use %%license for COPYING.txt
- Make separate doc sub-package

* Wed Nov 2 2016 Orion Poplawski <orion@cora.nwra.com> - 0.12-0.7.20140510svn7747
- Initial EPEL package
