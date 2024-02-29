%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name:		python%{python3_pkgversion}-HepMC3
Version:	3.2.7
Release:	2%{?dist}
Summary:	C++ Event Record for Monte Carlo Generators

#		HepMC3 itself is LGPLv3+
#		The included bxzstr header-only library is MPLv2.0
License:	LGPL-3.0-or-later AND MPL-2.0
URL:		https://hepmc.web.cern.ch/hepmc/
Source0:	https://hepmc.web.cern.ch/hepmc/releases/HepMC3-%{version}.tar.gz

#		The ROOT cmake file used by this project requires cmake 3.9
BuildRequires:	cmake3 >= 3.9
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	root-core
BuildRequires:	root-hist
BuildRequires:	root-io
BuildRequires:	root-tree
BuildRequires:	json-devel
BuildRequires:	protobuf-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
%if %{?rhel}%{!?rhel:0} == 7
BuildRequires:	python2-devel
BuildRequires:	python%{python3_other_pkgversion}-devel
%endif
BuildRequires:	python%{python3_pkgversion}-devel
#		Additional requirements for tests
BuildRequires:	pythia8-devel
BuildRequires:	valgrind
#		For HepMC2 - HepMC3 conversion tests
BuildRequires:	HepMC-devel

%description
The HepMC3 package is an object oriented, C++ event record for
High Energy Physics Monte Carlo generators and simulation, described in
A. Buckley et al., "The HepMC3 Event Record Library for Monte Carlo
Event Generators" Comput.Phys.Commun. 260 (2021) 107310, arxiv:1912.08005.
It is a continuation of the HepMC2 by M. Dobbs and J.B. Hansen described
in "The HepMC C++ Monte Carlo event record for High Energy Physics"
(Comput. Phys. Commun. 134 (2001) 41). In version 3 the package
has undergone several modifications and in particular, the latest
HepMC3 series is a completely new re-write using currently available
C++11 techniques, and have out-of-the-box interfaces for the widely
used in HEP community ROOT and Python.

%package devel
Summary:	C++ Event Record for Monte Carlo Generators - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development files for %{name}.

%package search
Summary:	C++ Event Record for Monte Carlo Generators - search engine library
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description search
This package provides a library for selecting particles in HepMC3 event
records.

%package search-devel
Summary:	C++ Event Record for Monte Carlo Generators - %{name}-search development files
Requires:	%{name}-search%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description search-devel
This package provides development files for %{name}-search.

%package rootIO
Summary:	C++ Event Record for Monte Carlo Generators - ROOT IO
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description rootIO
This package provides a library for ROOT IO support.

%package rootIO-devel
Summary:	C++ Event Record for Monte Carlo Generators - %{name}-rootIO development files
Requires:	%{name}-rootIO%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description rootIO-devel
This package provides development files for %{name}-rootIO.

%package protobufIO
Summary:	C++ Event Record for Monte Carlo Generators - protobuf IO
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description protobufIO
This package provides a library for protobuf IO support.

%package protobufIO-devel
Summary:	C++ Event Record for Monte Carlo Generators - %{name}-protobufIO development files
Requires:	%{name}-protobufIO%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description protobufIO-devel
This package provides development files for %{name}-protobufIO.

%package interfaces-devel
Summary:	C++ Event Record for Monte Carlo Generators - generator interfaces
License:	LGPL-3.0-or-later AND GPL-3.0-or-later
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

%description interfaces-devel
This package provides HepMC3 interfaces to some common Monte Carlo generators.

%if %{?rhel}%{!?rhel:0} == 7
%package -n python2-HeppMC3
Summary:	HeppMC3 Python 2 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python2-HeppMC3
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python2-HeppMC3
This package provides the Python 2 bindings for HepMC3.

%package -n python2-HeppMC3-search
Summary:	HepMC3 search module Python 2 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python2-HeppMC3-search
Requires:	%{name}-search%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python2-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python2-HeppMC3-search
This package provides the Python 2 bindings for HepMC3 search module.

