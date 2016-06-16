%global pkgname webpy
%global srcname web.py
%bcond_without python2

Name:		python-%{pkgname}
Version:	0.37
Release:	9
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
# Generated by:
# git clone git@github.com:webpy/webpy.git
# git checkout -b python3 origin/python3
# git rebase -i webpy-0.37
# git diff webpy-0.37 >python-webpy-0.37-python3.patch
# vi python-webpy-0.37-python3.patch
# [remove chunks that apply to files that are in the git repository,
# but not in release tarballs]
Patch0:			python-webpy-0.37-python3.patch
BuildRequires:		pkgconfig(python)
BuildArch:		noarch
#Requires:		python-cherrypy
%rename			python-%{pkgname}

%description
web.py is a web framework for python that is as simple as it is
powerful. web.py is in the public domain; you can use it for whatever
purpose with absolutely no restrictions. 

%if %{with python2}
%package -n python2-%{pkgname}
Summary:	A simple web framework for Python
Group:		Development/Python
BuildRequires:	pkgconfig(python2)

%description -n python2-%{pkgname}
web.py is a web framework for python that is as simple as it is
powerful. web.py is in the public domain; you can use it for whatever
purpose with absolutely no restrictions. 
%endif

%prep
%setup -qcn web.py-%{version}

chmod 0755 web.py-%{version}/web/wsgiserver/ssl_builtin.py
chmod 0755 web.py-%{version}/web/wsgiserver/ssl_pyopenssl.py
chmod 0755 web.py-%{version}/web/wsgiserver/__init__.py

%if %{with python2}
cp -a web.py-%{version} python2
%endif

cd web.py-%{version}
%patch0 -p1 -b .py3~

%build
cd web.py-%{version}
%{__python} setup.py build

%if %{with python2}
cd ../python2
%{__python2} setup.py build
%endif

%install
cd web.py-%{version}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%if %{with python2}
cd ../python2
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%endif

%files
%doc web.py-%{version}/PKG-INFO
%{python_sitelib}/web
%{python_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%files -n python2-%{pkgname}
%doc python2/PKG-INFO
%{python2_sitelib}/web
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info
