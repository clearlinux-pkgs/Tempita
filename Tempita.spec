#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Tempita
Version  : 0.5.2
Release  : 43
URL      : https://pypi.python.org/packages/source/T/Tempita/Tempita-0.5.2.tar.gz
Source0  : https://pypi.python.org/packages/source/T/Tempita/Tempita-0.5.2.tar.gz
Summary  : A very small text templating language
Group    : Development/Tools
License  : MIT
Requires: Tempita-python = %{version}-%{release}
Requires: Tempita-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nose

%description
This isn't meant to be the Next Big Thing in templating; it's just a
        handy little templating language for when your project outgrows
        ``string.Template`` or ``%`` substitution.  It's small, it embeds
        Python in strings, and it doesn't do much else.
        
        You can read about the `language

%package python
Summary: python components for the Tempita package.
Group: Default
Requires: Tempita-python3 = %{version}-%{release}
Provides: tempita-python

%description python
python components for the Tempita package.


%package python3
Summary: python3 components for the Tempita package.
Group: Default
Requires: python3-core
Provides: pypi(tempita)

%description python3
python3 components for the Tempita package.


%prep
%setup -q -n Tempita-0.5.2
cd %{_builddir}/Tempita-0.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583523671
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
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
