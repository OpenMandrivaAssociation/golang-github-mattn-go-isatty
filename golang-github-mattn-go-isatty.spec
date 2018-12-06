# http://github.com/mattn/go-isatty
%global goipath         github.com/mattn/go-isatty
%global commit          3fb116b820352b7f0c281308a4d6250c22d94e27

%gometa

Name:           golang-github-mattn-go-isatty
Version:        0.0.4
Release:        0.1%{?dist}
Summary:        Isatty for golang
# Detected licences
# - MIT/X11 (BSD like) at 'LICENSE'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{summary}


%package devel
Summary:       %{summary}

BuildRequires: golang(golang.org/x/sys/unix)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .


%install
%goinstall glide.lock glide.yaml


%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Nov 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.4-0.1.20181102git3fb116b
- Bump to commit 3fb116b820352b7f0c281308a4d6250c22d94e27

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.0.3-6
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.0.3-4
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.0.3-3
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Ed Marshall <esm@logic.net> - 0.0.3-1
- Update to v0.0.3 (#1495177)
- This project makes proper releases; drop git commit boilerplate

* Mon Sep 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 0.0.2-0.1.gitfc9e8d8
- Update to v0.0.2
  resolves: #1462140

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git66b8e73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git66b8e73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jan 05 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git66b8e73
- First package for Fedora
  resolves: #1430143
