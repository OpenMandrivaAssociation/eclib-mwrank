%define name		eclib-mwrank
%define libname		%mklibname -d mwrank
%define mwrankdir	%{_datadir}/%{name}

Name:		%{name}
Group:		Sciences/Mathematics
License:	GPL
Summary:	Mordell-Weil groups of elliptic curves over Q via 2-descent
Version:	0.20080720
Release:	1
Source:		http://www.warwick.ac.uk/~masgaj/ftp/progs/mwrank-2008-07-20.tgz
URL:		http://www.warwick.ac.uk/~masgaj/mwrank/index.html

BuildRequires:	gcc-c++
BuildRequires:	libgmp-devel
BuildRequires:	libntl-devel
BuildRequires:	libpari-devel

%description
mwrank:
    Computes Mordell-Weil groups of elliptic curves over Q via 2-descent.
conductor:
    Computes conductor of input curves.
tate:
    Computes conductor and local reduction data of input curves.
torsion:
    Computes torsion subgroup of input curves.
indep:
    Tests points for independence.
findinf:
    Search for points on a curve, followed by saturation. One can also
  input known points so this can be used to saturate a known set of points.
allisog:
    Computes curves isogenous to input curves.
twist:
    Computes quadratic twists of input curves.
ratpoint:
    Search for points on a quartic y2=g(x) (viewed as a 2-cover of
  its Jacobian) after testing for local solubility. Points found are
  mapped to the Jacobian via the 2-covering map. This is intended
  mainly for further processing of quartics output by mwrank.

%package	-n %{libname}
Group:		Development/C
License:	GPL
Summary:	Development files for %{name}

%description	-n %{libname}
Development header files and libraries for %{name}.

%prep
%setup -q -n mwrank-2008-07-20

%build
BASE=%{_prefix} %configure --with-pari=%{_prefix} --with-ntl_all=%{_prefix}

%ifnarch %{ix86}
perl -pi -e 's|/lib|/%{_lib}|;' Makefile
%endif

%make

%install
mkdir -p %{buildroot}%{_libdir}
make PREFIX=%{buildroot}%{_prefix} install

# create a link to the most important binary in bindir.
mkdir -p %{buildroot}%{mwrankdir}/bin
mkdir -p %{buildroot}%{_bindir}
cp -fa mwrank conductor tate torsion indep findinf allisog twist ratpoint \
	%{buildroot}%{mwrankdir}/bin
ln -sf %{mwrankdir}/bin/mwrank %{buildroot}/%{_bindir}/mwrank

# add an "easy" link to doc directory.
ln -sf %{_docdir}/%{name} %{buildroot}/%{mwrankdir}/doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mwrank
%{mwrankdir}/bin/*
%{mwrankdir}/doc
%doc mwrank.changes mwrank.doc mwrank.info mwrank.options mwrank.readme
%doc README PRIMES

%files		-n %{libname}
%defattr(-,root,root)
%dir %{_includedir}/mwrank
%{_includedir}/mwrank/*
%{_libdir}/libmwrank.*
