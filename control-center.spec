Summary:	GNOME control center
Summary(pl):	Centrum kontroli GNOME
Name:		control-center
Version:	1.0.53
Release:	2
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/control-center/%{name}-%{version}.tar.gz
Patch0:		control-center-nosound.patch
Patch1:		control-center-esdrelease.patch
Patch2:		control-center-bgcolor1.patch
Patch3:		control-center-fsbgpath.patch
Patch4:		control-center-dontstartesd.patch
Patch5:		control-center-limitedbgs.patch
Patch6:		control-center-numwallpapers.patch
Patch7:		control-center-applnk.patch
Icon:		control-center.gif
Requires:	xscreensaver >= 2.34
BuildRequires:	gtk+-devel >= 1.1.16
BuildRequires:	esound-devel >= 0.2.5
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
A Configuration tool for easily setting up your GNOME environment. GNOME is
the GNU Network Object Model Environment. That's a fancy name but really
GNOME is a nice GUI desktop environment. It makes using your computer easy,
powerful, and easy to configure.

%description -l pl
Narzêdzie do ³atwej konfiguracji twojego ¶rodowiska GNOME. GNOME to
Obiektowe ¦rodowisko Sieciowe na licencji GNU (GNU Network Object Model
Environment). Nazwa jest do¶æ dziwaczna, ale w rzeczywisto¶ci jest to mi³e
¶rodowisko pracy. Powoduje, ¿e u¿ywanie komputera jest proste, wydajne i
³atwe w konfiguracji.

%package devel
Summary:	GNOME control-center includes
Summary(pl):	Pliki nag³ówkowe centrum kontroli GNOME
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Capplet development stuff.

%description -l pl
Rzeczy potrzebne do kompilacji.

%package static
Summary:	GNOME control-center static libraries
Summary(pl):	Statyczne biblioteki dla centrum kontroli GNOME
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
GNOME control-center static libraries.

%description -l pl
Statyczne biblioteki dla centrum kontroli GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
gettextize --force --copy
automake
LDFLAGS="-s"; export LDFLAGS 
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_datadir}/control-center/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/Desktop/screensaver-properties.desktop

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_datadir}/control-center
%{_applnkdir}/Settings
%dir %{_datadir}/gnome/wm-properties
%{_datadir}/pixmaps/*

%files devel
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_datadir}/idl/*
%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
