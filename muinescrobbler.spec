%define name muinescrobbler
%define version 0.1.8
%define release %mkrel 6
%define plugindir %_prefix/lib/muine/plugins

Summary: Audioscrobbler plugin for Muine
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gna.org/muinescrobbler/%{name}-%{version}.tar.bz2
Patch: muinescrobbler-new-mono.patch
Patch1: muinescrobbler-fix-linking.patch
License: GPLv2+
Group: Sound
Url: https://home.gna.org/muinescrobbler/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: muine
BuildRequires: gnome-sharp2-devel
Requires: muine

%description
This adds support for Audioscrobbler to the Muine player:
http://www.audioscrobbler.com

%prep
%setup -q -n %name
%patch -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%plugindir
install -m 644 AudioscrobblerPlugin.dll %buildroot%plugindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%plugindir/AudioscrobblerPlugin.dll
