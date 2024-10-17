%define upstream_name    Devel-Caller-Perl
%define upstream_version 1.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary: 	%{upstream_name} module for perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}/
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


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.400.0-2mdv2011.0
+ Revision: 681396
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2011.0
+ Revision: 504940
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-4mdv2010.0
+ Revision: 430408
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.4-3mdv2009.0
+ Revision: 241206
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.4-1mdv2008.0
+ Revision: 67611
- use %%mkrel


* Tue Feb 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4

* Wed Apr 16 2003 Peter Chen <petechen@netilla.com> 1.3-1mdk
- Initial packaging.

