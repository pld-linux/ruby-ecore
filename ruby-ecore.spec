%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby binding to the ecore library
Summary(pl):	Dowi�zania j�zyka Ruby do biblioteki ecore
Name:		ruby-ecore
Version:	0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	ruby-ecore.tar.gz
# Source0-md5:	2c698928f2a24e92e44fe5dedf0b4767
URL:		http://code-monkey.de/projects/ruby-efl.html
BuildRequires:	rake
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	ruby-evas-devel
BuildRequires:	ecore-devel
#BuildRequires:	setup.rb = 3.3.1
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the ecore library.

%description -l pl
Dowi�zania j�zyka Ruby do biblioteki ecore.

%package devel
Summary:	Headers for ruby-ecore library
Summary(pl):	Pliki nag��wkowe do biblioteki ruby-ecore
Group:		Development/Libraries

%description devel
Headers for ruby-ecore library.

%description devel -l pl
Pliki nag��wkowe do biblioteki ruby-ecore.

%prep
%setup -q -n ruby-ecore

%build
rake

#rdoc --op rdoc ext
#rdoc --ri --op ri ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

DESTDIR=$RPM_BUILD_ROOT RUBYARCHDIR=%{ruby_archdir} rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/*.so

%files devel
%defattr(644,root,root,755)
%{ruby_archdir}/ecore
