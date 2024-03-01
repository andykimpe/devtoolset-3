Summary: python3 link to default /usr/bin/python
Name: python
Version: 3.6.8
Release: 39
Group: System Environment/Base
BuildRoot: /var/tmp/%{name}-buildroot
License: GPL
Requires: python3

%description
python3 link to default /usr/bin/python.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files


%changelog
* Wed Aug 19 2009 Rob White <rwhite@bla.net>
- First test of RPM
