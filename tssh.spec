Name:           tssh
Version:        0.1.26
Release:        1
Summary:        Highly OpenSSH-compatible client with extended features.

License:        MIT
URL:            https://trzsz.github.io/tssh
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang-bin >= 1.25

%undefine _debugsource_packages
%define debug_package %{nil}

%description
trzsz-ssh(tssh) is a highly OpenSSH-compatible client with extended features.

%prep
%autosetup -n trzsz-ssh-%{version}

%build
export CGO_ENABLED=0
export GOPROXY=direct
go build -ldflags="-s -w" -o %{_builddir}/bin/tssh ./cmd/tssh

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/bin/tssh %{buildroot}%{_bindir}/tssh

%files
%{_bindir}/tssh

%changelog
* Sun Jul 26 2026 Lonny Wong <lonnywong@qq.com> - 0.1.26-1
- Update to tssh v0.1.26

* Sun May 3 2026 Lonny Wong <lonnywong@qq.com> - 0.1.25-1
- Initial RPM spec for tssh
