%define name xine-skins
#gw The package version is the skin.version in the skinconfig file
#gw TODO, next time, remove the .0 to match the skin.version
%define version 5.0
%define release %mkrel 5

Summary: Skins for Xine
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %name-%version.tar.bz2
License: GPL
Group: Video
Url: http://xinehq.de/index.php/skins
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
