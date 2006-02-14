Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Summary(uk):	Центр керування GNOME
Summary(ru):	Центр управления GNOME
Name:		control-center
Version:	2.13.92
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/control-center/2.13/%{name}-%{version}.tar.bz2
# Source0-md5:	eba22b935cfad8660a8ee1a4a0b1e47d
Patch0:		%{name}-randr.patch
Patch1:		%{name}-wm_properties-dir.patch
Patch2:		%{name}-additional-metacity-keybinding.patch
Patch3:		%{name}-default_apps.patch
Patch4:		%{name}-capplet.patch
Patch5:		%{name}-desktop.patch
Patch6:		%{name}-Makefile.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	audiofile >= 1:0.2.6
BuildRequires:	autoconf
BuildRequires:	automake >= 1.9.0
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	esound-devel
BuildRequires:	evolution-data-server-devel >= 1.4.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.12.1
BuildRequires:	gnome-doc-utils >= 0.4.2
BuildRequires:	gnome-menus-devel >= 2.12.0
BuildRequires:	gnome-vfs2-devel >= 2.13.4
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	gtk+2-devel >= 2:2.8.6
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.11.0
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	libxklavier-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	metacity-devel >= 2:2.12.1
BuildRequires:	nautilus-devel >= 2.11.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	scrollkeeper
Requires:	desktop-file-utils
Requires:	gnome-vfs2 >= 2.12.1
Requires:	libxklavier >= 2.0-3
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
Summary:	GNOME Control-Center header files
Summary(pl):	Pliki nagЁСwkowe bibliotek GNOME Control-Center
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
GNOME Control-Center header files.

%description devel -l pl
Pliki nagЁСwkowe bibliotek GNOME Control-Center

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1 

sed -i -e 's|-Wextra||' configure.in

%build
gnome-doc-prepare --copy --force
%{__gnome_doc_common}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-gstreamer \
	--enable-aboutme \
	X_EXTRA_LIBS="-lXext"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/window-manager-settings/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions*/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.{a,la}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install apps_gnome_settings_daemon_default_editor.schemas
%gconf_schema_install apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_install apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_install desktop_gnome_font_rendering.schemas
%gconf_schema_install desktop_gnome_peripherals_keyboard_xkb.schemas
%gconf_schema_install fontilus.schemas
%gconf_schema_install themus.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%preun
%gconf_schema_uninstall apps_gnome_settings_daemon_default_editor.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_uninstall desktop_gnome_font_rendering.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_keyboard_xkb.schemas
%gconf_schema_uninstall fontilus.schemas
%gconf_schema_uninstall themus.schemas

%postun
/sbin/ldconfig
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_screensaver.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_keyboard_xkb.schemas
%{_sysconfdir}/gconf/schemas/fontilus.schemas
%{_sysconfdir}/gconf/schemas/themus.schemas
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gnome-settings-daemon
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/nautilus/extensions*/*.so
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/lib*.so
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so
%dir %{_libdir}/window-manager-settings
%{_libdir}/bonobo/servers/*
%{_datadir}/control-center-2.0
%{_datadir}/gnome/cursor-fonts
%{_datadir}/gnome-default-applications
%{_datadir}/gnome/vfolders/*
%{_datadir}/idl/*
%{_iconsdir}/*/*/*/gnome-control-center.png
%{_omf_dest_dir}/control-center
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gnome-window-settings-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
