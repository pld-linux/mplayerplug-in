# TODO
# - plugins shouldn't be only symlinks for one file?
# - (where shoild be this file)? ______________/
# - i (glen) propose to put all netscape-compatible plugins to
#   %{_libdir}/nsplugins and all browser plugin packages symlink there. the
#   %{_libdir}/nsplugins should itself go to FHS? as if *all* NS-compatible
#   plugins go there, there's no one parent for them :), or nsplugins.spec could
#   do too, if FHS won't do.
Summary:	Embedded Video Player for Mozilla
Summary(pl):	Osadzony odtwarzacz wideo dla Mozilli
Name:		mozilla-plugin-mplayer
Version:	2.85
Release:	2
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
Summary(pl):	Wbudowany odtwarzacz klipów filmowych dla Mozilli Firefox
Group:		X11/Applications/Multimedia
PreReq:		mozilla-firefox
Requires:	mplayer >= 1.0

%description -n mozilla-firefox-plugin-mplayer
This package contains plugin for Mozilla Firefox browser.

%description -n  mozilla-firefox-plugin-mplayer -l pl
Ta paczka zawiera plugin do u¿ywania mplayera jako odtwarzacza klipów
filmowych ze stron WWW.

%package -n opera-plugin-mplayer
Summary:        Embedded Video Player for Opera
Summary(pl):    Wbudowany odtwarzacz klipów filmowych dla Opery
Group:          X11/Applications/Multimedia
PreReq:         opera
Requires:       mplayer >= 1.0

%description -n opera-plugin-mplayer
This package contains plugin for Opera browser.

%description -n  opera-plugin-mplayer -l pl
Ta paczka zawiera plugin do u¿ywania mplayera jako odtwarzacza klipów
filmowych ze stron WWW w przegladarce Opera.

%package -n konqueror-plugin-mplayer
Summary:        Embedded Video Player for Opera
Summary(pl):    Wbudowany odtwarzacz klipów filmowych dla Opery
Group:          X11/Applications/Multimedia
PreReq:         konqueror
Requires:       mplayer >= 1.0

%description -n konqueror-plugin-mplayer
This package contains plugin for konqueror browser.

%description -n  konqueror-plugin-mplayer -l pl
Ta paczka zawiera plugin do u¿ywania mplayera jako odtwarzacza klipów
filmowych ze stron WWW w przegladarce konqueror.

%prep
%setup -q -n mplayerplug-in

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/{mozilla,mozilla-firefox,opera}/plugins,%{_sysconfdir}/mplayer} \
	$RPM_BUILD_ROOT%{_libdir}/kde3/plugins/konqueror

install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla-firefox/plugins
install *.so $RPM_BUILD_ROOT%{_libdir}/opera/plugins
install *.so $RPM_BUILD_ROOT%{_libdir}/kde3/plugins/konqueror
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

%files -n opera-plugin-mplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opera/plugins/*.so

%files -n konqueror-plugin-mplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/konqueror/*.so
