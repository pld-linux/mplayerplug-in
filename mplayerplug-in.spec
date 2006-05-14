Summary:	Embedded Video Player for Mozilla
Summary(pl):	Osadzony odtwarzacz wideo dla Mozilli
Name:		mplayerplug-in
%define	snap	20060514
Version:	3.25
Release:	2.%{snap}.1
License:	GPL
Group:		X11/Applications/Multimedia
# Source0:	http://dl.sourceforge.net/mplayerplug-in/mplayerplug-in-%{version}.tar.gz
Source0:	http://mplayerplug-in.sourceforge.net/mplayerplug-in-daily.tar.gz
# Source0-md5:	571b6c169df405bd732eb29ddc069d37
Patch0:		%{name}-opera.patch
URL:		http://mplayerplug-in.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.236
Requires:	%{name}-common = %{version}-%{release}
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	konqueror-plugin-mplayer
Obsoletes:	mozilla-firefox-plugin-mplayer
Obsoletes:	mozilla-plugin-mplayer
Obsoletes:	opera-plugin-mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/browser-plugins
%define		browsers	mozilla, mozilla-firefox, konqueror, seamonkey

%description
mplayerplug-in is a browser plugin that uses mplayer to play videos
from websites.

Supported browsers: %{browsers}.

%description -l pl
mplayerplug-in jest wtyczk± przegl±darki wykorzystuj±c± mplayera do
odtwarzania klipów filmowych ze stron WWW.

Obs³ugiwane przegl±darki: %{browsers}.

%package common
Summary:	Common files for %{name}
Summary(pl):	Wspólne pliki dla %{name}
Group:		X11/Applications/Multimedia
Requires:	mplayer >= 1:1.0-0.pre5

%description common
This package provides common files for %{name}.

%description common -l pl
Ten pakiet dostarcza wspólne pliki dla %{name}.

%package opera
Summary:	Embedded Video Player for Opera
Summary(pl):	Osadzony odtwarzacz wideo dla Opery
Group:		X11/Applications/Multimedia
Requires:	%{name}-common = %{version}-%{release}
Requires:	opera
Obsoletes:	opera-plugin-mplayer

%description opera
mplayerplug-in is a browser plugin that uses mplayer to play videos
from websites. This plugin is adapted for Opera.

%description opera -l pl
mplayerplug-in jest wtyczk± przegl±darki wykorzystuj±c± mplayera do
odtwarzania klipów filmowych ze stron WWW. Ta wtyczka jest
dostosowana do Opery.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}

# for opera (works only with X toolkit)
%configure \
	--enable-x
%{__make}
mkdir -p opera
mv -f *.so opera/
mv -f *.xpt opera/

# other (with no limited features)
%configure \
	--enable-gtk2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/opera/plugins,%{_plugindir},%{_sysconfdir}/mplayer}

%{__make} install -C po \
	DESTDIR=$RPM_BUILD_ROOT

install *.so $RPM_BUILD_ROOT%{_plugindir}
install *.xpt $RPM_BUILD_ROOT%{_plugindir}
install opera/*.so $RPM_BUILD_ROOT%{_libdir}/opera/plugins
install opera/*.xpt $RPM_BUILD_ROOT%{_libdir}/opera/plugins
install mplayerplug-in.conf $RPM_BUILD_ROOT%{_sysconfdir}
install mplayerplug-in.types $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- mozilla-firefox
%nsplugin_install -d %{_libdir}/mozilla-firefox/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_install -d %{_libdir}/mozilla-firefox/plugins %{name}.xpt %%{name}-{gmp,qt,rm,wmp}.xpt

%triggerun -- mozilla-firefox
%nsplugin_uninstall -d %{_libdir}/mozilla-firefox/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_uninstall -d %{_libdir}/mozilla-firefox/plugins %{name}.xpt %{name}-{gmp,qt,rm,wmp}.xpt

%triggerin -- mozilla
%nsplugin_install -d %{_libdir}/mozilla/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_install -d %{_libdir}/mozilla/plugins %{name}.xpt %{name}-{gmp,qt,rm,wmp}.xpt

%triggerun -- mozilla
%nsplugin_uninstall -d %{_libdir}/mozilla/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_uninstall -d %{_libdir}/mozilla/plugins %{name}.xpt %{name}-{gmp,qt,rm,wmp}.xpt

%triggerin -- konqueror
%nsplugin_install -d %{_libdir}/kde3/plugins/konqueror %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_install -d %{_libdir}/kde3/plugins/konqueror %{name}.xpt %{name}-{gmp,qt,rm,wmp}.xpt

%triggerun -- konqueror
%nsplugin_uninstall -d %{_libdir}/kde3/plugins/konqueror %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_uninstall -d %{_libdir}/kde3/plugins/konqueror %{name}.xpt %{name}-{gmp,qt,rm,wmp}.xpt

%triggerin -- seamonkey
%nsplugin_install -d %{_libdir}/seamonkey/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_install -d %{_libdir}/seamonkey/plugins %{name}.xpt %{name}-{gmp,qt,rm,wmp}.xpt

%triggerun -- seamonkey
%nsplugin_uninstall -d %{_libdir}/seamonkey/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%nsplugin_uninstall -d %{_libdir}/seamonkey/plugins %{name}.xpt %{name}-{gmp,qt,rm,wmp}.xpt

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*.so
%{_plugindir}/*.xpt

%files common
%defattr(644,root,root,755)
%doc ChangeLog TODO README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mplayerplug-in.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mplayer/mplayerplug-in.types

%files opera
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opera/plugins/*.so
%{_libdir}/opera/plugins/*.xpt
