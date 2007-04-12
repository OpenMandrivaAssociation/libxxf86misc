%define libxxf86misc %mklibname xxf86misc 1
Name: libxxf86misc
Summary:  XFree86 Misc Extension Library
Version: 1.0.1
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXxf86misc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
XFree86 Misc Extension Library

#-----------------------------------------------------------

%package -n %{libxxf86misc}
Summary:  XFree86 Misc Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxxf86misc}
XFree86 Misc Extension Library

#-----------------------------------------------------------

%package -n %{libxxf86misc}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxxf86misc} >= %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxxf86misc-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxxf86misc}-devel
Development files for %{name}

%files -n %{libxxf86misc}-devel
%defattr(-,root,root)
%{_libdir}/libXxf86misc.so
%{_libdir}/libXxf86misc.la
%{_libdir}/pkgconfig/xxf86misc.pc
%{_mandir}/man3/XF86Misc*.3x.bz2

#-----------------------------------------------------------

%package -n %{libxxf86misc}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxxf86misc}-devel = %{version}
Provides: libxxf86misc-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxxf86misc}-static-devel
Static development files for %{name}

%files -n %{libxxf86misc}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxxf86misc}
%defattr(-,root,root)
%{_libdir}/libXxf86misc.so.1
%{_libdir}/libXxf86misc.so.1.1.0


