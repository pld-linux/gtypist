Summary:	Program for learning typist	
Summary(pl):	Program do nauki bezwzrokowego pisania na klawiaturze
Name:		gtypist
Version:	2.4.1
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
URL:		http://www.gnu.org/software/gtypist
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
BuildRequires:	automake
Provides:	typist
Obsoletes:	typist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program came from a desire to learn 'proper' typing.

%description -l pl
Program do nauki bezwzrokowego pisania na klawiaturze. Oferuje kilka
lekcji, na razie tylko po angielsku.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS NEWS TODO THANKS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_datadir}/%{name}
