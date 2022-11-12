Name:		texlive-biblatex-philosophy
Version:	64414
Release:	1
Summary:	Styles for using biblatex for work in philosophy
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-philosophy
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.r64414.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.doc.r64414.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-philosophy.source.r64414.tar.xz
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
%{_texmfdistdir}/tex/latex/biblatex-philosophy
%doc %{_texmfdistdir}/doc/latex/biblatex-philosophy
#- source
%doc %{_texmfdistdir}/source/latex/biblatex-philosophy

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
