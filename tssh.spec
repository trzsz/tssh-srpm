Name:           tssh
Version:        0.1.25
Release:        1
Summary:        Highly OpenSSH-compatible client with extended features.

License:        MIT
URL:            https://github.com/trzsz/trzsz-ssh
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang >= 1.25
BuildRequires:  git

%if 0%{?rhel} >= 8 && 0%{?rhel} <= 9 || 0%{?mageia}
%undefine _debugsource_packages
%endif

%if 0%{?openEuler} || 0%{?mageia} == 8
%define debug_package %{nil}
%endif

%description
trzsz-ssh(tssh) is a highly OpenSSH-compatible client with extended features.

%prep
%autosetup -n trzsz-ssh-%{version}

%build
%if 0%{?mageia} == 8
export GOPROXY=direct
%endif
go build -o %{_builddir}/bin/tssh ./cmd/tssh

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/bin/tssh %{buildroot}%{_bindir}/tssh

%files
%{_bindir}/tssh

%changelog
* Sun May 3 2026 Lonny Wong <lonnywong@qq.com> - 0.1.25-1
- Initial RPM spec for tssh