%package -n python2-HeppMC3-rootIO
Summary:	HepMC3 ROOT I/O module Python 2 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python2-HeppMC3-rootIO
Requires:	%{name}-rootIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python2-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python2-HeppMC3-rootIO
This package provides the Python 2 bindings for HepMC3 ROOT I/O module.

%package -n python2-HeppMC3-protobufIO
Summary:	HepMC3 protobuf I/O module Python 2 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python2-HeppMC3-protobufIO
Requires:	%{name}-protobufIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python2-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python2-%{name}-protobufIO
This package provides the Python 2 bindings for HepMC3 protobuf I/O module.

%package -n python%{?python3_other_pkgversion}-HeppMC3
Summary:	HepMC3 Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_other_pkgversion}-HeppMC3
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python%{?python3_other_pkgversion}-%{name}
This package provides the Python 3 bindings for HepMC3.

%package -n python%{?python3_other_pkgversion}-HeppMC3-search
Summary:	HepMC3 search module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_other_pkgversion}-HeppMC3-search
Requires:	%{name}-search%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_other_pkgversion}-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python%{?python3_other_pkgversion}-HeppMC3-search
This package provides the Python 3 bindings for HepMC3 search module.

%package -n python%{?python3_other_pkgversion}-HeppMC3-rootIO
Summary:	HepMC3 ROOT I/O module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_other_pkgversion}-HeppMC3-rootIO
Requires:	%{name}-rootIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_other_pkgversion}-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python%{?python3_other_pkgversion}-HeppMC3-rootIO
This package provides the Python 3 bindings for HepMC3 ROOT I/O module.

%package -n python%{?python3_other_pkgversion}-HeppMC3-protobufIO
Summary:	HepMC3 protobuf I/O module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_other_pkgversion}-HeppMC3-protobufIO
Requires:	%{name}-protobufIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_other_pkgversion}-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python%{?python3_other_pkgversion}-HeppMC3-protobufIO
This package provides the Python 3 bindings for HepMC3 protobuf I/O module.
%endif

%package -n python%{python3_pkgversion}-HeppMC3
Summary:	HepMC3 Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_pkgversion}-HeppMC3
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python%{python3_pkgversion}-HeppMC3
This package provides the Python 3 bindings for HepMC3.

%package -n python%{python3_pkgversion}-HeppMC3-search
Summary:	HepMC3 search module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_pkgversion}-HeppMC3-search
Requires:	%{name}-search%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python%{python3_pkgversion}-HeppMC3-search
This package provides the Python 3 bindings for HepMC3 search module.

%package -n python%{python3_pkgversion}-HeppMC3-rootIO
Summary:	HepMC3 ROOT I/O module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_pkgversion}-HeppMC3-rootIO
Requires:	%{name}-rootIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python%{python3_pkgversion}-HeppMC3-rootIO
This package provides the Python 3 bindings for HepMC3 ROOT I/O module.

%package -n python%{python3_pkgversion}-HeppMC3-protobufIO
Summary:	HepMC3 protobuf I/O module Python 3 bindings
License:	LGPL-3.0-or-later AND CNRI-Python AND BSD-3-Clause
Provides:	python%{python3_pkgversion}-HeppMC3-protobufIO
Requires:	%{name}-protobufIO%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-HeppMC3%{?_isa} = %{version}-%{release}

%description -n python%{python3_pkgversion}-HeppMC3-protobufIO
This package provides the Python 3 bindings for HepMC3 protobuf I/O module.

%package doc
Summary:	C++ Event Record for Monte Carlo Generators - documentation
BuildArch:	noarch

%description doc
This package provides HepMC manuals and examples.

%prep
%setup -q -n HepMC3-3.2.7

%build
%cmake3 \
	-DHEPMC3_ENABLE_ROOTIO:BOOL=ON \
	-DHEPMC3_ROOTIO_INSTALL_LIBDIR:PATH=%{_libdir}/root \
	-DHEPMC3_ENABLE_PROTOBUFIO:BOOL=ON \
	-DHEPMC3_ENABLE_TEST:BOOL=ON \
	-DHEPMC3_INSTALL_INTERFACES:BOOL=ON \
	-DHEPMC3_INSTALL_EXAMPLES:BOOL=ON \
