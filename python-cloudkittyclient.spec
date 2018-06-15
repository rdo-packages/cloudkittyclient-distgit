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

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pbr

Requires:      python2-keystoneclient >= 1:3.8.0
Requires:      python2-stevedore
Requires:      python2-babel
Requires:      python2-pbr
Requires:      git
Requires:      python2-babel
Requires:      python2-oslo-i18n >= 2.1.0
Requires:      python2-oslo-serialization >= 1.10.0
Requires:      python2-oslo-utils >= 3.20.0
Requires:      python2-prettytable
Requires:      python2-openstackclient >= 3.3.0

%description -n python2-%{sname}
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:       Client library for CloudKitty
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires:      python3-keystoneclient >= 1:3.8.0
Requires:      python3-stevedore
Requires:      python3-babel
Requires:      python3-pbr
Requires:      python3-babel
Requires:      python3-oslo-i18n >= 2.1.0
Requires:      python3-oslo-serialization >= 1.10.0
Requires:      python3-oslo-utils >= 3.20.0
Requires:      python3-prettytable
Requires:      python3-openstackclient >= 3.3.0

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

%{__python2} setup.py build_sphinx -b html

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
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/python-cloudkittyclient/commit/?id=d070f6a68cddf51c57e77107f1b823a8f75770ba
