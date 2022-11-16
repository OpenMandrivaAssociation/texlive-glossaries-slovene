Name:		texlive-glossaries-slovene
Version:	51211
Release:	1
Summary:	Slovene language module for glossaries package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-slovene
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-slovene.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-slovene.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-slovene.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Slovene language module for glossaries package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/glossaries-slovene
%{_texmfdistdir}/tex/latex/glossaries-slovene
%doc %{_texmfdistdir}/doc/latex/glossaries-slovene

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