%if %{?rhel}%{!?rhel:0} == 7
	-DHEPMC3_PYTHON_VERSIONS=2,%python3_version,%python3_other_version \
%else
	-DHEPMC3_PYTHON_VERSIONS=%python3_version \
%endif
	-DHEPMC3_BUILD_DOCS:BOOL=ON \
	-DHEPMC3_BUILD_STATIC_LIBS:BOOL=OFF \
	-DHEPMC3_TEST_VALGRIND:BOOL=ON \
	-DCMAKE_INSTALL_DOCDIR:PATH=%{_pkgdocdir} \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake3_build

%install
%cmake3_install

rm %{buildroot}%{_includedir}/HeppMC3/bxzstr/LICENSE

%ldconfig_scriptlets
%ldconfig_scriptlets search
%ldconfig_scriptlets rootIO
%ldconfig_scriptlets protobufIO

%files
%{_libdir}/libHepMC3.so.3
%license COPYING
%license include/HepMC3/bxzstr/LICENSE

%files devel
%{_bindir}/HepMC3-config
%{_libdir}/libHepMC3.so
%dir %{_includedir}/HeppMC3
%dir %{_includedir}/HeppMC3/bxzstr
%dir %{_includedir}/HeppMC3/Data
%{_includedir}/HeppMC3/bxzstr/bxzstr.hpp
%{_includedir}/HeppMC3/bxzstr/bz_stream_wrapper.hpp
%{_includedir}/HeppMC3/bxzstr/compression_types.hpp
%{_includedir}/HeppMC3/bxzstr/config.hpp
%{_includedir}/HeppMC3/bxzstr/lzma_stream_wrapper.hpp
%{_includedir}/HeppMC3/bxzstr/stream_wrapper.hpp
%{_includedir}/HeppMC3/bxzstr/strict_fstream.hpp
%{_includedir}/HeppMC3/bxzstr/zstd_stream_wrapper.hpp
%{_includedir}/HeppMC3/bxzstr/z_stream_wrapper.hpp
%{_includedir}/HeppMC3/AssociatedParticle.h
%{_includedir}/HeppMC3/Attribute.h
%{_includedir}/HeppMC3/CompressedIO.h
%{_includedir}/HeppMC3/Data/GenEventData.h
%{_includedir}/HeppMC3/Data/GenParticleData.h
%{_includedir}/HeppMC3/Data/GenRunInfoData.h
%{_includedir}/HeppMC3/Data/GenVertexData.h
%{_includedir}/HeppMC3/Errors.h
%{_includedir}/HeppMC3/FourVector.h
%{_includedir}/HeppMC3/GenCrossSection.h
%{_includedir}/HeppMC3/GenCrossSection_fwd.h
%{_includedir}/HeppMC3/GenEvent.h
%{_includedir}/HeppMC3/GenHeavyIon.h
%{_includedir}/HeppMC3/GenHeavyIon_fwd.h
%{_includedir}/HeppMC3/GenParticle.h
%{_includedir}/HeppMC3/GenParticle_fwd.h
%{_includedir}/HeppMC3/GenPdfInfo.h
%{_includedir}/HeppMC3/GenPdfInfo_fwd.h
%{_includedir}/HeppMC3/GenRunInfo.h
%{_includedir}/HeppMC3/GenVertex.h
%{_includedir}/HeppMC3/GenVertex_fwd.h
%{_includedir}/HeppMC3/HEPEVT_Helpers.h
%{_includedir}/HeppMC3/HEPEVT_Wrapper.h
%{_includedir}/HeppMC3/HEPEVT_Wrapper_Runtime.h
%{_includedir}/HeppMC3/HEPEVT_Wrapper_Runtime_Static.h
%{_includedir}/HeppMC3/HEPEVT_Wrapper_Template.h
%{_includedir}/HeppMC3/HepMC3.h
%{_includedir}/HeppMC3/LHEF.h
%{_includedir}/HeppMC3/LHEFAttributes.h
%{_includedir}/HeppMC3/Print.h
%{_includedir}/HeppMC3/PrintStreams.h
%{_includedir}/HeppMC3/Reader.h
%{_includedir}/HeppMC3/ReaderAscii.h
%{_includedir}/HeppMC3/ReaderAsciiHepMC2.h
%{_includedir}/HeppMC3/ReaderFactory.h
%{_includedir}/HeppMC3/ReaderGZ.h
%{_includedir}/HeppMC3/ReaderHEPEVT.h
%{_includedir}/HeppMC3/ReaderLHEF.h
%{_includedir}/HeppMC3/ReaderMT.h
%{_includedir}/HeppMC3/ReaderPlugin.h
%{_includedir}/HeppMC3/Setup.h
%{_includedir}/HeppMC3/Units.h
%{_includedir}/HeppMC3/Version.h
%{_includedir}/HeppMC3/Writer.h
%{_includedir}/HeppMC3/WriterAscii.h
%{_includedir}/HeppMC3/WriterAsciiHepMC2.h
%{_includedir}/HeppMC3/WriterHEPEVT.h
%{_includedir}/HeppMC3/WriterGZ.h
%{_includedir}/HeppMC3/WriterPlugin.h
%dir %{_datadir}/HeppMC3
%dir %{_datadir}/HeppMC3/cmake
%{_datadir}/HeppMC3/cmake/HepMC3Config.cmake
%{_datadir}/HeppMC3/cmake/HepMC3Config-version.cmake
%{_datadir}/HeppMC3/cmake/HepMC3Targets.cmake
%{_datadir}/HeppMC3/cmake/HepMC3Targets-release.cmake

