Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Summary(uk):	Центр керування GNOME
Summary(ru):	Центр управления GNOME
Name:		control-center
Version:	2.2.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.2/%{name}-%{version}.tar.bz2
Patch0:		%{name}-fontconfig.patch
URL:		http://www.gnome.org/
Icon:		control-center.gif
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	ORBit2-devel >= 2.6.0
BuildRequires:	audiofile >= 0.2.3-3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	esound-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libbonobo-devel >= 2.1.1
BuildRequires:	libbonoboui-devel >= 2.1.2
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.1.90
BuildRequires:	libgnomeui-devel >= 2.1.90
BuildRequires:	libxml2-devel >= 2.5.1
BuildRequires:	libtool
BuildRequires:	scrollkeeper >= 0.3.11
BuildRequires:	startup-notification-devel
BuildRequires:	metacity-devel
BuildRequires:	Xft-devel >= 2.1
Requires:	gnome-vfs2 >= 2.2.0
PreReq:		scrollkeeper
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

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

%package devel
Summary:	GNOME Control-Center includes
Summary(pl):	Pliki nagЁСwkowe bibliotek GNOME Control-Center
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
GNOME Control-Center header files.

%description devel -l pl
Pliki nagЁСwkowe bibliotek GNOME Control-Center

%package static
Summary:	GNOME Control-Center static libraries
Summary(pl):	Statyczne biblioteki GNOME Control-Center
Group:          X11/Development/Libraries                                       
Requires:       %{name} = %{version}  

%description static                                                             
GNOME Control-Centerp static libraries.                                                
                                                                                
%description static -l pl                                                       
Statyczne biblioteki GNOME Control-Center.   

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure --disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so
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

%files devel
%defattr(644,root,root,755)                                                     
%{_includedir}/gnome-window-settings-2.0
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
%{_libdir}/window-manager-settings/*.la

%files static                                                                   
%defattr(644,root,root,755)                                                     
%{_libdir}/*.a
%{_libdir}/window-manager-settings/*.a
