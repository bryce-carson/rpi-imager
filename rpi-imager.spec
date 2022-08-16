Name:       rpi-imager
Version:    1.7.2
Release:    3
Summary:    Raspberry Pi operating system imager tool

License:    GPLv2+
URL:        https://www.raspberrypi.org/

Source: https://github.com/bryce-carson/rpi-imager.git

BuildRequires: git gcc gcc-c++ make cmake libarchive-devel libcurl-devel openssl-devel qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qtsvg-devel qt5-linguist

%description
Raspberry Pi imaging utility.

Graphical user-interface to write disk images and format SD cards.

%prep
%setup -q

%build
%cmake .
%make_build

%install
%make_install

%check
ctest -V %{?_smp_mflags}

%files
%doc

%changelog
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-3
- Fix all the issues with Tito and sources, hopefully.
- Also CMake
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-1
- New RPM with Tito; first Tito tag _this_ commit

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- Created an RPM spec file for 1.7.2
- Initialized Tito for use with Copr
