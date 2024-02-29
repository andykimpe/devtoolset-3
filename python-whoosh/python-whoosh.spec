%global mod_name Whoosh

Name:           python-whoosh
Version:        2.7.4
Release:        5%{?dist}
Summary:        Fast, pure-Python full text indexing, search, and spell checking library 

License:        BSD 
URL:            http://pythonhosted.org/Whoosh/
Source0:        https://pypi.python.org/packages/source/W/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  pytest 
BuildRequires:  python-sphinx

%description
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

%package -n python2-whoosh
Summary:    Fast, Python3 full text indexing, search, and spell checking library
%{?python_provide:%python_provide python2-whoosh}

%description -n python2-whoosh
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

%package -n python34-whoosh
Summary:    Fast, Python3 full text indexing, search, and spell checking library
BuildRequires: python34-devel
BuildRequires: python34-setuptools
BuildRequires: python34-pytest
Provide: python34-whoosh

%description -n python34-whoosh
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-whoosh
Summary:    Fast, Python3 full text indexing, search, and spell checking library
BuildRequires: python%{python3_other_pkgversion}-devel
BuildRequires: python%{python3_other_pkgversion}-setuptools
BuildRequires: python%{python3_other_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_other_pkgversion}-whoosh}

%description -n python%{python3_other_pkgversion}-whoosh
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how Whoosh
works can be extended or replaced to meet your needs exactly.
%endif

%prep
%setup -q -n %{mod_name}-%{version}

%build
%py2_build
%py3_build
%if 0%{?python3_other_pkgversion}
%py3_other_build
%endif
sphinx-build docs/source docs/html
rm -f docs/html/.buildinfo
rm -rf docs/html/.doctrees

%install
%py2_install
%py3_install
%if 0%{?python3_other_pkgversion}
%py3_other_install
%endif

%check
%{__python2} setup.py test
%{__python3} setup.py test
%if 0%{?python3_other_pkgversion}
%{__python3_other} setup.py test
%endif

%files -n python2-whoosh
%license LICENSE.txt
%doc docs/html/ README.txt
%{python2_sitelib}/*.egg-info/
%{python2_sitelib}/whoosh

%files -n python34-whoosh
%license LICENSE.txt
%doc README.txt docs/html/
%{python3_sitelib}/whoosh
%{python3_sitelib}/*.egg-info/

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-whoosh
%license LICENSE.txt
%doc README.txt docs/html/
%{python3_other_sitelib}/whoosh
%{python3_other_sitelib}/*.egg-info/
%endif

%changelog
* Thu Apr 04 2019 Orion Poplawski <orion@nwra.com> - 2.7.4-5
- Build for python3_other

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 2.7.4-4
- Rebuilt to change main python from 3.4 to 3.6

* Wed Oct 12 2016 Orion Poplawski <orion@cora.nwra.com> - 2.7.4-3
- Ship python2-whoosh
- Build python3 package for EPEL7
- Modernize spec

* Mon May 02 2016 Robert Kuska <rkuska@redhat.com> - 2.7.4-1
- Update to 2.7.4

* Wed Jul 30 2014 Robert Kuska <rkuska@redhat.com> - 2.5.7-4
- Change spec for el6 and epel7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Robert Kuska <rkuska@redhat.com> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 03 2014 Robert Kuska <rkuska@redhat.com> - 2.5.7-1
- Rebase to 2.5.7

* Mon Jan 27 2014 Robert Kuska <rkuska@redhat.com> - 2.5.6-1
- Rebase to 2.5.6

* Tue Nov 19 2013 Robert Kuska <rkuska@redhat.com> - 2.5.5-1
- Rebase to 2.5.5

* Mon Sep 09 2013 Robert Kuska <rkuska@redhat.com> - 2.5.3-1
- Rebase to 2.5.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Robert Kuska <rkuska@redhat.com> - 2.5.1-1
- Update source
- Add python3 subpackage (rhbz#979235)

* Mon Apr 08 2013 Robert Kuska <rkuska@redhat.com> - 2.4.1-2
- Review fixes

* Fri Apr 05 2013 Robert Kuska <rkuska@redhat.com> - 2.4.1-1
- Initial package

