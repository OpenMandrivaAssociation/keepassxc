Name:           keepassx
Version:        0.4.1
Release:        %mkrel 1
Epoch:          0
Summary:        Cross Platform Password Manager
License:        GPLv2+
Group:          File tools
URL:            http://www.keepassx.org/
Source0:        http://downloads.sourceforge.net/keepassx/keepassx-%{version}.tar.gz
Source1:        %{name}.desktop
Provides:       keepass = %{epoch}%{version}-%{release}
Provides:       KeePassX = %{epoch}%{version}-%{release}
Requires(post):  desktop-file-utils
Requires(postun):  desktop-file-utils
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick
BuildRequires:  libxtst-devel
BuildRequires:  qt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{qt4dir}/bin/qmake
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} INSTALL_ROOT=%{buildroot}

%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

%{_bindir}/convert -scale 32 share/keepassx/icons/keepassx.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{_bindir}/convert -scale 16 share/keepassx/icons/keepassx.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_bindir}/convert -scale 32 share/keepassx/icons/keepassx.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_bindir}/convert -scale 64 share/keepassx/icons/keepassx.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{_bindir}/desktop-file-install --vendor "" \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE1}

%clean
%{__rm} -rf %{buildroot}

%post
%{update_desktop_database}
%update_icon_cache hicolor
%{update_mime_database}

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%{clean_mime_database}

%files
%defattr(0644,root,root,0755)
%doc changelog
%attr(0755,root,root) %{_bindir}/keepassx
%{_datadir}/keepassx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/keepassx.xpm
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/mime/packages/keepassx.xml
%{_datadir}/mimelnk/application/x-keepass.desktop
