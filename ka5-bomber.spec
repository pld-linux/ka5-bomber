#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		bomber
Summary:	Single player arcade game
Name:		ka5-%{kaname}
Version:	22.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	21512b4ed6ad13e9fa7a5cf7d80b5036
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
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

%description -l pl.UTF-8
Bomber jest jednoosobową grą zręcznościową. Gracz bombarduje różne miasta
samolotem, z każdym przelotem wysokość na której leci bombowiec obniża się.

Celem gry jest zniszczenie wszystkich budynków, żeby przejść do następnego
poziomu. Każdy następny poziom jest coraz trudniejszy przez zwiększającą
się prędkość samolotu i wyższe budynki.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


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
%{_datadir}/metainfo/org.kde.bomber.appdata.xml
