Summary:	Program for learning typist
Summary(pl):	Program do nauki bezwzrokowego pisania na klawiaturze
Name:		gtypist
Version:	2.6.2
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ca8cd4f23d7b1a91d2c3a36596525e81
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-texinfo-fix.patch
Patch3:		%{name}-gettext.patch
Patch4:		%{name}-pl.po.patch
URL:		http://www.gnu.org/software/gtypist/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6.3
BuildRequires:	gettext-devel >= 0.11
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	typist

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
%patch4 -p1

%build
rm -f missing
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
