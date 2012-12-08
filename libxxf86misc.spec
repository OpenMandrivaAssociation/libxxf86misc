%define name		libxxf86misc
%define version		1.0.3
%define release		4

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
Obsoletes: %{mklibname xxf86misc 1 -d} < 1.0.3-4

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXxf86misc.so
%{_libdir}/pkgconfig/xxf86misc.pc
%{_mandir}/man3/XF86Misc*.3*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xxf86misc 1 -d -s} < 1.0.3-4

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

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXxf86misc.so.%{major}*


%changelog
* Thu Aug 7 2011 Akdengi <akdengi> 1.0.4-4
- drop .la
- fix Obsoletes

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 660307
- mass rebuild

* Mon Nov 22 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 599630
- new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 464051
- New version: 1.0.2

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-8mdv2010.0
+ Revision: 425974
- rebuild

* Sun Nov 09 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.1-7mdv2009.1
+ Revision: 301208
- rebuild for new xcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 223091
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 153300
- Update BuildRequires and rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 75081
- obsolete old -static-devel package
- complete spec clean

* Fri Aug 17 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-2mdv2008.0
+ Revision: 64692
- rebuild for 2008
- new devel policy
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

