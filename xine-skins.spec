%define name xine-skins
#gw The package version is the skin.version in the skinconfig file
#gw TODO, next time, remove the .0 to match the skin.version
%define version 5.0
%define release 9

Summary: Skins for Xine
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %name-%version.tar.bz2
License: GPL
Group: Video
Url: http://xinehq.de/index.php/skins
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: xine-ui >= 0.99.1-4mdk
BuildArch: noarch

%description
This package contains additional skins for the Xine UI.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_datadir/xine/skins
for skin in *.tar.gz;do tar xzf $skin -C %buildroot%_datadir/xine/skins
done

#gw remove skin sources
rm -rf %buildroot%_datadir/xine/skins/*/src/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %dir %_datadir/xine/skins/*
%attr(644,root,root) %dir %_datadir/xine/skins/*/*


%changelog
* Tue Jul 26 2011 GÃ¶tz Waschk <waschk@mandriva.org> 5.0-8mdv2012.0
+ Revision: 691698
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 5.0-7mdv2011.0
+ Revision: 242993
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 5.0-5mdv2008.0
+ Revision: 57478
- Import xine-skins



* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 5.0-1mdv2007.0
- Rebuild

* Sun May 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 5.0-4mdk
- Rebuild
- use mkrel

* Fri May 20 2005 Götz Waschk <waschk@mandriva.org> 5.0-3mdk
- add more skins

* Mon May 10 2004 Götz Waschk <waschk@linux-mandrake.com> 5.0-2mdk
- fix Bug 9734

* Tue May  4 2004 Götz Waschk <waschk@linux-mandrake.com> 5.0-1mdk
- initial package
