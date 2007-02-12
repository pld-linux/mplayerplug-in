# TODO
# - cvs move SPECS/{mozilla-plugin-mplayer,mplayerplug-in}.spec,v
Summary:	Embedded Video Player for Mozilla
Summary(pl.UTF-8):   Osadzony odtwarzacz wideo dla Mozilli
Name:		mplayerplug-in
Version:	2.85
Release:	0.13
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplayerplug-in/mplayerplug-in-%{version}.tar.gz
# Source0-md5:	57353e0f61640331972f860aa5fda3f1
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

%description -l pl.UTF-8
mplayerplug-in jest wtyczką wykorzystującą mplayera do odtwarzania
klipów filmowych ze stron WWW.

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
%ns_plugin_install -d %{_libdir}/mozilla-firefox/plugins %{name}.so

%triggerun -- mozilla-firefox
%ns_plugin_uninstall -d %{_libdir}/mozilla-firefox/plugins %{name}.so

%triggerin -- mozilla
%ns_plugin_install -d %{_libdir}/mozilla/plugins %{name}.so

%triggerun -- mozilla
%ns_plugin_uninstall -d %{_libdir}/mozilla/plugins %{name}.so

%ifarch %{ix86} ppc sparc sparc64
%triggerin -- opera
%ns_plugin_install -d %{_libdir}/opera/plugins %{name}.so

%triggerun -- opera
%ns_plugin_uninstall -d %{_libdir}/opera/plugins %{name}.so
%endif

%triggerin -- konqueror
%ns_plugin_install -d %{_libdir}/kde3/plugins/konqueror %{name}.so

%triggerun -- konqueror
%ns_plugin_uninstall -d %{_libdir}/kde3/plugins/konqueror %{name}.so

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README
%attr(755,root,root) %{_plugindir}/%{name}.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayerplug-in.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayer/mplayerplug-in.types
