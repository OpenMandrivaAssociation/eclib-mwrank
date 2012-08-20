%define name		eclib-mwrank
%define eclibdir	%{_datadir}/%{name}
%define libeclib	%mklibname eclib 0
%define libeclib_devel	%mklibname -d eclib

Name:		%{name}
Group:		Sciences/Mathematics
License:	GPLv3+
Summary:	Mordell-Weil groups of elliptic curves over Q via 2-descent
Version:	0.20120428
Release:	1
URL:		http://www.warwick.ac.uk/~masgaj/mwrank/index.html
Source:		http://sagemath.org/packages/standard/eclib-20120428.spkg

BuildRequires:	gcc-c++
BuildRequires:	gmp-devel
BuildRequires:	ntl-devel
BuildRequires:	libpari-devel

%description
mwrank is a program written in C++ for computing Mordell-Weil groups of
elliptic curves over Q via 2-descent. It is available as source code
(licensed under GPL) in the eclib package. mwrank is now only distributed
as part of eclib. eclib is also included in Sage, and for most potential
users the easiest way to run mwrank is to install Sage (which also of
course gives you much much more). I no longer provide a source code
distribution of mwrank by itself: use eclib instead. Full source code
for eclib is available from google code.

%package	-n %{libeclib}
Group:		Sciences/Mathematics
License:	GPL
Summary:	Run time libraries for %{name}
Obsoletes:	%mklibname -d mwrank

%description	-n %{libeclib}
Run time libraries for %{name}.

%package	-n %{libeclib_devel}
Group:		Development/C
License:	GPL
Summary:	Development files for %{name}
Provides:	eclib-devel = %{version}-%{release}
Provides:	libeclib-devel = %{version}-%{release}
Requires:	%{libeclib} = %{version}-%{release}

%description	-n %{libeclib_devel}
Development header files and libraries for %{name}.

%prep
%setup -q -n eclib-20120428

%build
pushd src
    %configure2_5x --disable-static --enable-shared --disable-allprogs
    %make
popd

%install
pushd src
    %makeinstall_std
    mkdir -p %{buildroot}%{_docdir}/eclib
    cp -a AUTHORS COPYING ChangeLog NEWS README %{buildroot}%{_docdir}/eclib
popd

%check
pushd src
    make -C src check LD_LIBRARY_PATH=%{buildroot}%{_libdir}
popd

%files
%{_bindir}/*

%files		-n %{libeclib}
%doc %dir %{_docdir}/eclib
%doc %{_docdir}/eclib/AUTHORS
%doc %{_docdir}/eclib/COPYING
%doc %{_docdir}/eclib/ChangeLog
%doc %{_docdir}/eclib/NEWS
%doc %{_docdir}/eclib/README
%{_libdir}/lib*.so.*

%files		-n %{libeclib_devel}
%{_includedir}/eclib
%{_libdir}/lib*.so
