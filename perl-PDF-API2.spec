#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PDF
%define		pnam	API2
Summary:	PDF::API2 - PDF Creation/Modification
Summary(pl.UTF-8):	PDF::API2 - tworzenie i modyfikowanie dokumentów PDF
Name:		perl-PDF-API2
Version:	0.51
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PDF/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83fa3694ed289493c6ffead473f62a19
URL:		http://search.cpan.org/dist/PDF-API2/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-Zlib
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is 'The Next Generation' of Text::PDF::API which initially
provided a nice API around the Text::PDF::* modules created by Martin
Hosken.

%description -l pl.UTF-8
Ten moduł to "nowa generacja" Text::PDF::API, początkowo
udostępniającego ładne API obudowujące moduły Text::PDF::*, napisane
przez Martina Hoskena.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/PDF
%dir %{perl_vendorlib}/PDF/API2
%dir %{perl_vendorlib}/PDF/API2/Resource
%dir %{perl_vendorlib}/PDF/API2/Resource/XObject
%dir %{perl_vendorlib}/PDF/API2/Resource/XObject/Form
%dir %{perl_vendorlib}/PDF/API2/Resource/XObject/Form/BarCode
%dir %{perl_vendorlib}/PDF/API2/Resource/XObject/Image
%dir %{perl_vendorlib}/PDF/API2/Resource/Font
%dir %{perl_vendorlib}/PDF/API2/Resource/Font/CoreFont
%dir %{perl_vendorlib}/PDF/API2/Resource/ColorSpace
%dir %{perl_vendorlib}/PDF/API2/Resource/ColorSpace/Indexed
%dir %{perl_vendorlib}/PDF/API2/Resource/CIDFont
%dir %{perl_vendorlib}/PDF/API2/Resource/CIDFont/CJKFont
%dir %{perl_vendorlib}/PDF/API2/Resource/CIDFont/CMap
%dir %{perl_vendorlib}/PDF/API2/Resource/CIDFont/TrueType
%dir %{perl_vendorlib}/PDF/API2/Basic
%dir %{perl_vendorlib}/PDF/API2/Basic/TTF
%dir %{perl_vendorlib}/PDF/API2/Basic/TTF/Mort
%dir %{perl_vendorlib}/PDF/API2/Basic/TTF/Kern
%dir %{perl_vendorlib}/PDF/API2/Basic/PDF
%dir %{perl_vendorlib}/PDF/API2/Content
%{perl_vendorlib}/PDF/API2.pm
%{perl_vendorlib}/PDF/API2/*.pm
%{perl_vendorlib}/PDF/API2/Resource/*.pm
%{perl_vendorlib}/PDF/API2/Resource/*.txt
%{perl_vendorlib}/PDF/API2/Resource/XObject/*.pm
%{perl_vendorlib}/PDF/API2/Resource/XObject/Form/*.pm
%{perl_vendorlib}/PDF/API2/Resource/XObject/Form/BarCode/*.pm
%{perl_vendorlib}/PDF/API2/Resource/XObject/Image/*.pm
%{perl_vendorlib}/PDF/API2/Resource/Font/*.pm
%{perl_vendorlib}/PDF/API2/Resource/Font/CoreFont/*.pm
%{perl_vendorlib}/PDF/API2/Resource/ColorSpace/*.pm
%{perl_vendorlib}/PDF/API2/Resource/ColorSpace/Indexed/*.pm
%{perl_vendorlib}/PDF/API2/Resource/CIDFont/*.pm
%{perl_vendorlib}/PDF/API2/Resource/CIDFont/CJKFont/*.pm
%{perl_vendorlib}/PDF/API2/Resource/CIDFont/CMap/*.pm
%{perl_vendorlib}/PDF/API2/Resource/CIDFont/TrueType/*.pm
%{perl_vendorlib}/PDF/API2/Basic/TTF/*.pm
%{perl_vendorlib}/PDF/API2/Basic/TTF/Mort/*.pm
%{perl_vendorlib}/PDF/API2/Basic/TTF/Kern/*.pm
%{perl_vendorlib}/PDF/API2/Basic/PDF/*.pm
%{perl_vendorlib}/PDF/API2/Content/*.pm
# and most important
%{perl_vendorlib}/PDF/API2/HOWTO.pod
