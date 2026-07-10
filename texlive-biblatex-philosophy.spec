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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers two styles - philosophy-classic and philosophy-modern
- that facilitate the production of two different kinds of bibliography,
based on the authoryear style, with options and features to manage the
information about the translation of foreign texts or their reprints.
Though the package's default settings are based on the conventions used
in Italian publications, these styles can be used with every language
recognized by babel, possibly with some simple redefinitions.

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
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-philosophy
%dir %{_datadir}/texmf-dist/source/latex/biblatex-philosophy
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-philosophy
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-philosophy/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-philosophy/biblatex-philosophy.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-philosophy/examples.zip
%doc %{_datadir}/texmf-dist/source/latex/biblatex-philosophy/biblatex-philosophy.bib
%doc %{_datadir}/texmf-dist/source/latex/biblatex-philosophy/biblatex-philosophy.dtx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/english-philosophy.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/french-philosophy.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/italian-philosophy.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/philosophy-classic.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/philosophy-classic.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/philosophy-modern.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/philosophy-modern.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/philosophy-standard.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/philosophy-verbose.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/philosophy-verbose.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-philosophy/spanish-philosophy.lbx
