Summary:	Embedded Video Player for Mozilla
Summary(pl):	Osadzony odtwarzacz wideo dla Mozilli
Name:		mozilla-plugin-mplayer
Version:	0.80
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplayerplug-in/mplayerplug-in-%{version}.tar.gz
# Source0-md5:	2ee4b6572758566d7079a7a06903a5fb
Source1:	http://dl.sourceforge.net/mplayerplug-in/mini.tar.bz2
# Source1-md5:	051bee1ba7f4f20b5a94cb444b5dfe80
URL:		http://mplayerplug-in.sourceforge.net/
Requires:	mplayer >= 0.90rc4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mplayerplug-in is a browser plugin that uses mplayer to play videos
from websites.

%description -l pl
mplayerplug-in jest wtyczk± wykorzystuj±c± mplayera do odtwarzania
klipów filmowych ze stron www.

%prep
%setup -q -n mplayerplug-in -a1

echo "use-gui=yes" > mplayerplug-in.conf

cd mini
mv README ../README-skin_mini

%build
%{__make} \
	CC="%{__cc}" \
	OPTIMIZER="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mozilla/plugins,%{_sysconfdir},%{_datadir}/mplayer/Skin/mini}

install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install mplayerplug-in.conf $RPM_BUILD_ROOT%{_sysconfdir}
install mini/{skin,*.png} $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin/mini

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README README-skin_mini
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_datadir}/mplayer/Skin/mini
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayerplug-in.conf
