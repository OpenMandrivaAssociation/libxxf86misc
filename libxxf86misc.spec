%define name		libxxf86misc
%define version		1.0.1
%define release		%mkrel 8

%define major		1
%define libname		%mklibname xxf86misc %{major}
%define develname	%mklibname xxf86misc -d
%define staticname	%mklibname xxf86misc -d -s

Name:		%{name}
Summary:	XFree86 Misc Extension Library
Version:	%{version}
Release:	%{release}
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86misc-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
XFree86 Misc Extension Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  XFree86 Misc Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
XFree86 Misc Extension Library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} >= %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname xxf86misc 1 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXxf86misc.so
%{_libdir}/libXxf86misc.la
%{_libdir}/pkgconfig/xxf86misc.pc
%{_mandir}/man3/XF86Misc*.3*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xxf86misc 1 -d -s}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXxf86misc.a

#-----------------------------------------------------------

%prep
%setup -q -n libXxf86misc-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXxf86misc.so.%{major}*

