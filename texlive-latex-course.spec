Name:		texlive-latex-course
Version:	25505
Release:	1
Summary:	A LaTeX course as a projected presentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-course
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-course.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-course.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A brief Beamer-based slide presentation on LaTeX, based on
Rupprecht's LaTeX 2.09 course, which the author has translated
to English and taken to LaTeX2e/Beamer. Additional material was
taken from the Short Introduction to LaTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-course/Graphics/Ross-Siegel.png
%doc %{_texmfdistdir}/doc/latex/latex-course/Graphics/Thumbs.db
%doc %{_texmfdistdir}/doc/latex/latex-course/Graphics/campus3.png
%doc %{_texmfdistdir}/doc/latex/latex-course/LaTeX-Course.pdf
%doc %{_texmfdistdir}/doc/latex/latex-course/LaTeX-Course.tex
%doc %{_texmfdistdir}/doc/latex/latex-course/LaTeX-course.prj
%doc %{_texmfdistdir}/doc/latex/latex-course/README
%doc %{_texmfdistdir}/doc/latex/latex-course/beamercolorthemeross.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
