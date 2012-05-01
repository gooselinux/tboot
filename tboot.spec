%define alphatag 20110714

Summary:        Performs a verified launch using Intel TXT
Name:           tboot
Version:        1.5.0
Release:        0.1.%{alphatag}%{?dist}

Group:          System Environment/Base
License:        BSD
URL:            http://sourceforge.net/projects/tboot/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{alphatag}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  trousers-devel
BuildRequires:  openssl-devel
ExclusiveArch:  %{ix86} x86_64


%description
Trusted Boot (tboot) is an open source, pre-kernel/VMM module that uses
Intel Trusted Execution Technology (Intel TXT) to perform a measured
and verified launch of an OS kernel/VMM.

%prep
%setup -q -n %{name}-%{alphatag}


%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
make debug=y %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make debug=y DISTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING docs/* lcptools/lcptools2.txt lcptools/Linux_LCP_Tools_User_Manual.pdf
%{_sbindir}/acminfo
%{_sbindir}/lcp_crtpconf
%{_sbindir}/lcp_crtpol
%{_sbindir}/lcp_crtpol2
%{_sbindir}/lcp_crtpolelt
%{_sbindir}/lcp_crtpollist
%{_sbindir}/lcp_mlehash
%{_sbindir}/lcp_readpol
%{_sbindir}/lcp_writepol
%{_sbindir}/parse_err
%{_sbindir}/tb_polgen
%{_sbindir}/tpmnv_defindex
%{_sbindir}/tpmnv_getcap
%{_sbindir}/tpmnv_lock
%{_sbindir}/tpmnv_relindex
%{_sbindir}/txt-stat
/boot/tboot.gz
/boot/tboot-syms


%changelog
* Wed Jul 27 2011 David Cantrell <dcantrell@redhat.com> - 1.5.0-0.1.20110714-1
- Intel uploaded a new snapshot, fix the version and release to match guidelines
  Related: rhbz#691617

* Mon Jul 25 2011 David Cantrell <dcantrell@redhat.com> - 20110429-1
- Import from F15
  Resolves: rhbz#691617

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 1 2010 Joseph Cihula <joseph.cihula@intel.com> - 20101005-1.fc13
- Initial import
