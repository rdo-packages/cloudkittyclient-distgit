# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%global __python %{__python3}
%else
%global pyver 2
%global __python %{__python2}
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global cname cloudkitty
%global sname %{cname}client
%global with_doc 1

%global common_desc \
python-%{sname} is a command-line client for CloudKitty, the \
Rating-as-a-Service component for OpenStack.

Name:          python-%{sname}
Version:       3.1.0
Release:       1%{?dist}
Summary:       Client library for CloudKitty
License:       ASL 2.0
URL:           http://launchpad.net/%{name}/
Source0:       https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:     noarch

%description
%{common_desc}


%package -n python%{pyver}-%{sname}
Summary:       Client library for CloudKitty
%{?python_provide:%python_provide python%{pyver}-%{sname}}

BuildRequires: python%{pyver}-cliff
BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-pbr
BuildRequires: python%{pyver}-mock
BuildRequires: python%{pyver}-stestr
BuildRequires: python%{pyver}-openstackclient >= 3.14.0
BuildRequires: python%{pyver}-oslo-log >= 3.36
BuildRequires: python%{pyver}-jsonpath-rw-ext
BuildRequires: git

Requires:      python%{pyver}-keystoneauth1 >= 3.4.0
Requires:      python%{pyver}-pbr
Requires:      python%{pyver}-cliff
Requires:      python%{pyver}-oslo-utils >= 3.35
Requires:      python%{pyver}-oslo-log >= 3.36
Requires:      python%{pyver}-openstackclient >= 3.14.0
Requires:      python%{pyver}-jsonpath-rw-ext
Requires:      python%{pyver}-six >= 1.11
Requires:      python%{pyver}-os-client-config
Requires:      python%{pyver}-osc-lib >= 1.12.1

# Handle python2 exception
%if %{pyver} == 2
Requires:      PyYAML
%else
Requires:      python%{pyver}-yaml
%endif

%description -n python%{pyver}-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:       Documentation for the CloudKitty client

BuildRequires: python%{pyver}-sphinx
BuildRequires: python%{pyver}-openstackdocstheme
BuildRequires: python%{pyver}-sphinxcontrib-rsvgconverter

Requires: python%{pyver}-%{sname} = %{version}-%{release}

%description doc
%{common_desc}

This package contains documentation.
%endif
%prep
%autosetup -n %{name}-%{upstream_version} -S git

%build
%{pyver_build}

%if 0%{?with_doc}
# Build html documentation
sphinx-build-%{pyver} -b html doc/source doc/build/html
# Remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyver_install}
mv %{buildroot}%{_bindir}/%{cname} %{buildroot}%{_bindir}/%{cname}-%{python_version}
ln -s %{cname}-%{python_version} %{buildroot}%{_bindir}/%{cname}-%{pyver}
ln -s %{cname}-%{pyver} %{buildroot}%{_bindir}/%{cname}


# Delete tests
rm -fr %{buildroot}%{pyver_sitelib}/%{sname}/tests

%files -n python%{pyver}-%{sname}
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{sname}
%{pyver_sitelib}/*.egg-info
%{_bindir}/%{cname}
%{_bindir}/%{cname}-%{pyver}
%{_bindir}/%{cname}-%{python_version}

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
* Wed Sep 25 2019 RDO <dev@lists.rdoproject.org> 3.1.0-1
- Update to 3.1.0

* Mon Sep 23 2019 RDO <dev@lists.rdoproject.org> 3.0.0-1
- Update to 3.0.0

