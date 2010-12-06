Summary:	Cross Platform Password Manager
Name:		keepassx
Version:	0.4.3
Release:	%mkrel 2
Source0:	http://downloads.sourceforge.net/keepassx/keepassx-%{version}.tar.gz
License:	GPLv2+
Group:		File tools
URL:		http://www.keepassx.org/
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	libxtst-devel
BuildRequires:	qt4-devel
BuildRequires:	desktop-file-utils
Provides:	keepass = %{version}-%{release}
Provides:	KeePassX = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
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
