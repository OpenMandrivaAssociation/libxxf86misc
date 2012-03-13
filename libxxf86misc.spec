%define name		libxxf86misc
%define version		1.0.3
%define release		%mkrel 2

%define major		1
%define libname		%mklibname xxf86misc %{major}
%define develname	%mklibname xxf86misc -d

Name:		libxxf86misc
Summary:	XFree86 Misc Extension Library
Version:	1.0.3
Release:	3
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86misc-%{version}.tar.bz2

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
XFree86 Misc Extension Library.

%package -n %{libname}
Summary:  XFree86 Misc Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
XFree86 Misc Extension Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} >= %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xxf86misc1-devel
Obsoletes: %{_lib}xxf86misc-static-devel < 1.0.3-3
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXxf86misc-%{version}

%build
%configure2_5x	\
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXxf86misc.so.%{major}*

%files -n %{develname}
%{_libdir}/libXxf86misc.so
%{_libdir}/pkgconfig/xxf86misc.pc
%{_mandir}/man3/XF86Misc*.3*

