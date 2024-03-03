%{?scl:%scl_package eclipse-license}
%{!?scl:%global pkg_name eclipse-license}
%{?java_common_find_provides_and_requires}

%global license_ver 1.0.1
%global qualifier v20140414-1359
%global gittag org.eclipse.license-license-%{license_ver}.%{qualifier}

Name:      devtoolset-3-eclipse-license
Version:   %{license_ver}
Release:   5.3.bootstrap1%{?dist}
Summary:   Shared license feature for Eclipse

License:   EPL
URL:       http://wiki.eclipse.org/CBI
Source0:   http://git.eclipse.org/c/cbi/org.eclipse.license.git/snapshot/%{gittag}.tar.bz2

BuildArch: noarch

BuildRequires: %{?scl_prefix}tycho
BuildRequires: %{?scl_prefix}tycho-extras

Requires: %{?scl_prefix}eclipse-filesystem

%description
Shared license feature for Eclipse. Other features may consume this
feature to avoid unnecessary duplication of license boiler plate.

%prep
%setup -q -n %{gittag}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build -j
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc org.eclipse.license/epl-v10.html

%changelog
* Tue Jan 13 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-5.3
- Related: rhbz#1175105 - Regenerate auto-provides

* Mon Jan 12 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-5.2
- Related: rhbz#1175105 - rebuilt

* Wed Jan 07 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-5.1
- Resolves: rhbz#1175105 - Import into DTS 3.1

* Tue Aug 26 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-5
- Build/install with xmvn
- Require eclipse-filesystem

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Mat Booth <mat.booth@redhat.com> - 1.0.1-3
- Update to latest upstream.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-2
- Use Xmvn.

* Thu Mar 13 2014 Mat Booth <mat.booth@redhat.com> - 1.0.0-1
- Initial version of license shared feature.

