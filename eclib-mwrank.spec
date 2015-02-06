%define			with_allprogs 0
%define libold		%mklibname eclib 0
%define libold_devel	%mklibname -d eclib
%define libold2		%mklibname mwrank
%define libec		%mklibname ec 0
%define libec_devel	%mklibname -d ec

Name:		eclib-mwrank
Version:	20120830
Release:	8
Summary:	Library for Computations on Elliptic Curves
Group:		Sciences/Mathematics
License:	GPLv3+
URL:		http://www.warwick.ac.uk/~masgaj/
Source0: 	http://sagemath.org/packages/standard/eclib-%{version}.spkg

BuildRequires:	gmp-devel
BuildRequires:	libtool
BuildRequires:	ntl-devel
BuildRequires:	libpari-devel

%description
John Cremona's programs for enumerating and computating with elliptic
curves defined over the rational numbers.

%package	-n %{libec}
Group:		Sciences/Mathematics
Summary:	Library for Computations on Elliptic Curves
# bogus but required for clean updates
%rename		%{libold}
%rename		%{libold2}

%description	-n %{libec}
John Cremona's programs for enumerating and computating with elliptic
curves defined over the rational numbers.

%package	-n %{libec_devel}
Group:		Development/C++
Summary:	Development files for %{name}
Requires:	%{libec} = %{EVRD}
%rename		%{libold_devel}
%rename		eclib-devel
%rename		libeclib-devel

%description	-n %{libec_devel}
Development header files and libraries for %{name}.

%prep
%setup -q -n eclib-%{version}
# do not want rpath
pushd src
    rm -f ltmain.sh
    libtoolize
    autoreconf
popd

%build
pushd src
    %configure \
	--disable-static \
	--enable-shared \
%if %{with_allprogs}
	--enable-allprogs
%else
	--disable-allprogs
%endif
    make %{?_smpflags}
popd

%install
make DESTDIR=%{buildroot} -C src install
rm -f %{buildroot}%{_libdir}/*.la
cp -p src/AUTHORS src/COPYING src/NEWS src/README \
    %{buildroot}%{_docdir}/eclib
%if !%{with_allprogs}
rm %{buildroot}%{_docdir}/eclib/progs.txt
%endif

%check
make -C src check LD_LIBRARY_PATH=%{buildroot}%{_libdir}

%files
%{_bindir}/mwrank
%{_mandir}/man1/mwrank.1*

%files		-n %{libec}
%doc %{_docdir}/eclib
%{_libdir}/libec.so.*

%files		-n %{libec_devel}
%{_includedir}/eclib
%{_libdir}/libec.so

%changelog
* Mon Jan 28 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 20120830-1
- Update to latest upstream release.

* Thu Nov 11 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.20100711-2mdv2011.0
+ Revision: 595920
- Rebuild with newer pari

* Fri Sep 24 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.20100711-1mdv2011.0
+ Revision: 580817
- Update to newer upstream version

* Wed Mar 24 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.20080720.p10-1mdv2010.1
+ Revision: 527310
- Update to latest upstream release

* Fri Feb 26 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.20080720-6mdv2010.1
+ Revision: 512142
- Update to sagemath patchlevel 9 tarball.

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 0.20080720-5mdv2010.1
+ Revision: 503701
- rebuild for new gmp

* Tue Jan 26 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.20080720-4mdv2010.1
+ Revision: 496885
- Update to sagemath patchlevel 8 tarball.

* Thu May 14 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.20080720-3mdv2010.0
+ Revision: 375747
+ rebuild (emptylog)

* Mon May 11 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.20080720-2mdv2010.0
+ Revision: 374859
- Update to version distributed with sage math, and use the sage math
  naming convention.

* Tue Mar 10 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.20080720-1mdv2009.1
+ Revision: 353350
- Initial import of eclib-mwrank.
  http://www.warwick.ac.uk/~masgaj/mwrank/index.html.
- eclib-mwrank

