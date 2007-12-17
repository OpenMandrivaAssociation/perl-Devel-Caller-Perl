%define module  Devel-Caller-Perl
%define version 1.4
%define release %mkrel 1
%define	pdir	Devel

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0: 	%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/search?dist=%{module}
BuildArch: 	noarch
Requires: 	perl, perl-base, perl-Exporter-Lite
BuildRequires:	perl-devel, perl-Module-Build

%description
%{module} module for perl.  This module allows a method to get at
arguments passed to subroutines higher up in the call stack.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
# make test

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(444,root,root,755)
%doc README
%{perl_vendorlib}/Devel/Caller/*
%_mandir/man3/*

