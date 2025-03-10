#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module

%define	module	rpdb
Summary:	pdb wrapper with remote access via tcp socket
Name:		python-rpdb
Version:	0.1.3
Release:	13
License:	?
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/r/rpdb/rpdb-%{version}.tar.gz
# Source0-md5:	4f350f523446a9100395d41b0b05c6cb
URL:		https://pypi.python.org/pypi/rpdb/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
Requires:	python
Requires:	python-devel-src
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wrapper around pdb that will re-route stdin and stdout to a socket
handler.

%package -n python3-%{module}
Summary:	pdb wrapper with remote access via tcp socket
Group:		Libraries/Python
Requires:	python3
Requires:	python3-devel-tools

%description -n python3-%{module}
A wrapper around pdb that will re-route stdin and stdout to a socket
handler.

%prep
%setup  -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/rpdb
%{py_sitescriptdir}/rpdb-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc PKG-INFO
%{py3_sitescriptdir}/rpdb
%{py3_sitescriptdir}/rpdb-%{version}-py*.egg-info
%endif
