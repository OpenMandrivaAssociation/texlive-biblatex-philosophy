# revision 26219
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-philosophy
# catalog-date 2012-05-05 15:20:56 +0200
# catalog-license lppl1.3
# catalog-version 0.8b
Name:		texlive-biblatex-philosophy
Version:	0.8b
Release:	1
Summary:	Styles for using biblatex for work in philosophy
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-philosophy
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The packages offers two styles philosophy-classic and
philosophy-modern, that facilitate the production of produce
two different kinds of bibliography, based on the authoryear
style, with options and features to manage the information
about the translation of foreign texts or their reprints.
Though the package's default settings are based on the
conventions used in Italian publications, these styles can be
used with every language recognized by babel, possibly with
some simple redefinitions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-philosophy/english-philosophy.lbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/italian-philosophy.lbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-classic.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-classic.cbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-modern.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-modern.cbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-standard.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-verbose.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy/README
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy/Test-philosophy-classic.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy/Test-philosophy-modern.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy/Test-philosophy-verbose.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy/biblatex-philosophy.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy/biblatex-philosophy.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy/biblatex-philosophy.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
