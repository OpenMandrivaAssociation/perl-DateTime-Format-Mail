%define upstream_name    DateTime-Format-Mail
%define upstream_version 0.3001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:    Convert between DateTime and RFC2822/822 formats
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(DateTime)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
