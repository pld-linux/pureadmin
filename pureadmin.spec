Summary:	Tool for management PureFTPd
Summary(pl):	Narzêdzie do zarz±dzania PureFTPd
Name:		pureadmin
Version:	0.1.12
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/purify/%{name}-%{version}.tar.gz
# Source0-md5:	b5eef80754af063b188880bdbc98ec71
URL:		http://purify.sourceforge.net/
BuildRequires:	fam-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PureAdmin is a graphical tool used to make the management of PureFTPd
a little easier. It uses the GTK+2.x widgets for its GUI and thus are
not dependent on a specific desktop environment such as GNOME or KDE.
It is, however, designed with the GNOME Human Interface Guidelines in
mind so it should integrate nicely with at least GNOME.

%description -l pl
PureAdmin jest graficznym narzêdziem do zarz±dzania serwerem PureFTPd.
U¿ywa widgetów GTK+2, dziêki czemu nie jest zale¿ne od konkretnego
¶rodowiska, jak GNOME czy KDE. Jest jednak zaprojektowane zgodnie z
zaleceniami GNOME Human Interface Guidelines, aby ³adnie integrowa³o
siê przynajmniej z GNOME.

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
