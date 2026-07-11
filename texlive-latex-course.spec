%global tl_name latex-course
%global tl_revision 68681

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2
Release:	%{tl_revision}.1
Summary:	A LaTeX course as a projected presentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-course
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-course.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-course.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A brief Beamer-based slide presentation on LaTeX, based on Rupprecht's
LaTeX 2.09 course, which the author has translated to English and taken
to LaTeX2e/Beamer. Additional material was taken from the Short
Introduction to LaTeX.

