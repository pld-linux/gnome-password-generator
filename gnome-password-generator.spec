Summary:	GNOME Password Generator
Summary(pl):	Generator hase³ dla GNOME
Name:		gnome-password-generator
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-password/%{name}-%{version}.tar.gz
# Source0-md5:	d8dfba62efd71f7aed96fed60b162f8d
URL:		http://gnome-password.sourceforge.net/
Requires:	python-gnome
Requires:	python-gnome-ui
Requires:	python-pygtk-gtk
Requires:	python-pygtk-pango
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.svg $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
