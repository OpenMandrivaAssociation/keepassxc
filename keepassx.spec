%define pre 20190923

Summary:	Cross Platform Password Manager
Name:		keepassx
Version:	2.0.4
%if 0%{?pre}
Release:	0.%{pre}.1
Source0:	https://github.com/keepassx/keepassx/archive/master.tar.gz
%else
Release:	1
Source0:	https://www.keepassx.org/releases/%{version}/keepassx-%{version}.tar.gz
%endif
License:	GPLv2+
Group:		File tools
URL:		http://www.keepassx.org/
BuildRequires:	cmake
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	qt5-macros
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	pkgconfig(libgcrypt)
Provides:	keepass = %{version}-%{release}
Provides:	KeePassX = %{version}-%{release}

%description
KeePassX is a free/open-source password manager or safe which helps
you to manage your passwords in a secure way. You can put all your
passwords in one database, which is locked with one master key or a
key-disk. So you only have to remember one single master password or
insert the key-disk to unlock the whole database. The databases are
encrypted using the best and most secure encryption algorithms
currently known (AES and Twofish).

%prep
%if 0%{?pre}
%setup -qn %{name}-master
%else
%setup -q
%endif
%apply_patches

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%doc CHANGELOG
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/*/mimetypes/*.png

