Name:		libusbg
Version:	0.1.0
Release:	0
License:	LGPL-2.1+ and GPL-2.0+
Summary: 	USB gadget with ConfigFS Library
Group:		Base/Device Management

Source0:	libusbg-%{version}.tar.gz
Source1001:	libusbg.manifest
BuildRequires:	pkg-config

%description
Libusbg is a librarary for all USB gadget operations using ConfigFS.

%package devel
Summary: 	USB gadget with ConfigFS Library
Group:		Development/Libraries
Requires:	glibc-devel
Requires:	%{name} = %{version}-%{release}

%description devel
Development package for libusbg. Contains headers and binaries required for
compilation of applications which use libusbg.

%package examples
Summary:	Examples of libusbg usage
Group:		Applications/Other
Requires: 	%{name} = %{version}-%{release}

%description examples
Sample applications which shows how to use libusbg.

%prep
%setup -q
cp %{SOURCE1001} .
%reconfigure

%build
make

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING COPYING.LGPL
%{_libdir}/libusbg.so.*
%{_libdir}/libusbg.so.*.*.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/usbg/usbg.h
%{_libdir}/pkgconfig/libusbg.pc
%{_libdir}/libusbg.so

%files examples
%manifest %{name}.manifest
%{_bindir}/gadget-acm-ecm
%{_bindir}/show-gadgets

%changelog