%files search
%{_libdir}/libHepMC3search.so.5

%files search-devel
%{_libdir}/libHepMC3search.so
%{_includedir}/HeppMC3/AttributeFeature.h
%{_includedir}/HeppMC3/Feature.h
%{_includedir}/HeppMC3/Filter.h
%{_includedir}/HeppMC3/FilterAttribute.h
%{_includedir}/HeppMC3/Relatives.h
%{_includedir}/HeppMC3/Selector.h
%{_datadir}/HeppMC3/cmake/HepMC3searchTargets.cmake
%{_datadir}/HeppMC3/cmake/HepMC3searchTargets-release.cmake

%files rootIO
%{_libdir}/root/libHepMC3rootIO.so.3
# unversioned symlink is used at runtime when library is used as a ROOT plugin
%{_libdir}/root/libHepMC3rootIO.so
%{_libdir}/root/libHepMC3rootIO_rdict.pcm
%{_libdir}/root/libHepMC3rootIO.rootmap

%files rootIO-devel
%{_includedir}/HeppMC3/ReaderRoot.h
%{_includedir}/HeppMC3/ReaderRootTree.h
%{_includedir}/HeppMC3/WriterRoot.h
%{_includedir}/HeppMC3/WriterRootTree.h
%{_datadir}/HeppMC3/cmake/HepMC3rootIOTargets.cmake
%{_datadir}/HeppMC3/cmake/HepMC3rootIOTargets-release.cmake

%files protobufIO
%{_libdir}/libHepMC3protobufIO.so.1

%files protobufIO-devel
%{_libdir}/libHepMC3protobufIO.so
%{_includedir}/HeppMC3/Readerprotobuf.h
%{_includedir}/HeppMC3/Writerprotobuf.h
%{_datadir}/HeppMC3/cmake/HepMC3protobufIOTargets.cmake
%{_datadir}/HeppMC3/cmake/HepMC3protobufIOTargets-release.cmake

%files interfaces-devel
%{_datadir}/HeppMC3/interfaces

%if %{?rhel}%{!?rhel:0} == 7
%files -n python2-HeppMC3
%dir %{python2_sitearch}/pyHepMC3
%{python2_sitearch}/pyHepMC3/__init__.py*
%{python2_sitearch}/pyHepMC3/pyHepMC3.so
%{python2_sitearch}/pyHepMC3-*.egg-info
%license python/include/LICENSE

%files -n python2-HeppMC3-search
%dir %{python2_sitearch}/pyHepMC3/search
%{python2_sitearch}/pyHepMC3/search/__init__.py*
%{python2_sitearch}/pyHepMC3/search/pyHepMC3search.so
%{python2_sitearch}/pyHepMC3.search-*.egg-info

