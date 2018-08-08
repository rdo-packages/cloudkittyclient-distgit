%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname cloudkittyclient

%if 0%{?fedora}
%global with_python3 1
%endif

%global common_desc \
python-cloudkittyclient is a command-line client for CloudKitty, the \
Rating-as-a-Service component for OpenStack.

Name:          python-cloudkittyclient
Version:       XXX
Release:       XXX
Summary:       Client library for CloudKitty
License:       ASL 2.0
URL:           http://launchpad.net/%{name}/
Source0:       https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:     noarch

%description
%{common_desc}


%package -n python2-%{sname}
Summary:       Client library for CloudKitty
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires: python2-cliff
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pbr
BuildRequires: python2-mock
BuildRequires: python2-stestr
BuildRequires: python2-openstackclient >= 3.14.0
BuildRequires: python2-oslo-log >= 3.36
BuildRequires: python2-jsonpath-rw-ext

Requires:      python2-keystoneauth1 >= 3.4.0
Requires:      python2-pbr
Requires:      python2-cliff
Requires:      git
Requires:      PyYAML
Requires:      python2-oslo-utils >= 3.35
Requires:      python2-oslo-log >= 3.36
Requires:      python2-openstackclient >= 3.14.0
Requires:      python2-jsonpath-rw-ext
Requires:      python2-six >= 1.11
Requires:      python2-os-client-config

%description -n python2-%{sname}
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:       Client library for CloudKitty
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
BuildRequires: python3-cliff
BuildRequires: python3-mock
BuildRequires: python3-stestr
BuildRequires: python3-openstackclient >= 3.14.0
BuildRequires: python3-oslo-log >= 3.36
BuildRequires: python3-jsonpath-rw-ext

Requires:      python3-keystoneauth1 >= 3.4.0
Requires:      python3-pbr
Requires:      python3-cliff
Requires:      python3-PyYAML
Requires:      python3-oslo-utils >= 3.35
Requires:      python3-oslo-log >= 3.36
Requires:      python3-openstackclient >= 3.14.0
Requires:      python3-jsonpath-rw-ext
Requires:      python3-six >= 1.11
Requires:      python3-os-client-config

%description -n python3-%{sname}
%{common_desc}
%endif

%package doc
Summary:       Documentation for the CloudKitty client

BuildRequires: python2-sphinx
BuildRequires: python2-openstackdocstheme

Requires: %{name} = %{version}-%{release}

%description doc
%{common_desc}

This package contains documentation.
%prep
%autosetup -n %{name}-%{upstream_version} -S git

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# Build html documentation
sphinx-build -b html doc/source doc/build/html
# Remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/cloudkitty %{buildroot}%{_bindir}/cloudkitty-%{python3_version}
ln -s ./cloudkitty-%{python3_version} %{buildroot}%{_bindir}/cloudkitty-3
# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/%{sname}/tests
%endif

%py2_install
mv %{buildroot}%{_bindir}/cloudkitty %{buildroot}%{_bindir}/cloudkitty-%{python2_version}
ln -s ./cloudkitty-%{python2_version} %{buildroot}%{_bindir}/cloudkitty-2

ln -s ./cloudkitty-2 %{buildroot}%{_bindir}/cloudkitty

# Delete tests
rm -fr %{buildroot}%{python2_sitelib}/%{sname}/tests

%files -n python2-%{sname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{sname}
%{python2_sitelib}/*.egg-info
%{_bindir}/cloudkitty
%{_bindir}/cloudkitty-2
%{_bindir}/cloudkitty-%{python2_version}

%if 0%{?with_python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/*.egg-info
%{_bindir}/cloudkitty-3
%{_bindir}/cloudkitty-%{python3_version}
%endif

%files doc
%doc doc/build/html
%license LICENSE

%changelog
