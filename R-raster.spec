#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-raster
Version  : 3.0.7
Release  : 27
URL      : https://cran.r-project.org/src/contrib/raster_3.0-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/raster_3.0-7.tar.gz
Summary  : Reading, writing, manipulating, analyzing and modeling of gridded spatial data.
Group    : Development/Tools
License  : GPL-3.0
Requires: R-raster-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-sp
BuildRequires : R-Rcpp
BuildRequires : R-sp
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-raster package.
Group: Libraries

%description lib
lib components for the R-raster package.


%prep
%setup -q -c -n raster

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569616547

%install
export SOURCE_DATE_EPOCH=1569616547
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library raster
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library raster
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library raster
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc raster || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/raster/DESCRIPTION
/usr/lib64/R/library/raster/INDEX
/usr/lib64/R/library/raster/Meta/Rd.rds
/usr/lib64/R/library/raster/Meta/features.rds
/usr/lib64/R/library/raster/Meta/hsearch.rds
/usr/lib64/R/library/raster/Meta/links.rds
/usr/lib64/R/library/raster/Meta/nsInfo.rds
/usr/lib64/R/library/raster/Meta/package.rds
/usr/lib64/R/library/raster/Meta/vignette.rds
/usr/lib64/R/library/raster/NAMESPACE
/usr/lib64/R/library/raster/R/raster
/usr/lib64/R/library/raster/R/raster.rdb
/usr/lib64/R/library/raster/R/raster.rdx
/usr/lib64/R/library/raster/doc/Raster.R
/usr/lib64/R/library/raster/doc/Raster.Rnw
/usr/lib64/R/library/raster/doc/Raster.pdf
/usr/lib64/R/library/raster/doc/functions.Rnw
/usr/lib64/R/library/raster/doc/functions.pdf
/usr/lib64/R/library/raster/doc/index.html
/usr/lib64/R/library/raster/doc/rasterfile.Rnw
/usr/lib64/R/library/raster/doc/rasterfile.pdf
/usr/lib64/R/library/raster/external/countries.rds
/usr/lib64/R/library/raster/external/lux.dbf
/usr/lib64/R/library/raster/external/lux.prj
/usr/lib64/R/library/raster/external/lux.rds
/usr/lib64/R/library/raster/external/lux.shp
/usr/lib64/R/library/raster/external/lux.shx
/usr/lib64/R/library/raster/external/rlogo.grd
/usr/lib64/R/library/raster/external/rlogo.gri
/usr/lib64/R/library/raster/external/test.grd
/usr/lib64/R/library/raster/external/test.gri
/usr/lib64/R/library/raster/help/AnIndex
/usr/lib64/R/library/raster/help/aliases.rds
/usr/lib64/R/library/raster/help/paths.rds
/usr/lib64/R/library/raster/help/raster.rdb
/usr/lib64/R/library/raster/help/raster.rdx
/usr/lib64/R/library/raster/html/00Index.html
/usr/lib64/R/library/raster/html/R.css
/usr/lib64/R/library/raster/tests/testthat.R
/usr/lib64/R/library/raster/tests/testthat/test-rasterize.R
/usr/lib64/R/library/raster/tests/testthat/test-sf-coercion.R
/usr/lib64/R/library/raster/tests/testthat/test-subset.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/raster/libs/raster.so
/usr/lib64/R/library/raster/libs/raster.so.avx2
/usr/lib64/R/library/raster/libs/raster.so.avx512
