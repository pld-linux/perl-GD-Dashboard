%include	/usr/lib/rpm/macros.perl
%define		pdir	GD
%define		pnam	Dashboard
Summary:	GD::Dashboard Perl module - create JPEGs of meters and dials
Summary(pl):	Modu³ Perla GD::Dashboard - tworzenie JPEG-ów z licznikami i zegarami
Name:		perl-GD-Dashboard
Version:	0.04
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GD::Dashboard module aims at providing users with a quick and easy
way to create dashboard or cockpit like JPGs to display key
information.

%description -l pl
Modu³ GD::Dashboard ma za zadanie dostarczenie szybkiego i ³atwego
sposobu na tworzenie desek rozdzielczych lub kokpitów z JPEG-ami
do wy¶wietlania kluczowych informacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/GD/Dashboard.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
