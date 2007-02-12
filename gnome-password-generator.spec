Summary:	GNOME Password Generator
Summary(pl.UTF-8):   Generator haseł dla GNOME
Name:		gnome-password-generator
Version:	1.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-password/%{name}-%{version}.tar.gz
# Source0-md5:	a2a043a93ce04f3bb798afded8bfd329
URL:		http://gnome-password.sourceforge.net/
Requires:	python-gnome >= 2.0.0
Requires:	python-gnome-ui >= 2.0.0
Requires:	python-pygtk-gtk >= 2.2.0
Requires:	python-pygtk-pango >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Password Generator is a GUI based secure password generator. It
allows the user to generate a specified number of random passwords of
a specified length.

%description -l pl.UTF-8
GNOME Password Generator jest graficznym programem służącym do
generowania bezpiecznych haseł. Pozwala on na wygenerowanie określonej
liczby losowych haseł o określonej długości.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
