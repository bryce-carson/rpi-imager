Name:       rpi-imager
Version:    1.7.3
Release:    2
Summary:    This is a test package.

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
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.3-2
- New release of RPM
- Fix RPM Spec file: use CMake macros

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- Release 2 of the RPM
- Use CMake

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- Fix RPM Spec file
- Use CMake
- Don't create a new version with Tito, just a new release of the RPM
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- Fix RPM Spec file
- Use CMake


* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.4-1
- Fix RPM spec file to use CMake

* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca> 1.7.3-1
- New RPM with Tito; first Tito tag _this_ commit
* Tue Aug 16 2022 Bryce Carson <bcars268@mtroyal.ca>
- Created an RPM spec file for 1.7.2
- Initialized Tito for use with Copr
