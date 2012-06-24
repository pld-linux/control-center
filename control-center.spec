Summary:	GNOME control center
Summary(es):	El centro de controle del GNOME
Summary(pl):	Centrum kontroli GNOME
Summary(pt_BR):	O Centro de Controle do GNOME
Summary(uk):	����� ��������� GNOME
Summary(ru):	����� ���������� GNOME
Name:		control-center
Version:	1.99.10
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	xmldocs.make
Source2:	omf.make
Patch0:		%{name}-ac_am.patch
URL:		http://www.gnome.org/
Icon:		control-center.gif
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	ORBit2-devel >= 2.4.0
BuildRequires:	audiofile >= 0.2.3-3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	esound-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	intltool >= 0.22
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.0.1
BuildRequires:	libxml2-devel >= 2.4.22
BuildRequires:	libtool
BuildRequires:	scrollkeeper >= 0.3.6
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

%prep
%setup -q
#%patch0 -p1
install %{SOURCE1} help/xmldocs.make
install %{SOURCE2} omf.make

%build
glib-gettextize --copy --force
intltoolize --copy --force
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
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
GCONF_CONFIG_SOURCE="" \
/usr/X11R6/bin/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

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
