#
# Conditional build:
%bcond_without	emacs	# Emacs mode
#
Summary:	Program for learning typist
Summary(hu.UTF-8):	Program gépírás tanulásához
Summary(pl.UTF-8):	Program do nauki bezwzrokowego pisania na klawiaturze
Name:		gtypist
Version:	2.8.5
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/gtypist/%{name}-%{version}.tar.bz2
# Source0-md5:	fdc223e29288cde265f67bec455a6d8b
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-info.patch
URL:		http://www.gnu.org/software/gtypist/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8.2
%{?with_emacs:BuildRequires:	emacs}
BuildRequires:	gettext-devel >= 0.12.1
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
Summary:	Emacs mode for editing gtypist's .typ files
Summary(pl.UTF-8):	Tryb Emacsa do edycji plików .typ gtypista
Group:		Applications/Editors/Emacs
# doesn't require gtypist itself

%description emacs
Emacs mode for editing gtypist's .typ files.

%description emacs -l pl.UTF-8
Tryb Emacsa do edycji plików .typ gtypista.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__rm} po/stamp-po

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

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QUESTIONS README THANKS TODO
%attr(755,root,root) %{_bindir}/gtypist
%attr(755,root,root) %{_bindir}/typefortune
%{_datadir}/%{name}
%{_mandir}/man1/gtypist.1*
%{_mandir}/man1/typefortune.1*
%{_infodir}/gtypist.info*
%lang(cs) %{_infodir}/gtypist.cs.info*

%if %{with emacs}
%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/gtypist-mode.el*
%endif