%files -n python2-HeppMC3-rootIO
%dir %{python2_sitearch}/pyHepMC3/rootIO
%{python2_sitearch}/pyHepMC3/rootIO/__init__.py*
%{python2_sitearch}/pyHepMC3/rootIO/pyHepMC3rootIO.so
%{python2_sitearch}/pyHepMC3.rootIO-*.egg-info

%files -n python2-HeppMC3-protobufIO
%dir %{python2_sitearch}/pyHepMC3/protobufIO
%{python2_sitearch}/pyHepMC3/protobufIO/__init__.py*
%{python2_sitearch}/pyHepMC3/protobufIO/pyHepMC3protobufIO.so
%{python2_sitearch}/pyHepMC3.protobufIO-*.egg-info

%files -n python%{?python3_other_pkgversion}-HeppMC3
%dir %{python3_other_sitearch}/pyHepMC3
%{python3_other_sitearch}/pyHepMC3/__init__.py
%{python3_other_sitearch}/pyHepMC3/__pycache__
%{python3_other_sitearch}/pyHepMC3/pyHepMC3.so
%{python3_other_sitearch}/pyHepMC3-*.egg-info
%license python/include/LICENSE

%files -n python%{?python3_other_pkgversion}-HeppMC3-search
%dir %{python3_other_sitearch}/pyHepMC3/search
%{python3_other_sitearch}/pyHepMC3/search/__init__.py
%{python3_other_sitearch}/pyHepMC3/search/__pycache__
%{python3_other_sitearch}/pyHepMC3/search/pyHepMC3search.so
%{python3_other_sitearch}/pyHepMC3.search-*.egg-info

%files -n python%{?python3_other_pkgversion}-HeppMC3-rootIO
%dir %{python3_other_sitearch}/pyHepMC3/rootIO
%{python3_other_sitearch}/pyHepMC3/rootIO/__init__.py
%{python3_other_sitearch}/pyHepMC3/rootIO/__pycache__
%{python3_other_sitearch}/pyHepMC3/rootIO/pyHepMC3rootIO.so
%{python3_other_sitearch}/pyHepMC3.rootIO-*.egg-info

%files -n python%{?python3_other_pkgversion}-HeppMC3-protobufIO
%dir %{python3_other_sitearch}/pyHepMC3/protobufIO
%{python3_other_sitearch}/pyHepMC3/protobufIO/__init__.py
%{python3_other_sitearch}/pyHepMC3/protobufIO/__pycache__
%{python3_other_sitearch}/pyHepMC3/protobufIO/pyHepMC3protobufIO.so
%{python3_other_sitearch}/pyHepMC3.protobufIO-*.egg-info
%endif

%files -n python%{python3_pkgversion}-HeppMC3
%dir %{python3_sitearch}/pyHepMC3
%{python3_sitearch}/pyHepMC3/__init__.py
%{python3_sitearch}/pyHepMC3/__pycache__
%{python3_sitearch}/pyHepMC3/pyHepMC3.so
%{python3_sitearch}/pyHepMC3-*.egg-info
%license python/include/LICENSE

%files -n python%{python3_pkgversion}-HeppMC3-search
%dir %{python3_sitearch}/pyHepMC3/search
%{python3_sitearch}/pyHepMC3/search/__init__.py
%{python3_sitearch}/pyHepMC3/search/__pycache__
%{python3_sitearch}/pyHepMC3/search/pyHepMC3search.so
%{python3_sitearch}/pyHepMC3.search-*.egg-info

%files -n python%{python3_pkgversion}-HeppMC3-rootIO
%dir %{python3_sitearch}/pyHepMC3/rootIO
%{python3_sitearch}/pyHepMC3/rootIO/__init__.py
%{python3_sitearch}/pyHepMC3/rootIO/__pycache__
%{python3_sitearch}/pyHepMC3/rootIO/pyHepMC3rootIO.so
%{python3_sitearch}/pyHepMC3.rootIO-*.egg-info

