Summary:	ACL and L2CAP session handlers
Summary(pl):	Obs³uga sesji ACL i L2CAP
Name:		bluez-qube
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
URL:		http://bluez.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACL and L2CAP session handlers.

%description -l pl
Obs³uga sesji ACL i L2CAP.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# temporary - programs are noinst now...
install -d $RPM_BUILD_ROOT%{_sbindir}
install aclsession l2session $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
# docs are just copied from hcidump...
#%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/*
