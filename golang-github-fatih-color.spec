# Run tests in check section
%bcond_without check

# https://github.com/fatih/color
%global goipath         github.com/fatih/color
Version:                1.7.0

%global common_description %{expand:
Color lets you use colorized outputs in terms of ANSI Escape Codes in Go 
(Golang). It has support for Windows too! The API can be used in several 
ways, pick one that suits you.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Color package for Go (golang)
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/mattn/go-colorable)
BuildRequires: golang(github.com/mattn/go-isatty)

# test requirement:
BuildRequires: golang(github.com/smartystreets/goconvey/convey)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE.md
%doc README.md


%changelog
* Tue Sep 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.7.0-2
- Update to new packaging
- Add missing BuildRequires (#1632758)

* Thu Aug 02 2018 Michael Cronenworth <mike@cchtml.com> - 1.7.0-1
- New upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20170905git1535ebc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.3.20170905git1535ebc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.1-0.2.20170905git1535ebc
- Provide alternate name path

* Mon Sep 18 2017 Matthias Runge <mrunge@redhat.com> - 0-0.1.20170905git1535ebc
- update to latest version
- package review (rhbz#1376437)

* Fri Apr 15 2016 Matthias Runge <mrunge@redhat.com> - 0.1-1
- initial package
