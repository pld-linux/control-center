Summary:	GNOME control center
Summary(pl):	Centrum kontroli GNOME
Name:		control-center
Version:	1.0.5
Release:	22
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/source/%{name}-%{version}.tar.gz
Source1:	control-center.png
Source2:	gnomecc.desktop
Patch0:		control-center-nosound.patch
Patch1:		control-center-esdrelease.patch
Patch2:		control-center-bgcolor1.patch
Patch3:		control-center-fsbgpath.patch
Patch4:		control-center-dontstartesd.patch
Patch5:		control-center-newsession.patch
Patch6:		control-center-fixclosedlg.patch 
Patch7:		control-center-limitedbgs.patch
Patch8:		control-center-smfixtry.patch
Patch9:		control-center-quietdebug.patch
Patch10:	control-center-geditfixtry.patch
Patch11:	control-center-addmime.patch
Patch12:	control-center-noscreensaver.patch
Patch13:	control-center-numwallpapers.patch
Patch14:	control-center-warning.patch
URL:		http://www.gnome.org/
Icon:		control-center.gif
Requires:	xscreensaver >= 2.34
BuildRequires:	gtk+-devel >= 1.1.16
BuildRequires:	esound-devel >= 0.2.5
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%description
A Configuration tool for easily setting up your GNOME environment.

GNOME is the GNU Network Object Model Environment. That's a fancy name but
really GNOME is a nice GUI desktop environment. It makes using your computer
easy, powerful, and easy to configure.

%description -l pl
Narzêdzie do ³atwej konfiguracji twojego ¶rodowiska GNOME.

GNOME to Obiektowe ¦rodowisko Sieciowe na licencji GNU (GNU Network Object
Model Environment). Nazwa jest do¶æ dziwaczna, ale w rzeczywisto¶ci jest to
mi³e ¶rodowisko pracy. Powoduje, ¿e u¿ywanie komputera jest proste, wydajne
i ³atwe w konfiguracji.

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
Statyczne biblioteki dla centrum kontroli GNOME

%prep
%setup -q
%patch0  -p1
%patch1  -p1
%patch2  -p1
%patch3  -p1
%patch4  -p1
%patch5  -p1
%patch6  -p1
%patch7  -p1
%patch8  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

cp %{SOURCE1} %{SOURCE2} control-center

%build
gettextize --force --copy
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

rm -f $RPM_BUILD_ROOT/usr/X11R6/bin/ui-properties
rm -rf $RPM_BUILD_ROOT/usr/X11R6/share/control-center/UIOptions
rm -rf $RPM_BUILD_ROOT/usr/X11R6/share/gnome/apps/Settings/UIOptions
                                                                                                              

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang

%defattr(644,root,root,755)
/etc/X11/GNOME/CORBA/servers/*
%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

/usr/X11R6/share/control-center
/usr/X11R6/share/gnome/
/usr/X11R6/share/pixmaps/*

%files devel
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) /usr/X11R6/lib/lib*.so
/usr/X11R6/share/idl/*
/usr/X11R6/include/*
%attr(755,root,root) /usr/X11R6/lib/*.sh

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a
