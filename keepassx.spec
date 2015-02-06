Summary:		Cross Platform Password Manager
Name:		keepassx
Version:		0.4.3
Release:		4
Source0:		http://downloads.sourceforge.net/keepassx/keepassx-%{version}.tar.gz
Patch0:		keepassx-0.4.3-fix-getpid-undef.patch
License:		GPLv2+
Group:		File tools
URL:		http://www.keepassx.org/
BuildRequires:	desktop-file-utils
#BuildRequires:	imagemagick
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


%changelog
* Tue Oct 09 2012 Giovanni Mariani <mc2374@mclink.it> 0.4.3-3
- Added BReq for libxi-devel, because the build needs XInput.h
- Added P0 to fix build failure because of "getpid" undefined
- Added version info to BReqs accoridng to to CMakeList.txt file
- Dropped BuildRoot, %%mkrel and %%clean section
- Dropped BReq for imagemagick: no more used in the build process

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.3-2mdv2011.0
+ Revision: 612563
- the mass rebuild of 2010.1 packages

* Wed Apr 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 532448
- fix spec
- new upstream release 0.4.3
- use upstream .desktop file instead of custom one
- clean spec

* Wed Feb 24 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0:0.4.2-0.beta.1mdv2010.1
+ Revision: 510701
- new version 0.4.2beta

* Fri Sep 18 2009 David Walluck <walluck@mandriva.org> 0:0.4.1-1mdv2010.0
+ Revision: 444394
- 0.4.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jan 15 2009 David Walluck <walluck@mandriva.org> 0:0.3.4-1mdv2009.1
+ Revision: 329876
- fix Exec line in .desktop
- 0.3.4

* Sat Oct 18 2008 David Walluck <walluck@mandriva.org> 0:0.3.3-1mdv2009.1
+ Revision: 295152
- 0.3.3

* Sun Aug 03 2008 David Walluck <walluck@mandriva.org> 0:0.3.2-1mdv2009.0
+ Revision: 261705
- 0.3.2

* Sun Apr 20 2008 David Walluck <walluck@mandriva.org> 0:0.3.1-1mdv2009.0
+ Revision: 196008
- 0.3.1

* Wed Jan 02 2008 David Walluck <walluck@mandriva.org> 0:0.2.2-5mdv2008.1
+ Revision: 140689
- add mime type to desktop file

* Wed Jan 02 2008 David Walluck <walluck@mandriva.org> 0:0.2.2-4mdv2008.1
+ Revision: 140687
- add mime file source
- add desktop post
- add mime file

* Tue Jan 01 2008 David Walluck <walluck@mandriva.org> 0:0.2.2-3mdv2008.1
+ Revision: 140032
- add docs

* Tue Jan 01 2008 David Walluck <walluck@mandriva.org> 0:0.2.2-2mdv2008.1
+ Revision: 139957
-BuildRequires: libxtst-devel
- import keepassx


