Name:           dmg2img
Version:        1.6.2
Release:        1%{?dist}
Summary:        DMG2IMG is a tool which allows converting Apple compressed dmg archives to standard (hfsplus) image disk files.

License:        GPLv2
URL:            http://vu1tur.eu.org/tools/
Source0:        http://vu1tur.eu.org/tools/%{name}-%{version}.tar.gz

BuildRequires:  bzip2-devel openssl-devel gcc

Patch1:		%{name}-%{version}-Makefile.patch

%description
DMG2IMG is a tool which allows converting Apple compressed dmg archives to standard (hfsplus) image disk files.
This tool handles zlib and bzip2 compressed dmg images.

%prep
%setup -q
%patch1 -p1 -b .Mafile-fix

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README COPYING
%{_bindir}/%{name}
%{_bindir}/vfdecrypt
%{_mandir}/1/vfdecrypt.1.gz

%changelog
* Sun May 29 2011 Alexei Panov ( elemc [AT] atisserv [DOT] ru ) - 1.6.2-1
- Initial build
