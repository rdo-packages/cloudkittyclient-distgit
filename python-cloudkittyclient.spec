%{!?upstream_version: %global upstream_version %{version}}

Name:          python-cloudkittyclient
Version:       0.5.0
Release:       1%{?dist}
Summary:       Client library for CloudKitty
License:       ASL 2.0
URL:           http://github.com/openstack/%{name}
Source0:       http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}%{?milestone}.tar.gz

BuildArch:     noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-keystoneclient
BuildRequires: python-stevedore
BuildRequires: python-babel

Provides:      python-cloudkittyclient = %{upstream_version}

Requires:      python-keystoneclient
Requires:      python-stevedore
Requires:      python-babel

%description
python-cloudkittyclient is a command-line client for CloudKitty, the
Rating-as-a-Service component for OpenStack.

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
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

sphinx-build -b html doc/source html

%files
%license LICENSE
%doc README.rst
%{_bindir}/cloudkitty
%{python2_sitelib}/cloudkittyclient
%{python2_sitelib}/python_cloudkittyclient-%{upstream_version}-py?.?.egg-info

%files doc
%license LICENSE
%doc html

%changelog
* Wed Mar 23 2016 RDO <rdo-list@redhat.com> 0.5.0-0.1
-  Rebuild for Mitaka 
