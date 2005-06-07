# TODO
# - share the plugin with two browsers
# - add more browsers (konqueror/opera)
Summary:	Embedded Video Player for Mozilla
Summary(pl):	Osadzony odtwarzacz wideo dla Mozilli
Name:		mozilla-plugin-mplayer
Version:	2.80
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplayerplug-in/mplayerplug-in-%{version}.tar.gz
# Source0-md5:	ce3235ff7d46fae416cfb175193a5f25
URL:		http://mplayerplug-in.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mozilla-devel
BuildRequires:	pkgconfig
Requires:	mplayer >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mplayerplug-in is a browser plugin that uses mplayer to play videos
from websites.

%description -l pl
mplayerplug-in jest wtyczk± wykorzystuj±c± mplayera do odtwarzania
klipów filmowych ze stron WWW.

%package -n mozilla-firefox-plugin-mplayer
Summary:	Embedded Video Player for Mozilla Firefox
Group:		X11/Applications/Multimedia
PreReq:		mozilla-firefox
Requires:	mplayer >= 1.0

%description -n mozilla-firefox-plugin-mplayer
This package contains plugin for Mozilla Firefox browser.

%prep
%setup -q -n mplayerplug-in

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{mozilla,mozilla-firefox}/plugins,%{_sysconfdir}/mplayer}

install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla-firefox/plugins
install mplayerplug-in.conf $RPM_BUILD_ROOT%{_sysconfdir}
install mplayerplug-in.types $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayerplug-in.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayer/mplayerplug-in.types

%files -n mozilla-firefox-plugin-mplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla-firefox/plugins/*.so
