Summary:	Program for learning typist
Summary(pl):	Program do nauki bezwzrokowego pisania na klawiaturze
Name:		gtypist
Version:	2.7
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://gtypist.org/releases/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	200d42de9a0070866d88116112370f0a
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-texinfo-fix.patch
Patch3:		%{name}-pl.po.patch
URL:		http://www.gnu.org/software/gtypist/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7.7
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	ncurses-devel
BuildRequires:	texinfo
BuildRequires:	xemacs
BuildRequires:	xemacs-fsf-compat-pkg
BuildRequires:	xemacs-sh-script-pkg
Obsoletes:	typist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program came from a desire to learn 'proper' typing.

%description -l pl
Program do nauki bezwzrokowego pisania na klawiaturze. Oferuje kilka
lekcji, na razie tylko po angielsku.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
%{_datadir}/%{name}
