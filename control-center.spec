Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Name:		control-center
Version:	1.4.0.4
Release:	1
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
El control-center es una herramienta para una configuración facilitada
el entorno GNOME.

%description -l pl
Narzêdzie do ³atwej konfiguracji twojego ¶rodowiska GNOME. GNOME to
Obiektowe ¦rodowisko Sieciowe na licencji GNU (GNU Network Object
Model Environment). Nazwa jest do¶æ dziwaczna, ale w rzeczywisto¶ci
jest to mi³e ¶rodowisko pracy. Powoduje, ¿e u¿ywanie komputera jest
proste, wydajne i ³atwe w konfiguracji.

%description -l pt_BR
O control-center é uma ferramenta para facilmente configurar seu
ambiente GNOME.

%package devel
Summary:	GNOME control-center includes
Summary(es):	Archivos para desarrollo con el control-center del GNOME
Summary(pl):	Pliki nag³ówkowe centrum kontroli GNOME
Summary(pt_BR):	Arquivos para desenvolvimento com o control-center do GNOME
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Capplet development stuff.

%description devel -l es
Archivos para desarrollo con el control-center del GNOME

%description -l pl
Rzeczy potrzebne do kompilacji.

%description devel -l pt_BR
Se você estiver interessado em desenvolver painéis para o centro de
controle do GNOME este pacote será necessário.

O control-center-devel lhe a ajuda na criação de 'capplets', que são
usados no centro de controle.

%package static
Summary:	GNOME control-center static libraries
Summary(es):	Archivos estáticos para desarrollo con el control-center del GNOME
Summary(pl):	Statyczne biblioteki dla centrum kontroli GNOME
Summary(pt_BR):	Arquivos estáticos para desenvolvimento com o control-center
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME control-center static libraries.

%description static -l es
El control-center es una herramienta para una configuración facilitada
el entorno GNOME.

Archivos para desarrollo con el control-center del GNOME Archivos
estáticos del control-center del gnome.

%description -l pl
Statyczne biblioteki dla centrum kontroli GNOME.

%description static -l pt_BR
O control-center-devel lhe a ajuda na criação de 'capplets', que são
usados no centro de controle.

Se você estiver interessado em desenvolver painéis para o centro de
controle do GNOME este pacote será necessário. Nota: este pacote
contém somente os arquivos estáticos.

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

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
xml-i18n-toolize --copy --force
libtoolize --copy --force
gettextize --copy --force
rm -f macros/xml-i18n-tools.m4	# have it in xml-i18n-tools
aclocal -I macros
autoconf
automake -a -c -f
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/omf/%{name}

rm -f $RPM_BUILD_ROOT%{_datadir}/control-center/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/Desktop/screensaver-properties.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/Desktop/screensaver-properties.desktop

find $RPM_BUILD_ROOT%{_applnkdir} -name .directory | xargs rm -f

gzip -9nf AUTHORS ChangeLog NEWS README

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
