%global tl_name bookcover
%global tl_revision 77334

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.9
Release:	%{tl_revision}.1
Summary:	A class for book covers and dust jackets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bookcover
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookcover.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookcover.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bookcover.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class helps typesetting book covers and dust jackets.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bookcover
%dir %{_datadir}/texmf-dist/source/latex/bookcover
%dir %{_datadir}/texmf-dist/tex/latex/bookcover
%dir %{_datadir}/texmf-dist/doc/latex/bookcover/figures
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/README
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/bookcover-example1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/bookcover-example1.tex
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/bookcover-example2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/bookcover-example2.tex
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/bookcover.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-barcode.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-bg.jpg
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-cards.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-description.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-dice.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-dustjacket.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-foldingmargin.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-margins.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-newpart.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-parts.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-pi.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-ruler.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-scheme-foldingmargin.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-scheme-widthflaps.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-scheme-withflaps.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-scheme-withoutflaps.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-showonly.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-tikz.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-tikzclip.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bookcover/figures/bookcover-trimming.pdf
%doc %{_datadir}/texmf-dist/source/latex/bookcover/bookcover.dtx
%doc %{_datadir}/texmf-dist/source/latex/bookcover/bookcover.ins
%{_datadir}/texmf-dist/tex/latex/bookcover/bookcover.cls
