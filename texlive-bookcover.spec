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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class helps typesetting book covers and dust jackets.

