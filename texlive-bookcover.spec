Name:		texlive-bookcover
Version:	70872
Release:	1
Summary:	A class for book covers and dust jackets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bookcover
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookcover.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookcover.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bookcover.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class helps typesetting book covers and dust jackets.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bookcover
%{_texmfdistdir}/tex/latex/bookcover
%doc %{_texmfdistdir}/doc/latex/bookcover

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
