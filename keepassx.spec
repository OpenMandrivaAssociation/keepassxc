Summary:	Cross Platform Password Manager
Name:		keepassx
Version:	0.4.4
Release:	1
Source0:	https://www.keepassx.org/releases/%{version}/keepassx-%{version}.tar.gz
Patch0:		keepassx-0.4.3-fix-getpid-undef.patch
License:	GPLv2+
Group:		File tools
URL:		http://www.keepassx.org/
BuildRequires:	desktop-file-utils
BuildRequires:	libxi-devel
BuildRequires:	libxtst-devel
BuildRequires:	qt4-devel >= 4.3.0
BuildRequires:	desktop-file-utils
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
%setup -q
%apply_patches

%build
%qmake_qt4 PREFIX=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std INSTALL_ROOT=%{buildroot}

install -D -m 644 share/keepassx/icons/keepassx_large.png	%{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
install -D -m 644 share/keepassx/icons/keepassx.png		%{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -D -m 644 share/keepassx/icons/keepassx_small.png	%{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

# fix .desktop file
desktop-file-install --vendor="mandriva" \
		--add-category="System" \
		--remove-key="X-SuSE-translate" \
		--delete-original \
		--dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc changelog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-keepass.desktop
