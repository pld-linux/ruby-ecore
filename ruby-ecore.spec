Summary:	Ruby binding to the ecore library
Summary(pl.UTF-8):	Dowiązania języka Ruby do biblioteki ecore
Name:		ruby-ecore
Version:	0
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	%{name}.tar.gz
# Source0-md5:	2c698928f2a24e92e44fe5dedf0b4767
URL:		http://code-monkey.de/pages/ruby-efl
#BuildRequires:	setup.rb >= 3.3.1
BuildRequires:	ecore-devel
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-evas-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the ecore library.

%description -l pl.UTF-8
Dowiązania języka Ruby do biblioteki ecore.

%package devel
Summary:	Headers for ruby-ecore library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki ruby-ecore
Group:		Development/Libraries

%description devel
Headers for ruby-ecore library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki ruby-ecore.

%prep
%setup -q -n %{name}

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
