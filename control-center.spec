Summary:	GNOME control center
Summary(pl):	Centrum kontroli GNOME
Name:		control-center
Version:	1.2.3
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/control-center/%{name}-%{version}.tar.gz
Patch0:		%{name}-nosound.patch
Patch1:		%{name}-esdrelease.patch
Patch2:		%{name}-bgcolor1.patch
Patch3:		%{name}-fsbgpath.patch
Patch4:		%{name}-applnk.patch
Icon:		control-center.gif
Requires:	xscreensaver >= 2.34
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.5
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.1.16
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
A Configuration tool for easily setting up your GNOME environment.
GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l pl
Narzêdzie do ³atwej konfiguracji twojego ¶rodowiska GNOME. GNOME to
Obiektowe ¦rodowisko Sieciowe na licencji GNU (GNU Network Object
Model Environment). Nazwa jest do¶æ dziwaczna, ale w rzeczywisto¶ci
jest to mi³e ¶rodowisko pracy. Powoduje, ¿e u¿ywanie komputera jest
proste, wydajne i ³atwe w konfiguracji.

%package devel
Summary:	GNOME control-center includes
Summary(pl):	Pliki nag³ówkowe centrum kontroli GNOME
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
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
Group(de):	X11/Entwicklung/Libraries
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

%build
gettextize --force --copy
aclocal -I macros
autoconf
automake -a -c
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_datadir}/control-center/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/Desktop/screensaver-properties.desktop
	
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Settings/{[!G]*,GNOME}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome

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
%{_applnkdir}/Settings/GNOME
%dir %{_datadir}/gnome/wm-properties
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_datadir}/idl/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
