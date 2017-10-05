#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wcwidth
Version  : 0.1.7
Release  : 7
URL      : http://pypi.debian.net/wcwidth/wcwidth-0.1.7.tar.gz
Source0  : http://pypi.debian.net/wcwidth/wcwidth-0.1.7.tar.gz
Summary  : Measures number of Terminal column cells of wide-character codes
Group    : Development/Tools
License  : MIT
Requires: wcwidth-legacypython
Requires: wcwidth-python3
Requires: wcwidth-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/travis/jquast/wcwidth.svg
:target: https://travis-ci.org/jquast/wcwidth
:alt: Travis Continous Integration

%package legacypython
Summary: legacypython components for the wcwidth package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the wcwidth package.


%package python
Summary: python components for the wcwidth package.
Group: Default
Requires: wcwidth-legacypython
Requires: wcwidth-python3

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507180875
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1507180875
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
