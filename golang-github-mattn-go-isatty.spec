# Run tests in check section
%bcond_without check

# https://github.com/mattn/go-isatty
%global goipath		github.com/mattn/go-isatty
%global forgeurl	https://github.com/mattn/go-isatty
Version:		0.0.20

%gometa

Summary:	Isatty for golang
Name:		golang-github-mattn-go-isatty

Release:	1
Source0:	https://github.com/mattn/go-isatty/archive/v%{version}/go-isatty-%{version}.tar.gz
URL:		https://github.com/mattn/go-isatty
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	golang(golang.org/x/sys/unix)
BuildArch:	noarch

%description
Isatty for golang.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-isatty-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

