#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wcwidth
Version  : 0.1.7
Release  : 23
URL      : http://pypi.debian.net/wcwidth/wcwidth-0.1.7.tar.gz
Source0  : http://pypi.debian.net/wcwidth/wcwidth-0.1.7.tar.gz
Summary  : Measures number of Terminal column cells of wide-character codes
Group    : Development/Tools
License  : MIT
Requires: wcwidth-license = %{version}-%{release}
Requires: wcwidth-python = %{version}-%{release}
Requires: wcwidth-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/travis/jquast/wcwidth.svg
:target: https://travis-ci.org/jquast/wcwidth
:alt: Travis Continous Integration

%package license
Summary: license components for the wcwidth package.
Group: Default

%description license
license components for the wcwidth package.


%package python
Summary: python components for the wcwidth package.
Group: Default
Requires: wcwidth-python3 = %{version}-%{release}

%description python
python components for the wcwidth package.


%package python3
Summary: python3 components for the wcwidth package.
Group: Default
Requires: python3-core

%description python3
python3 components for the wcwidth package.


%prep
%setup -q -n wcwidth-0.1.7
cd %{_builddir}/wcwidth-0.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574206977
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wcwidth
cp %{_builddir}/wcwidth-0.1.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/wcwidth/bc884d01243a5f1fd86b44ec9e33e276a3c10dc6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wcwidth/bc884d01243a5f1fd86b44ec9e33e276a3c10dc6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
