Summary: python3 link to default /usr/bin/python
Name: python
Version: 3.6.8
Release: 39
Group: System Environment/Base
BuildRoot: /var/tmp/%{name}-buildroot
License: GPL
Requires: python3 python2

%description
python3 link to default /usr/bin/python.

%package libs
Summary: python3 link to default /usr/bin/python
Group: System Environment/Base
Requires: python2-libs python3-libs

%description libs
python3 link to default /usr/bin/python

%package devel
Summary: python3 link to default /usr/bin/python
Group: System Environment/Base
Requires: python2-devel python3-devel

%description devel
python3 link to default /usr/bin/python

%package idle
Summary: python3 link to default /usr/bin/python
Group: System Environment/Base
Requires: python3-idle

%description idle
python3 link to default /usr/bin/python

%package tkinter
Summary: python3 link to default /usr/bin/python
Group: System Environment/Base
Requires: python2-tkinter python3-tkinter

%description tkinter
python3 link to default /usr/bin/python

%package test
Summary: python3 link to default /usr/bin/python
Group: System Environment/Base
Requires: python2-test python3-test

%description test
python3 link to default /usr/bin/python

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%post
ln -s /usr/bin/python3 /usr/bin/python

%postun
rm -f /usr/bin/python

%files


%changelog
* Wed Aug 19 2009 Rob White <rwhite@bla.net>
- First test of RPM
