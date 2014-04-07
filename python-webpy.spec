%global pkgname webpy
%global srcname web.py

Name:		python-%{pkgname}
Version:	0.37
Release:	2
Summary:	A simple web framework for Python
Group:		Development/Python

# The entire source code is Public Domain save for the following exceptions:
#   web/debugerror.py (Modified BSD)
#     This is from django
#     See http://code.djangoproject.com/browser/django/trunk/LICENSE
#   web/httpserver.py (Modified BSD)
#     This is from WSGIUtils/lib/wsgiutils/wsgiServer.py
#     See http://www.xfree86.org/3.3.6/COPYRIGHT2.html#5
License:		Public Domain and BSD

URL:			http://webpy.org/
Source0:		http://webpy.org/static/%{srcname}-%{version}.tar.gz
BuildRequires:	python2-devel
BuildArch:		noarch
Requires:		python-cherrypy

%description
web.py is a web framework for python that is as simple as it is
powerful. web.py is in the public domain; you can use it for whatever
purpose with absolutely no restrictions. 

%prep
%setup -q -n web.py-%{version}
rm web/wsgiserver/ssl_builtin.py
rm web/wsgiserver/ssl_pyopenssl.py
rm web/wsgiserver/__init__.py
echo "from cherrypy.wsgiserver import *" >> web/wsgiserver/__init__.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc PKG-INFO
%{python_sitelib}/web
%{python_sitelib}/%{srcname}-%{version}-py?.?.egg-info
