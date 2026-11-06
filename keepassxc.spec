Summary:	Cross Platform Password Manager
Name:		keepassxc
Version:	2.8.0
Release:	%{?beta:0.%{beta}.}2
License:	GPLv2+
Group:		File tools
# Forked from dormant http://www.keepassx.org/
Url:		https://www.keepassxc.org/
%if ! 0%{?beta:1}
Source0:	https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
%else
Source0:	https://github.com/keepassxreboot/keepassxc/archive/master/%{name}-%{version}-%{beta}.tar.gz
%endif
BuildRequires:		asciidoctor
BuildRequires:		cmake >= 3.16
BuildRequires:		ninja
BuildRequires:		cmake(Qt6Core)
BuildRequires:		cmake(Qt6Concurrent)
BuildRequires:		cmake(Qt6DBus)
BuildRequires:		cmake(Qt6Gui)
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		cmake(Qt6Network)
BuildRequires:		cmake(Qt6Svg)
BuildRequires:		cmake(Qt6SvgWidgets)
BuildRequires:		cmake(Qt6Widgets)
BuildRequires:		cmake(Qt6Test)
BuildRequires:		pkgconfig(botan-3)
BuildRequires:		pkgconfig(libqrencode)
BuildRequires:		pkgconfig(libkeyutils)
BuildRequires:		pkgconfig(xkbcommon)
## The following two BuildRequires added for yubikey support
BuildRequires:		pkgconfig(libpcsclite)
BuildRequires:		pkgconfig(libusb)
BuildRequires:		pkgconfig(minizip)
BuildRequires:		pkgconfig(readline)
BuildRequires:		pkgconfig(xi)
BuildRequires:		pkgconfig(xtst)
BuildRequires:		pkgconfig(zlib)
Provides:	keepass = %{version}-%{release}
Provides:	KeePassX = %{version}-%{release}
Provides:	KeePassXC = %{version}-%{release}
%rename keepassx

%description
KeePassXC is a free/open-source password manager or safe which helps you to
manage your passwords in a secure way. You can put all your passwords in one
database, which is locked with one master key or a key-disk. So you only have
to remember one single master password or insert the key-disk to unlock the
whole database. The databases are encrypted using the best and most secure
encryption algorithms currently known (AES and Twofish).

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-proxy
%{_datadir}/%{name}/
%{_datadir}/applications/org.%{name}.KeePassXC.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/org.%{name}.KeePassXC.appdata.xml
%{_datadir}/polkit-1/actions/org.%{name}.KeePassXC.policy
%{_iconsdir}/hicolor/*/apps/%{name}*.*
%{_iconsdir}/hicolor/*/mimetypes/*.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-cli.1*

#-----------------------------------------------------------------------------

%package cli
Summary:	CLI interface to the KeePassXC password manager
Group:		File tools

%description cli
Command Line Interface to the KeePassXC password manager.

#-----------------------------------------------------------------------------

%prep
%if 0%{?beta}
%autosetup -p1 -n %{name}-master
%else
%autosetup -p1
%endif
%cmake -G Ninja \
	-DKEEPASSXC_BUILD_TYPE=Release \
	-DKPXC_FEATURE_BROWSER:BOOL=ON \
	-DKPXC_FEATURE_FDOSECRETS:BOOL=ON \
	-DKPXC_FEATURE_NETWORK:BOOL=ON \
	-DKPXC_FEATURE_SSHAGENT:BOOL=ON \
	-DKPXC_FEATURE_UPDATES:BOOL=OFF \
	-DKPXC_FEATURE_DOCS:BOOL=ON


%build
%ninja_build -C build


%install
%ninja_install -C build