%files -n python%{python3_pkgversion}-HeppMC3-protobufIO
%dir %{python3_sitearch}/pyHepMC3/protobufIO
%{python3_sitearch}/pyHepMC3/protobufIO/__init__.py
%{python3_sitearch}/pyHepMC3/protobufIO/__pycache__
%{python3_sitearch}/pyHepMC3/protobufIO/pyHepMC3protobufIO.so
%{python3_sitearch}/pyHepMC3.protobufIO-*.egg-info

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/examples
%{_pkgdocdir}/html
%license COPYING

%changelog
* Wed Oct 04 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.7-1
- Update to version 3.2.7

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.2.6-2
- Rebuilt for Python 3.12

* Wed Apr 12 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.6-1
- Update to version 3.2.6
- Update license tag for license change (GPLv3 to LGPLv3)
- New protobuf IO subpackage
- Soname bump for libHepMC3search in HepMC3-search subpackage
- Drop patches accepted upstream or previously backported

* Tue Mar 21 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.5-7
- Rebuild for root 6.28
- Fix Python 3.12 build

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.5-4
- Rebuilt for Python 3.11

* Tue Apr 05 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.5-3
- Rebuild for root 6.26

* Tue Feb 22 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.5-2
- Fix detection of installed Pythia HepMC3 interface
- Fix endian issue in HEPEVT wrappers
- Fix doxygen markup syntax

* Mon Feb 21 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.5-1
- Update to version 3.2.5
- Update License tag for bxzstr

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.4-3
- Rebuild for root 6.24.02
- Build rootIO module also for s390x
- Reenable valgrind tests

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.4-1
- Update to version 3.2.4
- Drop patches accepted upstream or previously backported

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.3-4
- Rebuilt for Python 3.10

* Tue Apr 06 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.3-3
- Rebuild for root 6.22.08

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.3-1
- Update to version 3.2.3
- Use new cmake rpm macro also for EPEL
- Fix compilation warnings
- Fix build for multiple python versions (EPEL 7) - fix from upstream git

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.2-3
- Adapt to new cmake rpm macro

* Tue Jul 14 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.2-2
- Rebuild for root 6.22.00

* Wed Jun 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.2-1
- Update to version 3.2.2
- Drop patches accepted upstream or previously backported
- Drop the memory reduction on ARM patch - no longer needed since the
  python module sources were split into multiple files
- Use new cmake configuration option -DHEPMC3_INSTALL_EXAMPLES and
  simplify spec file accordingly
- Bump soname for libHepMC3search.so (3 to 4)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-3
- Rebuilt for Python 3.9

* Sun Mar 29 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.1-2
- Initialize ROOT in rootIO python bindings - avoids problem on EPEL 7 ppc64le
- Use upstream's fix for parallel python tests

* Sun Mar 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.1-1
- Update to version 3.2.1
- Drop patches accepted upstream or previously backported
- Fix glitches in the generation of the HepMC3-config script
- Add additional Python 3 version package for EPEL 7
  (cmake configuration now supports multiple Python 3 versions)
- Use new cmake configuration options -DHEPMC3_ROOTIO_INSTALL_LIBDIR and
  -DHEPMC3_BUILD_STATIC_LIBS and simplify spec file accordingly
- .egg-info filenames are now correct - auto generated provides work

* Tue Jan 28 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.0-3
- Add Python 3.9 as a valid Python version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.0-1
- Update to version 3.2.0
- Add Python packages
- Reduce memory usage when building Python bindings on ARM

* Sat Aug 31 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.2-1
- Update to version 3.1.2
- Drop patches accepted upstream or previously backported

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.1-2
- Rebuild for root 6.18.00

* Fri Apr 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.1-1
- Update to version 3.1.1
- Drop patches accepted upstream or previously backported
- Fix warnings about misleading indentation
- Add missing space in installed cmake file

* Tue Mar 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.0-3
- Rename interfaces subpackage to interfaces-devel
- Add patch fixing installed cmake file from upstream
- Increase test timeout

* Tue Mar 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.0-2
- Add soversion patch from upstream

* Fri Feb 22 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.0-1
- Initial build
