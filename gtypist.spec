Summary:	Program for learning typist
Summary(hu.UTF-8):	Program gépírás tanulásához
Summary(pl.UTF-8):	Program do nauki bezwzrokowego pisania na klawiaturze
Name:		gtypist
Version:	2.8.3
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/gtypist/%{name}-%{version}.tar.bz2
# Source0-md5:	43be4b69315a202cccfed0efd011d66c
Patch0:		%{name}-ncurses.patch
URL:		http://www.gnu.org/software/gtypist/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.7.7
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	ncurses-devel
BuildRequires:	texinfo
Obsoletes:	typist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program came from a desire to learn 'proper' typing.

%description -l hu.UTF-8
Ez a program a gépírás tanulásához íródott.

%description -l pl.UTF-8
Program do nauki bezwzrokowego pisania na klawiaturze. Oferuje kilka
lekcji, na razie tylko po angielsku.

%package emacs
Summary:	Emacs mode
Summary(hu.UTF-8):	Emacs mód
Group:		Applications/Editors/Emacs

%description emacs
Emacs mode.

%description emacs -l hu.UTF-8
Emacs mód.

%prep
%setup -q
%patch0 -p1

ln -sf version.texi doc/version.cs.texi
rm -f po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
%{_datadir}/%{name}

%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/gtypist*
