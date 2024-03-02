%global pkg_name cbi-plugins
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

%global tag cbi-plugins-1.1.1

Name:           devtoolset-3-cbi-plugins
Version:        1.1.1
Release:        4.bootstrap1%{?dist}
Summary:        A set of helpers for Eclipse CBI

Group:          Development/Libraries
License:        EPL
URL:            http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/
Source0:        http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/snapshot/%{tag}.tar.bz2
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}tycho
BuildRequires:  %{?scl_prefix}tycho-extras
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}httpcomponents-client
Requires:       %{?scl_prefix}tycho
Requires:       %{?scl_prefix}tycho-extras

%description
A set of helpers for Eclipse CBI.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{pkg_name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_disable_module eclipse-macsigner-plugin
%pom_disable_module eclipse-winsigner-plugin
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Apr 27 2015 Mat Booth <mat.booth@redhat.com> - 1.1.1-4
- Related: rhbz#1184224 - Bump release and rebuild

* Wed Jan 14 2015 Mat Booth <mat.booth@redhat.com> - 1.1.1-3
- Related: rhbz#1175105 - Rebuild for latest httpcomponents

* Fri Jan 09 2015 Roland Grunberg <rgrunber@redhat.com> - 1.1.1-2
- SCL-ize.
- Related: rhbz#1175105

* Mon Jul 28 2014 Roland Grunberg <rgrunber@redhat.com> - 1.1.1-2
- Update to 1.1.1 Release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.5-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-2
- Disable win/mac signers.

* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-1
- Update to latest upstream.

* Mon Sep 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.4-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.3-1
- Update to latest upstream.

* Thu Mar 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.4.git734d40
- Update to latest upstream.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.3.git120561
- Delete empty line from sources.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.2.git120561
- Review remarks fixed.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.1.git120561
- Initial contribution.
