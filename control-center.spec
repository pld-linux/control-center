Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Summary(uk):	����� ��������� GNOME
Summary(ru):	����� ���������� GNOME
Name:		control-center
Version:	2.7.1
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	f3f04612dc2485acaaa8e92c66f03331
Patch0:		%{name}-fontconfig.patch
Patch1:		%{name}-randr.patch
#Patch2:		%{name}-def-apps-capplet.patch
Patch3:		%{name}-wm_properties-dir.patch
Patch4:		%{name}-additional-metacity-keybinding.patch
Patch5:		%{name}-capplets-dir.patch
Patch6:		%{name}-dpi.patch
Patch7:		%{name}-locale-names.patch
#Patch8:		%{name}-reduced_resources.patch
Patch9:		%{name}-def-apps-capplet-browsers.patch
URL:		http://www.gnome.org/
Icon:		control-center.gif
BuildRequires:	GConf2-devel >= 2.7.91
BuildRequires:	ORBit2-devel >= 1:2.11.2
BuildRequires:	audiofile >= 1:0.2.6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	esound-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.7.91
BuildRequires:	gnome-vfs2-devel >= 2.7.91
BuildRequires:	gstreamer-plugins-devel >= 0.8.3
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	intltool >= 0.30
BuildRequires:	libbonobo-devel >= 2.6.2
BuildRequires:	libbonoboui-devel >= 2.6.1
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnome-devel >= 2.7.91
BuildRequires:	libgnomeui-devel >= 2.7.91
BuildRequires:	libxml2-devel >= 2.6.7
BuildRequires:	libxklavier-devel >= 1.03
BuildRequires:	libtool
BuildRequires:	metacity-devel >= 2:2.8.3
BuildRequires:	nautilus-devel >= 2.7.4
BuildRequires:	scrollkeeper >= 0.3.12
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	xft-devel >= 2.1.1
PreReq:		/sbin/ldconfig
PreReq:		scrollkeeper
Requires(post):	GConf2
Requires:	gnome-vfs2 >= 2.7.91
Obsoletes:	acme
Obsoletes:	fontilus
Obsoletes:	gnome
Obsoletes:	themus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Configuration tool for easily setting up your GNOME environment.
GNOME is the GNU Network Object Model Environment. That's a fancy name
but really GNOME is a nice GUI desktop environment. It makes using
your computer easy, powerful, and easy to configure.

%description -l es
El control-center es una herramienta para una configuraci�n facilitada
el entorno GNOME.

%description -l pl
Narz�dzie do �atwej konfiguracji twojego �rodowiska GNOME. GNOME to
Obiektowe �rodowisko Sieciowe na licencji GNU (GNU Network Object
Model Environment). Nazwa jest do�� dziwaczna, ale w rzeczywisto�ci
jest to mi�e �rodowisko pracy. Powoduje, �e u�ywanie komputera jest
proste, wydajne i �atwe w konfiguracji.

%description -l pt_BR
O control-center � uma ferramenta para facilmente configurar seu
ambiente GNOME.

%description -l ru
����� control-center �������� �������, ����������� ����������� �����
GNOME ����� ������� (����� ���� ��� ��� �������� ����� � ����,
��������� ���������� ������, ������� ��������, ��������� �����,
��������� ���� � ��.)

���� ����� �����, ���� �� �������������� ����� GNOME.

%description -l uk
����� control-center ͦ����� ���̦��, �˦ ���������� �����������
���������� GNOME ���ϧ ������� (��˦ ��ަ �� ��� �������� ����� ��
����, �������� ���������� ������, צ������ ��������, ������Φ �����,
����Ħ��� ��ۦ �� ��.)

��� ����� ���Ҧ����, ���� �� ������������ ���������� GNOME.

%package devel
Summary:	GNOME Control-Center header files
Summary(pl):	Pliki nag��wkowe bibliotek GNOME Control-Center
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
GNOME Control-Center header files.

%description devel -l pl
Pliki nag��wkowe bibliotek GNOME Control-Center

%package static
Summary:	GNOME Control-Center static libraries
Summary(pl):	Statyczne biblioteki GNOME Control-Center
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GNOME Control-Center static libraries.

%description static -l pl
Statyczne biblioteki GNOME Control-Center.

%prep
%setup -q
%patch0 -p1 -b .wiget
%patch1 -p1
##%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
##%patch8 -p1
%patch9 -p0

rm po/no.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-gstreamer \
	X_EXTRA_LIBS="-lXext"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/window-manager-settings/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.{a,la}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/fontilus-context-menu
%attr(755,root,root) %{_libdir}/gnome-settings-daemon
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/bonobo/*.so
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/lib*.so
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so
%dir %{_libdir}/window-manager-settings
%{_libdir}/bonobo/servers/*
%{_datadir}/application-registry/*
%{_datadir}/control-center-2.0
%{_datadir}/gnome/cursor-fonts
%{_datadir}/gnome/vfolders/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gnome/capplets
%{_datadir}/idl/*
%{_datadir}/mime-info/*
%{_iconsdir}/*
%{_pixmapsdir}/gnomecc-2
%{_pixmapsdir}/*.png
%{_desktopdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnome-window-settings-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
