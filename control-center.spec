Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Summary(uk):	Центр керування GNOME
Summary(ru):	Центр управления GNOME
Name:		control-center
Version:	1.4.0.5
Release:	4
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/control-center/%{name}-%{version}.tar.gz
Patch0:		%{name}-macros.patch
Patch1:		%{name}-applnk.patch
Patch2:		%{name}-wm-properties_path.patch
Patch3:		%{name}-esdrelease.patch
Patch4:		%{name}-pldrelease.patch
Patch5:		%{name}-am_conditional.patch
Patch6:		%{name}-uipropertiesmenu.patch
Patch7:		%{name}-setroothint.patch
Patch8:		%{name}-no_mans.patch
Patch9:		%{name}-omf.patch
URL:		http://www.gnome.org/
Icon:		control-center.gif
BuildRequires:	GConf-devel
BuildRequires:	ORBit-devel >= 0.5.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	esound-devel >= 0.2.5
BuildRequires:	findutils
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.12-3
BuildRequires:	gnome-vfs-devel >= 0.9
BuildRequires:	gtk+-devel >= 1.1.16
BuildRequires:	imlib-devel >= 1.8.2
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	oaf-devel
BuildRequires:	zlib-devel
BuildRequires:  libxml-devel
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	scrollkeeper
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
xml-i18n-toolize --copy --force
%{__libtoolize}
%{__gettextize}
rm -f macros/xml-i18n-tools.m4	# have it in xml-i18n-tools
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

rm -f $RPM_BUILD_ROOT%{_datadir}/control-center/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/Desktop/screensaver-properties.desktop

find $RPM_BUILD_ROOT%{_applnkdir} -name .directory | xargs rm -f

%find_lang %{name} --with-gnome

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
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%{_datadir}/control-center
%{_applnkdir}/Settings/GNOME
%{_omf_dest_dir}/%{name}
%dir %{_datadir}/gnome/wm-properties
%{_pixmapsdir}/*
%{_datadir}/idl/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
