#
# Conditional build:
%bcond_without	opera		# do not build without limited features: for opera
#
%ifnarch %{ix86} ppc sparc sparc64
%undefine	with_opera
%endif
Summary:	Embedded Video Player for Mozilla
Summary(pl):	Osadzony odtwarzacz wideo dla Mozilli
Name:		mplayerplug-in
Version:	3.35
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplayerplug-in/%{name}-%{version}.tar.gz
# Source0-md5:	5efa01fa433ee4c7118e534c36198e72
Patch0:		%{name}-opera.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-g_idle_add-fix.patch
Patch3:		%{name}-c.patch
URL:		http://mplayerplug-in.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	xulrunner-devel
Requires:	%{name}-common = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Obsoletes:	konqueror-plugin-mplayer
Obsoletes:	mozilla-firefox-plugin-mplayer
Obsoletes:	mozilla-plugin-mplayer
Obsoletes:	opera-plugin-mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mplayerplug-in is a browser plugin that uses mplayer to play videos
from websites.

%description -l pl
mplayerplug-in jest wtyczk± przegl±darki wykorzystuj±c± mplayera do
odtwarzania klipów filmowych ze stron WWW.

%package common
Summary:	Common files for %{name}
Summary(pl):	Wspólne pliki dla %{name}
Group:		X11/Applications/Multimedia
Requires:	mplayer >= 1:1.0-2.pre7try3

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
odtwarzania klipów filmowych ze stron WWW. Ta wtyczka jest dostosowana
do Opery.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}

# don't use --enable-x86_64 on x86_64, this builds 32-bit version on x86_64 host

%if %{with opera}
# for opera (works only with X toolkit)
%configure \
	--enable-x
%{__make}
mkdir -p opera
mv -f *.so *.xpt opera
%endif

# other (with no limited features)
%configure \
	--enable-gtk2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/opera/plugins,%{_browserpluginsdir},%{_sysconfdir}/mplayer}

%{__make} install -C po \
	DESTDIR=$RPM_BUILD_ROOT

install *.so *.xpt $RPM_BUILD_ROOT%{_browserpluginsdir}
%if %{with opera}
install opera/*.so $RPM_BUILD_ROOT%{_libdir}/opera/plugins
install opera/*.xpt $RPM_BUILD_ROOT%{_libdir}/opera/plugins
%endif
install mplayerplug-in.conf $RPM_BUILD_ROOT%{_sysconfdir}
install mplayerplug-in.types $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/*.so
%{_browserpluginsdir}/*.xpt

%files common
%defattr(644,root,root,755)
%doc ChangeLog TODO README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mplayerplug-in.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mplayer/mplayerplug-in.types

%if %{with opera}
%files opera
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opera/plugins/*.so
%{_libdir}/opera/plugins/*.xpt
%endif
