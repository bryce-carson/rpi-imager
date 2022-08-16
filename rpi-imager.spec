Name:       rpi-imager
Version:    1.7.2
Release:    9
Summary:    Raspberry Pi operating system imager tool

License:    GPLv2+
URL:        https://www.raspberrypi.org/

Source: https://github.com/bryce-carson/rpi-imager/archive/refs/tags/rpi-imager-%{version}-%{release}.tar.gz

BuildRequires: git gcc gcc-c++ make cmake libarchive-devel libcurl-devel openssl-devel qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qtsvg-devel qt5-linguist

%description
Raspberry Pi imaging utility.

Graphical user-interface to write disk images and format SD cards.

%prep
%setup -q

%build
%cmake src
%cmake_build

%install
%cmake_install

%check
ctest -V %{?_smp_mflags}

%files
/usr/bin/rpi-imager
/usr/share/applications/rpi-imager.desktop
/usr/share/icons/hicolor/128x128/apps/rpi-imager.png
/usr/share/metainfo/rpi-imager.metainfo.xml

%changelog
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-9
- 

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-8
- Fix files issue with RPM spec (bcars268@mtroyal.ca)

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-7
- 

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- 

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-6
- Fix source issues, fix CMake issue (bcars268@mtroyal.ca)

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- 

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- 

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-5
- Update SOURCE URL (bcars268@mtroyal.ca)

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- Update SOURCE URL (bcars268@mtroyal.ca)

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-4
- Fix Source URL issue

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-3
- Fix all the issues with Tito and sources, hopefully.
- Also CMake
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- Created an RPM spec file for 1.7.2
- Initialized Tito for use with Copr
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.2-1
- New RPM with Tito; first Tito tag _this_ commit
