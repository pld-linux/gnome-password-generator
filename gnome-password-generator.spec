Summary:	GNOME Password Generator
Summary(pl):	Generator hase³ dla GNOME
Name:		gnome-password-generator
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-password/%{name}-%{version}.tar.gz
# Source0-md5:	6b65977d94bee4c7336c3efc222ed1fa
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

%description -l pl
GNOME Password Generator jest graficznym programem s³u¿±cym do
generowania bezpiecznych hase³. Pozwala on na wygenerowanie okre¶lonej
liczby losowych hase³ o okre¶lonej d³ugo¶ci.

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
%{_desktopdir}/*
%{_pixmapsdir}/*
