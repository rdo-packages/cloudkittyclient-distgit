%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname cloudkittyclient

%if 0%{?fedora}
%global with_python3 1
%endif

Name:          python-cloudkittyclient
Version:       0.6.0
Release:       1%{?dist}
Summary:       Client library for CloudKitty
License:       ASL 2.0
URL:           http://launchpad.net/%{name}/
Source0:       http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:     noarch

%description
python-cloudkittyclient is a command-line client for CloudKitty, the
Rating-as-a-Service component for OpenStack.

%package -n python2-%{sname}
Summary:       Client library for CloudKitty
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr

Requires:      python-keystoneclient
Requires:      python-stevedore
Requires:      python-babel
Requires:      python-pbr
Requires:      python-babel
Requires:      python-oslo-i18n
Requires:      python-oslo-serialization
Requires:      python-oslo-utils
Requires:      python-prettytable

%description -n python2-%{sname}
python-cloudkittyclient is a command-line client for CloudKitty, the
Rating-as-a-Service component for OpenStack.

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:       Client library for CloudKitty
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires:      python3-keystoneclient
Requires:      python3-stevedore
Requires:      python3-babel
Requires:      python3-pbr
Requires:      python3-babel
Requires:      python3-oslo-i18n
Requires:      python3-oslo-serialization
Requires:      python3-oslo-utils
Requires:      python3-prettytable

%description -n python3-%{sname}
python-cloudkittyclient is a command-line client for CloudKitty, the
Rating-as-a-Service component for OpenStack.
%endif

%package doc
Summary:       Documentation for the CloudKitty client

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx

Requires: %{name} = %{version}-%{release}

%description doc
python-cloudkittyclient is a command-line client for CloudKitty, the
Rating-as-a-Service component for OpenStack.

%prep
%setup -q -n %{name}-%{upstream_version}

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

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html


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
%doc html
%license LICENSE

%changelog
* Tue Sep 13 2016 Haikel Guemar <hguemar@fedoraproject.org> 0.6.0-1
- Update to 0.6.0

