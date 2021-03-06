Summary:	Tool for management PureFTPd
Summary(pl.UTF-8):	Narzędzie do zarządzania PureFTPd
Name:		pureadmin
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/purify/%{name}-%{version}.tar.gz
# Source0-md5:	f7dc9fc7163b957bbcec1d4b2eec196d
URL:		http://purify.sourceforge.net/
BuildRequires:	fam-devel
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PureAdmin is a graphical tool used to make the management of PureFTPd
a little easier. It uses the GTK+2.x widgets for its GUI and thus are
not dependent on a specific desktop environment such as GNOME or KDE.
It is, however, designed with the GNOME Human Interface Guidelines in
mind so it should integrate nicely with at least GNOME.

%description -l pl.UTF-8
PureAdmin jest graficznym narzędziem do zarządzania serwerem PureFTPd.
Używa widgetów GTK+2, dzięki czemu nie jest zależne od konkretnego
środowiska, jak GNOME czy KDE. Jest jednak zaprojektowane zgodnie z
zaleceniami GNOME Human Interface Guidelines, aby ładnie integrowało
się przynajmniej z GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pureadmin
%{_desktopdir}/pureadmin.desktop
%{_pixmapsdir}/pureadmin.png
