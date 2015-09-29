#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Tempita
Version  : 0.5.2
Release  : 11
URL      : https://pypi.python.org/packages/source/T/Tempita/Tempita-0.5.2.tar.gz
Source0  : https://pypi.python.org/packages/source/T/Tempita/Tempita-0.5.2.tar.gz
Summary  : A very small text templating language
Group    : Development/Tools
License  : MIT
Requires: Tempita-python
BuildRequires : nose-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the Tempita package.
Group: Default

%description python
python components for the Tempita package.


%prep
%setup -q -n Tempita-0.5.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
