Summary:	Tool for management PureFTPd
Summary(pl):	Narz�dzie do zarz�dzania PureFTPd
Name:		pureadmin
Version:	0.1.10
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/purify/%{name}-%{version}.tar.gz
# Source0-md5:	bc243bfcec09574a6e416f9468a982e0
URL:		http://purify.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PureAdmin is a graphical tool used to make the management of PureFTPd
a little easier. It uses the GTK+2.x widgets for its GUI and thus are
not dependent on a specific desktop environment such as GNOME or KDE.
It is, however, designed with the GNOME Human Interface Guidelines in
mind so it should integrate nicely with at least GNOME.

%description -l pl
PureAdmin jest graficznym narz�dziem do zarz�dzania serwerem PureFTPd.
U�ywa widget�w GTK+2, dzi�ki czemu nie jest zale�ne od konkretnego
�rodowiska, jak GNOME czy KDE. Jest jednak zaprojektowane zgodnie z
zaleceniami GNOME Human Interface Guidelines, aby �adnie integrowa�o
si� przynajmniej z GNOME.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_desktopdir}/%{name}

install src/pureadmin $RPM_BUILD_ROOT%{_bindir}
install tools/pureadminsearch $RPM_BUILD_ROOT%{_bindir}
install tools/pureadmin.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.Hacking NEWS AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/pureadmin.desktop
