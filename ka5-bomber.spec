%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		bomber
Summary:	Single player arcade game
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3b5cb57ffd1ab5cd2b399520d041a832
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bomber is a single player arcade game. The player is invading various
cities in a plane that is decreasing in height.

The goal of the game is to destroy all the buildings and advance to
the next level. Each level gets a bit harder by increasing the speed
of the plane and the height of the buildings.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bomber
%{_desktopdir}/org.kde.bomber.desktop
%{_datadir}/bomber
%{_datadir}/config.kcfg/bomber.kcfg
%{_iconsdir}/hicolor/128x128/apps/bomber.png
%{_iconsdir}/hicolor/32x32/apps/bomber.png
%{_iconsdir}/hicolor/48x48/apps/bomber.png
%{_iconsdir}/hicolor/64x64/apps/bomber.png
%dir %{_datadir}/kxmlgui5/bomber
%{_datadir}/kxmlgui5/bomber/bomberui.rc
%{_datadir}/metainfo/org.kde.bomber.appdata.xml
