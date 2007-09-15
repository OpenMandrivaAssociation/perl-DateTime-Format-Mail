%define realname   DateTime-Format-Mail

Name:		perl-%{realname}
Version:    0.30
Release:    %mkrel 3
License:	Artistic and GPL
Group:		Development/Perl
Summary:    Convert between DateTime and RFC2822/822 formats
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/DateTime/DateTime-Format-Mail-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel perl(Test::Pod)
BuildRequires:	perl(Module::Build)
BuildArch: noarch

%description
RFCs 2822 and 822 specify date formats to be used by email. 
This module parses and emits such dates.

RFC2822 (April 2001) introduces a slightly different format of date than that 
used by RFC822 (August 1982). The main correction is that the preferred format
is more limited, and thus easier to parse programmatically.

Despite the ease of generating and parsing perfectly valid RFC822 and RFC2822 
people still get it wrong. So this module provides four things for those 
handling mail dates:
  A strict parser that will only accept RFC2822 dates, so you can see where 
    you're right.
  A strict formatter, so you can generate the right stuff to begin with.
  A loose parser, so you can take the misbegotten output from other programs 
    and turn it into something useful. This includes various minor errors as 
    well as some somewhat more bizarre mistakes. 

%prep
%setup -q -n DateTime-Format-Mail-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

