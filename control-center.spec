Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Summary(uk):	Центр керування GNOME
Summary(ru):	Центр управления GNOME
Name:		control-center
Version:	1.99.9
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-ac_am.patch
URL:		http://www.gnome.org/
Icon:		control-center.gif
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	audiofile >= 0.2.3-3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	esound-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.18
BuildRequires:	libbonobo-devel
BuildRequires:	libbonoboui-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnome-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libxml2-devel
BuildRequires:	libtool
PreReq:		scrollkeeper
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2

%description
A Configuration tool for easily setting up your GNOME environment.
GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l es
El control-center es una herramienta para una configuraciСn facilitada
el entorno GNOME.

%description -l pl
NarzЙdzie do Ёatwej konfiguracji twojego ╤rodowiska GNOME. GNOME to
Obiektowe ╕rodowisko Sieciowe na licencji GNU (GNU Network Object
Model Environment). Nazwa jest do╤Ф dziwaczna, ale w rzeczywisto╤ci
jest to miЁe ╤rodowisko pracy. Powoduje, ©e u©ywanie komputera jest
proste, wydajne i Ёatwe w konfiguracji.

%description -l pt_BR
O control-center И uma ferramenta para facilmente configurar seu
ambiente GNOME.

%description -l ru
Пакет control-center содержит утилиты, позволяющие настраивать среду
GNOME вашей системы (такие вещи как фон рабочего стола и темы,
программа сохранения экрана, оконный менеджер, системные звуки,
поведение мыши и др.)

Этот пакет нужен, если вы устанавливаете среду GNOME.

%description -l uk
Пакет control-center м╕стить утил╕ти, як╕ дозволяють настроювати
середовище GNOME вашо╖ системи (так╕ реч╕ як фон робочого столу та
теми, програма збереження екрану, в╕конний менеджер, системн╕ звуки,
повед╕нка миш╕ та ╕н.)

Цей пакет потр╕бний, якщо ви встановлю╓те середовище GNOME.

%prep
%setup -q
%patch0 -p1

%build
intltoolize --copy --force
gettextize --copy --force
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`; export GCONF_CONFIG_SOURCE
/usr/X11R6/bin/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null 2>&1

%postun
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/control-center-2.0/capplets/*
%{_datadir}/control-center-2.0/icons
%{_datadir}/control-center-2.0/interfaces
%{_datadir}/control-center-2.0/pixmaps
%{_datadir}/gnome/cursor-fonts
%{_datadir}/gnome/vfolders/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/idl/*
%{_pixmapsdir}/gnomecc-2
%{_pixmapsdir}/*.png
