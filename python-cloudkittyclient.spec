%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:     noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

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
BuildRequires: git-core

Requires:      python3-keystoneauth1 >= 4.3.0
Requires:      python3-pbr
Requires:      python3-cliff >= 3.5.0
Requires:      python3-oslo-utils >= 4.7.0
Requires:      python3-oslo-log >= 4.4.0
Requires:      python3-jsonpath-rw-ext >= 1.2.0
Requires:      python3-os-client-config >= 2.1.0
Requires:      python3-osc-lib >= 2.3.0

Requires:      python3-yaml >= 5.3.1

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
