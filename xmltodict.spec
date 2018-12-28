#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmltodict
Version  : 0.11.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/57/17/a6acddc5f5993ea6eaf792b2e6c3be55e3e11f3b85206c818572585f61e1/xmltodict-0.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/17/a6acddc5f5993ea6eaf792b2e6c3be55e3e11f3b85206c818572585f61e1/xmltodict-0.11.0.tar.gz
Summary  : Makes working with XML feel like you are working with JSON
Group    : Development/Tools
License  : MIT
Requires: xmltodict-python3
Requires: xmltodict-python
BuildRequires : buildreq-distutils3

%description
# xmltodict
`xmltodict` is a Python module that makes working with XML feel like you are working with [JSON](http://docs.python.org/library/json.html), as in this ["spec"](http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html):

%package python
Summary: python components for the xmltodict package.
Group: Default
Requires: xmltodict-python3

%description python
python components for the xmltodict package.


%package python3
Summary: python3 components for the xmltodict package.
Group: Default
Requires: python3-core

%description python3
python3 components for the xmltodict package.


%prep
%setup -q -n xmltodict-0.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534858462
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
