Name:           python-mpd2
Version:        3.1.1
Release:        2
Summary:        Python bindings for MPD
Group:          Development/Python
License:        GPLv2
URL:            https://github.com/Mic92/python-mpd2
Source0:        https://github.com/Mic92/python-mpd2/archive/python-mpd2-%{version}.tar.gz
BuildArch:	    noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)


%description
An MPD (Music Player Daemon) client library written in pure Python.

%prep
%setup -q

%build
%py_build

%install
%py_install

%files
%doc LICENSE.txt README.rst
%{python_sitelib}/*
