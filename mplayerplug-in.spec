Summary:	Embedded Video Player for Mozilla
Summary(pl):	Osadzony odtwarzacz wideo dla Mozilli
Name:		mozilla-plugin-mplayer
Version:	0.40
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.sf.net/mplayerplug-in/mplayerplug-in_v%{version}.tar.gz
Source1:	http://download.sf.net/mplayerplug-in/mini.tar.bz2
URL:		http://mplayerplug-in.sourceforge.net/
Requires:	mplayer >= 0.90rc4
#BuildRequires:	mozilla-embedded-devel
#PreReq:		mozilla-embedded
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mplayerplug-in is a browser plugin that uses mplayer to play
videos from websites.

%description -l pl
mplayerplug-in jest wtyczk± wykorzystuj±c± mplayera do odtwarzania
klipów filmowych ze stron www. 

%prep
%setup -q -n mplayerplug-in -a1

touch mplayerplug-in.conf

%build
%{__make} \
	CC="%{__cc}" \
	OPTIMIZER="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mozilla/plugins,%{_sysconfdir}}

install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
install mplayerplug-in.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayerplug-in.conf
