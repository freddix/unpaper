Summary:	Post-processing scanned and photocopied book pages
Name:		unpaper
Version:	5.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/Flameeyes/unpaper/archive/%{name}-%{version}.tar.gz
# Source0-md5:	0173ca8e6627865c09932674e77b6dd9
URL:		https://github.com/Flameeyes/unpaper
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unpaper is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously
created photocopies. The main purpose is to make scanned book pages
better readable on screen after conversion to PDF.
Additionally, unpaper might be useful to enhance the quality
of scanned pages before performing optical character recognition (OCR).

%prep
%setup -qn %{name}-unpaper-%{version}

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	PNGTOPNM=%{_bindir}/pngtopnm	\
	PNMTOPNG=%{_bindir}/pnmtopng	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/unpaper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO doc
%attr(755,root,root) %{_bindir}/unpaper
%{_mandir}/man1/unpaper.1*

