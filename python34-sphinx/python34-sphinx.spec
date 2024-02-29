%global upstream_name Sphinx

Name:       python34-sphinx
Version:    1.2.3
Release:    6%{?dist}
Summary:    Python documentation generator

# Unless otherwise noted, the license for code is BSD
# sphinx/util/stemmer.py Public Domain
# sphinx/pycode/pgen2 Python
# jquery (MIT or GPLv2)
License:    BSD and Public Domain and Python and (MIT or GPLv2)
URL:        http://sphinx.pocoo.org/
Source0:    http://pypi.python.org/packages/source/S/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
Patch0:     Sphinx-1.2.1-mantarget.patch
Patch1:     Sphinx-1.2.2-verbosetests.patch
Patch2:     html-parser-HTMLParserError-removed.patch
Patch3:     python3-sphinx-noclean.patch
# Rename locale files to sphinx3 to avoid conflicts
Patch4:     python3-sphinx-sphinx3.patch
Patch5:     Fix-3212-HTML-Builders-crashes-with-docutils-0.13.patch

BuildArch:     noarch

# for fixes
BuildRequires: dos2unix

# for testing
BuildRequires: gettext
BuildRequires: texinfo
# For man/html - requires python2
BuildRequires: python2-docutils
BuildRequires: python-jinja2
# note: no Python3 xapian binding yet
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-collection-latex
BuildRequires: tex(cmap.sty)
BuildRequires: tex(ecrm1000.tfm)
BuildRequires: tex(fancybox.sty)
BuildRequires: tex(footnote.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(parskip.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(threeparttable.sty)
BuildRequires: tex(upquote.sty)
BuildRequires: tex(wrapfig.sty)

Requires:      python34-sphinx = %{version}-%{release}

%description
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.


%package common
Summary:       Shared files for %{name}

%description common
Shared files for %{name}.


%package latex
Summary:       LaTeX builder dependencies for %{name}
Requires:      python34}-sphinx = %{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      tex(cmap.sty)
Requires:      tex(ecrm1000.tfm)
Requires:      tex(fancybox.sty)
Requires:      tex(footnote.sty)
Requires:      tex(framed.sty)
Requires:      tex(multirow.sty)
Requires:      tex(parskip.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(threeparttable.sty)
Requires:      tex(upquote.sty)
Requires:      tex(wrapfig.sty)

%description latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.


%package -n python34-sphinx
Summary:       Python documentation generator
BuildRequires: python34-devel
BuildRequires: python34-setuptools
BuildRequires: python34-docutils
BuildRequires: python34-jinja2
BuildRequires: python34-pygments
BuildRequires: python34-nose
BuildRequires: python34-sqlalchemy
BuildRequires: python34-whoosh
Requires:      %{name}-common = %{version}-%{release}
Requires:      python34-docutils
Requires:      python34-jinja2
Requires:      python34-pygments

%description -n python34-sphinx
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.

%package -n python34-sphinx-latex
Summary:       LaTeX builder dependencies for %{name}
Requires:      python34-sphinx = %{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      tex(cmap.sty)
Requires:      tex(ecrm1000.tfm)
Requires:      tex(fancybox.sty)
Requires:      tex(footnote.sty)
Requires:      tex(framed.sty)
Requires:      tex(multirow.sty)
Requires:      tex(parskip.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(threeparttable.sty)
Requires:      tex(upquote.sty)
Requires:      tex(wrapfig.sty)

%description -n python34-sphinx-latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.


#%if 0%{?python3_other_pkgversion}
#%package -n python%{python3_other_pkgversion}-sphinx
#Summary:       Python documentation generator
#BuildRequires: python%{python3_other_pkgversion}-devel
#BuildRequires: python%{python3_other_pkgversion}-setuptools
#BuildRequires: python%{python3_other_pkgversion}-docutils
#BuildRequires: python%{python3_other_pkgversion}-jinja2
#BuildRequires: python%{python3_other_pkgversion}-pygments
#BuildRequires: python%{python3_other_pkgversion}-nose
#BuildRequires: python%{python3_other_pkgversion}-sqlalchemy
#BuildRequires: python%{python3_other_pkgversion}-whoosh
#Requires:      %{name}-common = %{version}-%{release}
#Requires:      python%{python3_other_pkgversion}-docutils
#Requires:      python%{python3_other_pkgversion}-jinja2
#Requires:      python%{python3_other_pkgversion}-pygments
#
#%description -n python%{python3_other_pkgversion}-sphinx
#Sphinx is a tool that makes it easy to create intelligent and
#beautiful documentation for Python projects (or other documents
#consisting of multiple reStructuredText sources), written by Georg
#Brandl. It was originally created to translate the new Python
#documentation, but has now been cleaned up in the hope that it will be
#useful to many other projects.
#
#Sphinx uses reStructuredText as its markup language, and many of its
#strengths come from the power and straightforwardness of
#reStructuredText and its parsing and translating suite, the Docutils.
#
#Although it is still under constant development, the following
#features are already present, work fine and can be seen "in action" in
#the Python docs:
#
#    * Output formats: HTML (including Windows HTML Help) and LaTeX,
#      for printable PDF versions
#    * Extensive cross-references: semantic markup and automatic links
#      for functions, classes, glossary terms and similar pieces of
#      information
#    * Hierarchical structure: easy definition of a document tree, with
#      automatic links to siblings, parents and children
#    * Automatic indices: general index as well as a module index
#    * Code handling: automatic highlighting using the Pygments highlighter
#    * Various extensions are available, e.g. for automatic testing of
#      snippets and inclusion of appropriately formatted docstrings.
#
#%package -n python%{python3_other_pkgversion}-sphinx-latex
#Summary:       LaTeX builder dependencies for %{name}
#Requires:      python%{python3_other_pkgversion}-sphinx = %{version}-%{release}
#Requires:      texlive-collection-fontsrecommended
#Requires:      texlive-collection-latex
#Requires:      tex(cmap.sty)
#Requires:      tex(ecrm1000.tfm)
#Requires:      tex(fancybox.sty)
#Requires:      tex(footnote.sty)
#Requires:      tex(framed.sty)
#Requires:      tex(multirow.sty)
#Requires:      tex(parskip.sty)
#Requires:      tex(titlesec.sty)
#Requires:      tex(threeparttable.sty)
#Requires:      tex(upquote.sty)
#Requires:      tex(wrapfig.sty)
#
#%description -n python%{python3_other_pkgversion}-sphinx-latex
#Sphinx is a tool that makes it easy to create intelligent and
#beautiful documentation for Python projects (or other documents
#consisting of multiple reStructuredText sources), written by Georg
#Brandl. It was originally created to translate the new Python
#documentation, but has now been cleaned up in the hope that it will be
#useful to many other projects.
#
#This package pulls in the TeX dependencies needed by Sphinx's LaTeX
#builder.
#%endif


%package doc
Summary:    Documentation for %{name}
License:    BSD

%description doc
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package contains documentation in reST and HTML formats.


%prep
%setup -q -n %{upstream_name}-%{version}%{?prerel}
%patch0 -p1 -b .mantarget
# not backing up since every executable file in tests/ results in
# an additional "skipped" test
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .noclean
%patch4 -p1 -b .sphinx3
%patch5 -p1
sed '1d' -i sphinx/pycode/pgen2/token.py

# fix line encoding of bundled jquery.js
dos2unix -k ./sphinx/themes/basic/static/jquery.js

# Rename locale files
find sphinx/locale/*/LC_MESSAGES -name sphinx.\* | while read f
do
  mv ${f} ${f/sphinx./sphinx3.}
done

%build
%py3_build
#%if 0%{?python3_other_pkgversion}
#%py3_other_build
#%endif

pushd doc
make html
make man
rm -rf _build/html/.buildinfo
mv _build/html ..
popd


%install
%py3_install

# Make versioned executables
for i in sphinx-{apidoc,autogen,build,quickstart}; do
    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python3_version}
    ln -s $i-%{python3_version} %{buildroot}%{_bindir}/$i-3
done

#%if 0%{?python3_other_pkgversion}
#%py3_other_install
## Make versioned executables
#for i in sphinx-{apidoc,autogen,build,quickstart}; do
#    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python3_other_version}
#done
#%endif

# Deliver man pages
install -d %{buildroot}%{_mandir}/man1
mv doc/_build/man/sphinx-*.1 %{buildroot}%{_mandir}/man1/
for f in %{buildroot}%{_mandir}/man1/sphinx-*.1;
do
    cp -p $f $(echo $f | sed -e "s|.1$|-3.1|")
    mv $f $(echo $f | sed -e "s|.1$|-%{python3_version}.1|")
done

# Deliver rst files
rm -rf doc/_build
sed -i 's|python ../sphinx-build.py|/usr/bin/sphinx-build|' doc/Makefile
mv doc reST

# Move language files to /usr/share;
# patch to support this incorporated in 0.6.6
pushd %{buildroot}%{python3_sitelib}
for lang in `find sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -not -name __pycache__ -printf "%f "`;
do
  install -d %{buildroot}%{_datadir}/sphinx/locale/$lang
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx3.js \
     %{buildroot}%{_datadir}/sphinx/locale/$lang/
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx3.mo \
    %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
  rm -rf sphinx/locale/$lang
done
popd
%find_lang sphinx3

# Language files; Since these are javascript, it's not immediately obvious to
# find_lang that they need to be marked with a language.
(cd %{buildroot} && find . -name 'sphinx3.js') | sed -e 's|^.||' | sed -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.js$\):%lang(\2) \1\2\3:' \
  >> sphinx3.lang


%check
# texinfo seems to fail due to https://bugzilla.redhat.com/show_bug.cgi?id=1134160
# Several failures but the show must go on...
LANG=en_US.UTF-8 PYTHON=%{__python3} make test || :


%files
%license LICENSE
%{_bindir}/sphinx-*-3
%{_mandir}/man1/sphinx-*-3.1*

%files common -f sphinx3.lang
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*

%files latex
%license LICENSE

%files -n python34-sphinx
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst TODO
%{_bindir}/sphinx-*-%{python3_version}
%{_mandir}/man1/sphinx-*-%{python3_version}.1*
%{python3_sitelib}/*

%files -n python34-sphinx-latex
%license LICENSE

#%files -n python%{python3_other_pkgversion}-sphinx
#%license LICENSE
#%doc AUTHORS CHANGES EXAMPLES README.rst TODO
#%{_bindir}/sphinx-*-%{python3_other_version}
#%{python3_other_sitelib}/*

#%files -n python%{python3_other_pkgversion}-sphinx-latex
#%license LICENSE

%files doc
%license LICENSE
%doc html reST


%changelog
* Mon Dec 23 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.2.3-6
- Back-port patch for upstream bug #3212

* Thu Apr  4 2019 Orion Poplawski <orion@nwra.com> - 1.2.3-5
- Build for python3_other
- Move generic python3 script and man pages into main package 
- Move shared translations into common package 

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 1.2.3-4
- Rebuilt to change main python from 3.4 to 3.6

* Tue Dec 18 2018 Orion Poplawski <orion@nwra.com> - 1.2.3-3
- Rename locale files to avoid conflicts

* Thu Nov  8 2018 Orion Poplawski <orion@nwra.com> - 1.2.3-2
- Fix requires

* Tue Nov  6 2018 Orion Poplawski <orion@nwra.com> - 1.2.3-1
- Initial EPEL Python 3 package
