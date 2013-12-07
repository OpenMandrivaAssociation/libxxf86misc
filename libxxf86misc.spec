%define major	1
%define libname	%mklibname xxf86misc %{major}
%define devname	%mklibname xxf86misc -d

Summary:	XFree86 Misc Extension Library
Name:		libxxf86misc
Version:	1.0.3
Release:	9
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86misc-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xproto) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1

%description
XFree86 Misc Extension Library.

%package -n %{libname}
Summary:	XFree86 Misc Extension Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
XFree86 Misc Extension Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -qn libXxf86misc-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXxf86misc.so.%{major}*

%files -n %{devname}
%{_libdir}/libXxf86misc.so
%{_libdir}/pkgconfig/xxf86misc.pc
%{_mandir}/man3/XF86Misc*.3*

