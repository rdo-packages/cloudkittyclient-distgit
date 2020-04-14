
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global cname cloudkitty
%global sname %{cname}client
%global with_doc 1

%global common_desc \
python-%{sname} is a command-line client for CloudKitty, the \
Rating-as-a-Service component for OpenStack.

Name:          python-%{sname}
Version:       XXX
Release:       XXX
Summary:       Client library for CloudKitty
License:       ASL 2.0
URL:           http://launchpad.net/%{name}/
Source0:       https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:     noarch

%description
%{common_desc}


%package -n python3-%{sname}
Summary:       Client library for CloudKitty
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-cliff
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
BuildRequires: python3-mock
BuildRequires: python3-stestr
BuildRequires: python3-openstackclient >= 3.14.0
BuildRequires: python3-oslo-log >= 3.36
BuildRequires: python3-jsonpath-rw-ext
BuildRequires: git

Requires:      python3-keystoneauth1 >= 3.4.0
Requires:      python3-pbr
Requires:      python3-cliff
Requires:      python3-oslo-utils >= 3.35
Requires:      python3-oslo-log >= 3.36
Requires:      python3-jsonpath-rw-ext
Requires:      python3-six >= 1.11
Requires:      python3-os-client-config
Requires:      python3-osc-lib >= 1.12.1

Requires:      python3-yaml

%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:       Documentation for the CloudKitty client

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme
BuildRequires: python3-sphinxcontrib-rsvgconverter

Requires: python3-%{sname} = %{version}-%{release}

%description doc
%{common_desc}

This package contains documentation.
%endif
%prep
%autosetup -n %{name}-%{upstream_version} -S git

%build
%{py3_build}

%if 0%{?with_doc}
# Build html documentation
sphinx-build -b html doc/source doc/build/html
# Remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}
mv %{buildroot}%{_bindir}/%{cname} %{buildroot}%{_bindir}/%{cname}-%{python3_version}
ln -s %{cname}-%{python3_version} %{buildroot}%{_bindir}/%{cname}-3
ln -s %{cname}-3 %{buildroot}%{_bindir}/%{cname}


# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{sname}
%{python3_sitelib}/*.egg-info
%{_bindir}/%{cname}
%{_bindir}/%{cname}-3
%{_bindir}/%{cname}-%{python3_version}

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
