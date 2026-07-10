%global tl_name biblatex-philosophy
%global tl_revision 64414

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.8g
Release:	%{tl_revision}.1
Summary:	Styles for using BibLaTeX for work in philosophy
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-philosophy
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers two styles - philosophy-classic and philosophy-modern
- that facilitate the production of two different kinds of bibliography,
based on the authoryear style, with options and features to manage the
information about the translation of foreign texts or their reprints.
Though the package's default settings are based on the conventions used
in Italian publications, these styles can be used with every language
recognized by babel, possibly with some simple redefinitions.

