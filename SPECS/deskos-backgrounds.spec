Name:           deskos-backgrounds
Version:        1.0.0
Release:        1
Summary:        DeskOS default desktop background

License:        CC-BY-SA
URL:            https://github.com/deskosproject/deskos-backgrounds-rpm
Source0:        https://dl.deskosproject.org/sources/deskos-backgrounds/%{name}-%{version}.tar.xz

BuildArch:      noarch
Requires:       %{name}-gnome = %{version}-%{release}

%description
This package contains desktop backgrounds for the DeskOS default theme.
Pulls in theme for GNOME desktop.

%package        base
Summary:        Base images for DeskOS default background
License:        CC-BY-SA

%description    base
This package contains base images for DeskOS default background.

%package        gnome
Summary:        DeskOS default wallpaper for GNOME
Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains GNOME desktop wallpaper for the DeskOS default theme.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files base
%license CC-BY-SA-3.0 Attribution
%dir %{_datadir}/backgrounds/deskos
%dir %{_datadir}/backgrounds/deskos/default
%{_datadir}/backgrounds/deskos/default/normalish
%{_datadir}/backgrounds/deskos/default/standard
%{_datadir}/backgrounds/deskos/default/wide
%{_datadir}/backgrounds/deskos/default/tv-wide
%{_datadir}/backgrounds/deskos/default/deskos.xml

%files gnome
%{_datadir}/gnome-background-properties/deskos.xml

%changelog
* Thu Mar 24 2016 Ricardo Arguello <rarguello@deskosproject.org> - 1.0.0-1
- Initial RPM release
