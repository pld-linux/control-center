Summary:	GNOME control center
Summary(pl):	Centrum kontroli GNOME
Name:		control-center
Version:	1.4.0.1
Release:	4
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/control-center/%{name}-%{version}.tar.gz
Patch0:		%{name}-macros.patch
Patch1:		%{name}-applnk.patch
Patch2:		%{name}-gettext.patch
Patch3:		%{name}-wm-properties_path.patch
PAtch4:		%{name}-esdrelease.patch
URL:		http://www.gnome.org/
Icon:		control-center.gif
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.5
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gnome-libs-devel >= 1.2.12-3
BuildRequires:	gnome-vfs-devel >= 0.9
BuildRequires:	gtk+-devel >= 1.1.16
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
BuildRequires:	xml-i18n-tools
BuildRequires:	findutils
BuildRequires:	flex
BuildRequires:	bison
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
rm -f missing
xml-i18n-toolize --copy --force
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_datadir}/control-center/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/Desktop/screensaver-properties.desktop
	
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Settings/*.desktop \
      $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME
cp    $RPM_BUILD_ROOT%{_applnkdir}/Settings/Desktop/*.desktop \
      $RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/Desktop

find $RPM_BUILD_ROOT%{_applnkdir} -name .directory | xargs | rm -f

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
%{_datadir}/omf/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
