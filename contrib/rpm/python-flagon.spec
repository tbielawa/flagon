# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%global _pkg_name flagon
%global _short_release 1

Name:           python-flagon
Version:        0.0.1
Release:        %{_short_release}%{?dist}
Summary:        Feature flags for python

License:        MIT
URL:            https://github.com/ashcrow/flagon
Source0:        %{version}-%{_short_release}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools


%description
Generic feature flags for Python which attempts to be compatible with
Java's Togglz.

%prep
%setup -q -n %{_pkg_name}-%{version}-%{_short_release}

%build
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT

%files
%doc README.md LICENSE AUTHORS example CONTRIBUTING.md
%{python2_sitelib}/*

%changelog
* Tue Jun 10 2014 Tim Bielawa <tbielawa@redhat.com> - 0.0.1-1
- First release
