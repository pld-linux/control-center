Summary:     GNOME control center
Name:        control-center
Version:     0.99
Release:     1
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://ftp.gnome.org/pub/GNOME/source/%{name}-%{version}.tar.gz
Patch0:      control-center-DESTDIR.patch
Requires:    xscreensaver >= 2.34
Requires:    gnome-core = 0.99.2, ORBit = 0.3.91
URL:         http://www.gnome.org/
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   gnome

%description
A Configuration tool for easily setting up your GNOME environment.

GNOME is the GNU Network Object Model Environment. That's a fancy name but
really GNOME is a nice GUI desktop environment. It makes using your computer
easy, powerful, and easy to configure.

%package devel
Summary:     GNOME control-center includes
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
Capplet development stuff.

%package static
Summary:     GNOME control-center static libraries
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
GNOME control-center static libraries.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
%attr(755, root, root) /usr/X11R6/bin/*
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
/usr/X11R6/share/control-center
/usr/X11R6/share/apps/System/*
/usr/X11R6/share/pixmaps/*

%lang(ca)    /usr/X11R6/share/locale/ca/LC_MESSAGES/control-center.mo
%lang(cs)    /usr/X11R6/share/locale/cs/LC_MESSAGES/control-center.mo
%lang(da)    /usr/X11R6/share/locale/da/LC_MESSAGES/control-center.mo
%lang(de)    /usr/X11R6/share/locale/de/LC_MESSAGES/control-center.mo
%lang(es)    /usr/X11R6/share/locale/es/LC_MESSAGES/control-center.mo
#%lang(es_DO) /usr/X11R6/share/locale/es_DO/LC_MESSAGES/control-center.mo
#%lang(es_GT) /usr/X11R6/share/locale/es_GT/LC_MESSAGES/control-center.mo
#%lang(es_HN) /usr/X11R6/share/locale/es_HN/LC_MESSAGES/control-center.mo
#%lang(es_MX) /usr/X11R6/share/locale/es_MX/LC_MESSAGES/control-center.mo
#%lang(es_PA) /usr/X11R6/share/locale/es_PA/LC_MESSAGES/control-center.mo
#%lang(es_PE) /usr/X11R6/share/locale/es_PE/LC_MESSAGES/control-center.mo
#%lang(es_SV) /usr/X11R6/share/locale/es_SV/LC_MESSAGES/control-center.mo
%lang(fi)    /usr/X11R6/share/locale/fi/LC_MESSAGES/control-center.mo
%lang(fr)    /usr/X11R6/share/locale/fr/LC_MESSAGES/control-center.mo
%lang(ga)    /usr/X11R6/share/locale/ga/LC_MESSAGES/control-center.mo
%lang(hu)    /usr/X11R6/share/locale/hu/LC_MESSAGES/control-center.mo
%lang(it)    /usr/X11R6/share/locale/it/LC_MESSAGES/control-center.mo
%lang(ja)    /usr/X11R6/share/locale/ja/LC_MESSAGES/control-center.mo
%lang(ko)    /usr/X11R6/share/locale/ko/LC_MESSAGES/control-center.mo
%lang(no)    /usr/X11R6/share/locale/no/LC_MESSAGES/control-center.mo
%lang(pl)    /usr/X11R6/share/locale/pl/LC_MESSAGES/control-center.mo
%lang(pt)    /usr/X11R6/share/locale/pt/LC_MESSAGES/control-center.mo
%lang(ru)    /usr/X11R6/share/locale/ru/LC_MESSAGES/control-center.mo
%lang(sv)    /usr/X11R6/share/locale/sv/LC_MESSAGES/control-center.mo

%files devel
%defattr(644,  root, root, 755)
%attr(755, root, root) /usr/X11R6/lib/lib*.so
/usr/X11R6/share/idl/*
/usr/X11R6/include/*
%attr(755, root, root) /usr/X11R6/lib/*.sh

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%changelog
* Wed Jan 06 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.99-1]
- added -q %setup parameter,
- added LDFLAGS="-s" to ./configure enviroment,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- added full %attr description in %files,
- added %lang macros for
  /usr/X11R6/share/locale/*/LC_MESSAGES/control-center.mo files,
- added stripping shared libraries.

* Wed Dec 16 1998 Jonathan Blandford <jrb@redhat.com>
- Created for the new control-center branch
