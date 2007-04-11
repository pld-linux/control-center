Summary:	GNOME Control Center
Summary(es.UTF-8):	El centro de controle del GNOME
Summary(pl.UTF-8):	Centrum Kontroli GNOME
Summary(pt_BR.UTF-8):	O Centro de Controle do GNOME
Summary(ru.UTF-8):	Центр управления GNOME
Summary(uk.UTF-8):	Центр керування GNOME
Name:		control-center
Version:	2.18.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/control-center/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	bae0fd0f9e32f374bd7236d98788b13f
Patch0:		%{name}-randr.patch
Patch1:		%{name}-wm_properties-dir.patch
Patch2:		%{name}-additional-metacity-keybinding.patch
Patch3:		%{name}-default_apps.patch
Patch4:		%{name}-capplet.patch
Patch5:		%{name}-Makefile.patch
Patch6:		%{name}-compiz-support.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	alsa-lib-devel >= 1.0.12
BuildRequires:	audiofile >= 1:0.2.6
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	esound-devel
BuildRequires:	evolution-data-server-devel >= 1.10.1
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-desktop-devel >= 2.18.0
BuildRequires:	gnome-doc-utils >= 0.10.3
BuildRequires:	gnome-menus-devel >= 2.18.0
BuildRequires:	gnome-panel-devel >= 2.18.0
BuildRequires:	gnome-vfs2-devel >= 2.18.1
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.10.10
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomekbd-devel >= 2.18.1
BuildRequires:	libgnomeui-devel >= 2.18.1
BuildRequires:	librsvg-devel >= 2.16.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	metacity-devel >= 2:2.18.2
BuildRequires:	nautilus-devel >= 2.18.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	desktop-file-utils
Requires:	gnome-vfs2 >= 2.18.1
Requires:	gstreamer-audio-effects-base >= 0.10.10
Obsoletes:	acme
Obsoletes:	fontilus
Obsoletes:	gnome
Obsoletes:	themus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Configuration tool for easily setting up your GNOME environment.

%description -l es.UTF-8
El control-center es una herramienta para una configuración facilitada
el entorno GNOME.

%description -l pl.UTF-8
Narzędzie do łatwej konfiguracji środowiska GNOME.

%description -l pt_BR.UTF-8
O Control Center é uma ferramenta para facilmente configurar seu
ambiente GNOME.

%description -l ru.UTF-8
Пакет Control Center содержит утилиты, позволяющие настраивать среду
GNOME вашей системы (такие вещи как фон рабочего стола и темы,
программа сохранения экрана, оконный менеджер, системные звуки,
поведение мыши и др.)

Этот пакет нужен, если вы устанавливаете среду GNOME.

%description -l uk.UTF-8
Пакет Control Center містить утиліти, які дозволяють настроювати
середовище GNOME вашої системи (такі речі як фон робочого столу та
теми, програма збереження екрану, віконний менеджер, системні звуки,
поведінка миші та ін.)

Цей пакет потрібний, якщо ви встановлюєте середовище GNOME.

%package libs
Summary:	GNOME Control Center gnome-window-settings library
Summary(pl.UTF-8):	Biblioteka Control Center gnome-window-settings
Group:		Development/Libraries
Requires:	libgnomeui >= 2.18.1

%description libs
This package contains gnome-window-settings library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gnome-window-settings.

%package devel
Summary:	GNOME Control Center header files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek GNOME Control Center
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	dbus-glib-devel >= 0.73
Requires:	fam-devel
Requires:	gnome-desktop-devel >= 2.18.0
Requires:	gnome-menus-devel >= 2.18.0
Requires:	gtk+2-devel >= 2:2.10.10
Requires:	libgnomeui-devel >= 2.18.1
Requires:	librsvg-devel >= 2.16.1

%description devel
GNOME Control-Center header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek GNOME Control Center.

%package static
Summary:	GNOME Control Center static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GNOME Control Center
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GNOME Control Center static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNOME Control Center.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__gnome_doc_prepare}
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
	--disable-update-mimedb \
	--enable-gstreamer=0.10 \
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_gnome_settings_daemon_default_editor.schemas
%gconf_schema_install apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_install apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_install control-center.schemas
%gconf_schema_install desktop_gnome_font_rendering.schemas
%gconf_schema_install fontilus.schemas
%gconf_schema_install themus.schemas
%scrollkeeper_update_post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_gnome_settings_daemon_default_editor.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_uninstall	control-center.schemas
%gconf_schema_uninstall desktop_gnome_font_rendering.schemas
%gconf_schema_uninstall fontilus.schemas
%gconf_schema_uninstall themus.schemas

%postun
%scrollkeeper_update_postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_screensaver.schemas
%{_sysconfdir}/gconf/schemas/control-center.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas
%{_sysconfdir}/gconf/schemas/fontilus.schemas
%{_sysconfdir}/gconf/schemas/themus.schemas
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_sysconfdir}/xdg/menus/gnomecc.menu
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gnome-settings-daemon
%attr(755,root,root) %{_libdir}/nautilus/extensions*/*.so
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/lib*.so
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so
%dir %{_libdir}/window-manager-settings
%{_datadir}/control-center
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-directories/*.directory
%{_datadir}/gnome/cursor-fonts
%{_datadir}/mime/packages/gnome-theme-package.xml
%{_iconsdir}/hicolor/*/*/typing-monitor.*
%{_omf_dest_dir}/control-center
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-window-settings.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-window-settings.so
%{_libdir}/libgnome-window-settings.la
%{_includedir}/gnome-window-settings-2.0
%{_includedir}/gnome-settings-daemon-2.0
%{_pkgconfigdir}/gnome-window-settings-2.0.pc
%{_pkgconfigdir}/gnome-settings-daemon.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-window-settings.a
