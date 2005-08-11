# TODO
# - cvs move SPECS/{mozilla-plugin-mplayer,mplayerplug-in}.spec,v
Summary:	Embedded Video Player for Mozilla
Summary(pl):	Osadzony odtwarzacz wideo dla Mozilli
Name:		mplayerplug-in
Version:	3.05
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	mplayerplug-in-%{version}.tar.gz
# Source0-md5:	119c5634af875a712b27b90fdb1a3eb0
URL:		http://mplayerplug-in.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.224
Requires:	mplayer >= 1:1.0
Requires:	browser-plugins
Obsoletes:	mozilla-plugin-mplayer
Obsoletes:	mozilla-firefox-plugin-mplayer
Obsoletes:	opera-plugin-mplayer
Obsoletes:	konqueror-plugin-mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/browser-plugins

# use macro, otherwise extra LF isinserted along with the ifarch
%ifarch %{ix86} ppc sparc sparc64
%define	browsers mozilla, mozilla-firefox, opera, konqueror
%else
%define	browsers mozilla, mozilla-firefox, konqueror
%endif

%description
mplayerplug-in is a browser plugin that uses mplayer to play videos
from websites.

Supported browsers: %{browsers}.

%description -l pl
mplayerplug-in jest wtyczk� wykorzystuj�c� mplayera do odtwarzania
klip�w filmowych ze stron WWW.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_plugindir},%{_sysconfdir}/mplayer}

install *.so $RPM_BUILD_ROOT%{_plugindir}
install mplayerplug-in.conf $RPM_BUILD_ROOT%{_sysconfdir}
install mplayerplug-in.types $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- mozilla-firefox
%nsplugin_install -d %{_libdir}/mozilla-firefox/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so

%triggerun -- mozilla-firefox
%nsplugin_uninstall -d %{_libdir}/mozilla-firefox/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so

%triggerin -- mozilla
%nsplugin_install -d %{_libdir}/mozilla/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so

%triggerun -- mozilla
%nsplugin_uninstall -d %{_libdir}/mozilla/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so

%ifarch %{ix86} ppc sparc sparc64
%triggerin -- opera
%nsplugin_install -d %{_libdir}/opera/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so

%triggerun -- opera
%nsplugin_uninstall -d %{_libdir}/opera/plugins %{name}.so %{name}-{gmp,qt,rm,wmp}.so
%endif

%triggerin -- konqueror
%nsplugin_install -d %{_libdir}/kde3/plugins/konqueror %{name}.so %{name}-{gmp,qt,rm,wmp}.so

%triggerun -- konqueror
%nsplugin_uninstall -d %{_libdir}/kde3/plugins/konqueror %{name}.so %{name}-{gmp,qt,rm,wmp}.so

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README
%attr(755,root,root) %{_plugindir}/%{name}.so
%attr(755,root,root) %{_plugindir}/%{name}-gmp.so
%attr(755,root,root) %{_plugindir}/%{name}-qt.so
%attr(755,root,root) %{_plugindir}/%{name}-rm.so
%attr(755,root,root) %{_plugindir}/%{name}-wmp.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayerplug-in.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayer/mplayerplug-in.types
