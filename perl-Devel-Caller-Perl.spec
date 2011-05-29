%define upstream_name    Devel-Caller-Perl
%define upstream_version 1.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0: 	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Module::Build)

BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

Requires: 	perl(Exporter::Lite)

%description
%{upstream_name} module for perl.  This module allows a method to get at
arguments passed to subroutines higher up in the call stack.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(444,root,root,755)
%doc README
%{perl_vendorlib}/Devel/Caller/*
%_mandir/man3/*
