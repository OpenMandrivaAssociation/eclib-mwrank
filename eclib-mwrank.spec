%define name		eclib-mwrank
%define eclibdir	%{_datadir}/%{name}
%define libname		%mklibname -d eclib

Name:		%{name}
Group:		Sciences/Mathematics
License:	GPL
Summary:	Mordell-Weil groups of elliptic curves over Q via 2-descent
Version:	0.20100711
Release:	%mkrel 3
Source:		eclib-20100711.tar.bz2
URL:		http://www.warwick.ac.uk/~masgaj/mwrank/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	gcc-c++
BuildRequires:	libgmp-devel
BuildRequires:	ntl-devel
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
Provides:	eclib-devel = %{version}-%{release}
Provides:	libeclib-devel = %{version}-%{release}
Obsoletes:	%mklibname -d mwrank

%description	-n %{libname}
Development header files and libraries for %{name}.

%prep
%setup -q -n eclib-20100711

%build
cd src
make	NTL_PREFIX=%{_prefix}	\
	PARI_PREFIX=%{_prefix}	\
	PICFLAG=-fPIC		\
	all so

%install
cd src
mkdir -p %{buildroot}%{_libdir}
cp -fa lib/*.so %{buildroot}%{_libdir}

mkdir -p %{buildroot}%{_includedir}/eclib
cp -far include/* %{buildroot}%{_includedir}/eclib

# create a link to the most important binary in bindir.
mkdir -p %{buildroot}%{eclibdir}/bin
mkdir -p %{buildroot}%{_bindir}
cp -fa	qrank/{mwrank,ratpoint}						\
	qcurves/{allisog,conductor,indep,findinf,tate,torsion,twist}	\
	procs/tconic							\
	%{buildroot}%{eclibdir}/bin
ln -sf %{eclibdir}/bin/mwrank %{buildroot}/%{_bindir}/mwrank

# add an "easy" link to doc directory.
ln -sf %{_docdir}/%{name} %{buildroot}/%{eclibdir}/doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mwrank
%{eclibdir}/bin/*
%{eclibdir}/doc
%doc src/qrank/mwrank.changes src/qrank/mwrank.doc src/qrank/mwrank.info
%doc src/qrank/mwrank.options src/qrank/mwrank.readme

%files		-n %{libname}
%defattr(-,root,root)
%dir %{_includedir}/eclib
%{_includedir}/eclib/*
%{_libdir}/lib*.so
