%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Dashboard
Summary:	GD::Dashboard Perl module - create JPEGs of meters and dials
Summary(pl.UTF-8):	Moduł Perla GD::Dashboard - tworzenie JPEG-ów z licznikami i zegarami
Name:		perl-GD-Dashboard
Version:	0.04
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1875cf4b9aab046e8ff43c3096859c2b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GD::Dashboard module aims at providing users with a quick and easy
way to create dashboard or cockpit like JPGs to display key
information.

%description -l pl.UTF-8
Moduł GD::Dashboard ma za zadanie dostarczenie szybkiego i łatwego
sposobu na tworzenie desek rozdzielczych lub kokpitów z JPEG-ami
do wyświetlania kluczowych informacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes readme
%{perl_vendorlib}/GD/Dashboard.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
