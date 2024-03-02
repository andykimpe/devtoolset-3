%global pkg_name decentxml
%{?scl:%scl_package %{pkg_name}}

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

%{?java_common_find_provides_and_requires}

Name:             devtoolset-3-decentxml
Version:          1.4
Release:          10%{?dist}
Summary:          XML parser optimized for round-tripping and code reuse
License:          BSD
Group:            Development/Libraries
URL:              http://code.google.com/p/decentxml
Source0:          https://decentxml.googlecode.com/files/decentxml-1.4-src.zip
# for running w3c conformance test suite
Source1:          http://www.w3.org/XML/Test/xmlts20031210.zip
BuildArch:        noarch

BuildRequires:    %{?scl_prefix_java_common}maven-local
BuildRequires:    %{?scl_prefix_maven}maven-surefire-provider-junit
BuildRequires:    %{?scl_prefix_maven}apache-commons-parent

%description
XML parser optimized for round-tripping and code reuse with main
features being:
 * Allows 100% round-tripping, even for weird whitespace between
   attributes in the start tag or in the end tag
 * Suitable for building editors and filters which want/need to
   preserve the original file layout as much as possible
 * Error messages have line and column information
 * Easy to reuse individual components
 * XML 1.1 compatible

%package javadoc
Summary:          API documentation for decentxml
Group:            Documentation


%description javadoc
This package contains the API documentation for decentxml.

%prep
%setup -q -n decentxml-%{version}
# we are looking for xml conformance data one lever above so unzip
# here and symlink there
unzip %{SOURCE1}
ln -sf decentxml-%{version}/xmlconf ../xmlconf
sed -i -e "s|junit-dep|junit|g" pom.xml

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_file  : decentxml
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Apr 27 2015 Mat Booth <mat.booth@redhat.com> - 1.4-10
- Related: rhbz#1184224 - Bump release and rebuild

* Thu Jan 15 2015 Mat Booth <mat.booth@redhat.com> - 1.4-9
- Rebuild to regenerate requires/provides

* Wed Jan 07 2015 Roland Grunberg <rgrunber@redhat.com> - 1.4-8
- SCL-ize
- Related: rhbz#1175105

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.4-3
- Build with xmvn

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 1 2012 Alexander Kurtakov <akurtako@redhat.com> 1.4-1
- Update to 1.4 upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-1
- Initial version of the package
