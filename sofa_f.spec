%define debug_package %{nil}

Name:           sofa_f
Version:        20210512
Release:        1%{?dist}
Summary:        SOFA Library for Fortran 77.

License:        IAU
Source0:        http://www.iausofa.org/2021_0512_F/%{name}-%{version}.tar.gz
 
BuildRequires:  gcc-gfortran

%description
Issue 2021-05-12 is the fifteenth release of the SOFA Library for Fortran 77.

%prep
%setup -q -n sofa

%build
cd %{version}/f77/src
sed -i 's@INSTALL_DIR = $(HOME)@INSTALL_DIR = %{buildroot}/usr@g' makefile
make

%install
rm -rf %{buildroot}
cd %{version}/f77/src
make test

%files
/usr/lib/libsofa.a

%changelog
* Tue Dec 14 2021 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 20210512-1
- Initial package.
