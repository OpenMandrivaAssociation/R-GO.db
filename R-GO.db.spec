%global packname  GO.db
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.6.1
Release:          2
Summary:          A set of annotation maps describing the entire Gene Ontology
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              https://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core R-methods R-AnnotationDbi
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-AnnotationDbi

%description
A set of annotation maps describing the entire Gene Ontology assembled
using data from GO

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
