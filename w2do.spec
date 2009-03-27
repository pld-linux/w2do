Summary:	A commandline todo manager
Summary(pl.UTF-8):	Konsolowy menadżer rzeczy do zrobienia
Name:		w2do
Version:	2.2.1
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://w2do.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	1d323bbf039210661da0a3592c0c42d6
Patch0:		%{name}-Makefile.patch
URL:		http://w2do.blackened.cz/
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
w2do is a simple-to-use commandline todo manager. It can export to
HTML 4.01 Strict and plain text.

%description -l pl.UTF-8
w2do to prosty w użyciu konsolowy menadżer rzeczy do zrobienia.
Umożliwa eksport do HTML 4.01 Strict jak również do zwykłego
tekstu.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} prefix="%{_prefix}" install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/w2*
%{_mandir}/man1/w2*.1*
