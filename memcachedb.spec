Summary:	distributed key-value storage system
Summary(pl.UTF-8):	rozproszony system do przechowywania par klucz-wartość
Name:		memcachedb
Version:	1.2.0
Release:	1
License:	BSD like
Group:		Applications
Source0:	http://memcachedb.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	1642242ab2108611873588b77848317b
URL:		http://www.memcachedb.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db4.7-devel
BuildRequires:	libevent-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MemcacheDB is a distributed key-value storage system designed for
persistent. It is NOT a cache solution, but a persistent storage
engine for fast and reliable key-value based object storage and
retrieval. It conforms to memcache protocol (not completed), so any
memcached client can have connectivity with it. MemcacheDB uses
Berkeley DB as a storing backend, so lots of features including
transaction and replication are supported.

%description -l pl.UTF-8
MemcacheDB to rozproszony system do przechowywania par klucz-wartość.
Nie jest to rozwiązanie typu cache, ale silnik do trwałego
przechowywania danych oraz szybkiego i wiarygodnego zapisywania i
odczytywania par klucz-wartość. System zgodny jest z protokołem
memcache (nie całkowicie), dzięki czemu dowolny klient memcached
będzie mógł się do niego podłączyć. MemcacheDB korzysta z bazy Berkley
DB jako systemu do przechowywania danych, dzieki czemu wspierana jest
funkcjonalność taka jak transakcje czy replikacje.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-threads
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install tools/*.py $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README TODO doc/protocol.txt conf/DB_CONFIG.example
%attr(755,root,root) %{_bindir}/*
