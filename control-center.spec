Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Summary(uk):	Центр керування GNOME
Summary(ru):	Центр управления GNOME
Name:		control-center
Version:	1.99.7
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
Icon:		control-center.gif
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
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
PreReq:		/sbin/ldconfig
PreReq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
Summary:	GNOME control-center includes
Summary(es):	Archivos para desarrollo con el control-center del GNOME
Summary(pl):	Pliki nagЁСwkowe centrum kontroli GNOME
Summary(pt_BR):	Arquivos para desenvolvimento com o control-center do GNOME
Summary(ru):	Среда разработки программ для Центра Управления GNOME
Summary(uk):	Середовище розробки програм для Центру Керування GNOME
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Capplet development stuff.

%description devel -l es
Archivos para desarrollo con el control-center del GNOME

%description -l pl
Rzeczy potrzebne do kompilacji.

%description devel -l pt_BR
Se vocЙ estiver interessado em desenvolver painИis para o centro de
controle do GNOME este pacote serА necessАrio.

O control-center-devel lhe a ajuda na criaГЦo de 'capplets', que sЦo
usados no centro de controle.

%description devel -l ru
Пакет control-center-devel содержит среду, необходимую для разработки
модулей (`capplets'), используемых в Центре Управления GNOME.

Если вы только используете рабочий стол GNOME, но не разрабатываете
программ, то вам не нужно устанавливать этот пакет.

%description devel -l uk
Пакет control-center-devel м╕стить середовище, необх╕дне для розробки
модул╕в (`capplets'), як╕ використовуються в Центр╕ Керування GNOME.

Якщо ви лише використову╓те робочий ст╕л GNOME, але не розробля╓те
програм, то вам не потр╕бно встановлювати цей пакет.

%package static
Summary:	GNOME control-center static libraries
Summary(es):	Archivos estАticos para desarrollo con el control-center del GNOME
Summary(pl):	Statyczne biblioteki dla centrum kontroli GNOME
Summary(pt_BR):	Arquivos estАticos para desenvolvimento com o control-center
Summary(ru):	Статические библиотеки для разработки программ Центра Управления GNOME
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм Центру Керування GNOME
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME control-center static libraries.

%description static -l es
El control-center es una herramienta para una configuraciСn facilitada
el entorno GNOME.

Archivos para desarrollo con el control-center del GNOME Archivos
estАticos del control-center del gnome.

%description -l pl
Statyczne biblioteki dla centrum kontroli GNOME.

%description static -l pt_BR
O control-center-devel lhe a ajuda na criaГЦo de 'capplets', que sЦo
usados no centro de controle.

Se vocЙ estiver interessado em desenvolver painИis para o centro de
controle do GNOME este pacote serА necessАrio. Nota: este pacote
contИm somente os arquivos estАticos.

%description static -l ru
Пакет control-center-static содержит статические библиотеки для
разработки модулей (`capplets'), используемых в Центре Управления
GNOME.

%description static -l uk
Пакет control-center-static м╕стить статичн╕ б╕бл╕отеки для розробки
модул╕в (`capplets'), як╕ використовуються в Центр╕ Керування GNOME.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/omf/%{name}

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_datadir}/control-center
%{_applnkdir}/Settings/GNOME
%{_omf_dest_dir}/omf/%{name}
%dir %{_datadir}/gnome/wm-properties
%{_pixmapsdir}/*
%{_datadir}/idl/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
