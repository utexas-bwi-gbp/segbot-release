Name:           ros-indigo-segbot
Version:        0.3.5
Release:        0%{?dist}
Summary:        ROS segbot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/segbot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-segbot-bringup
Requires:       ros-indigo-segbot-description
Requires:       ros-indigo-segbot-firmware
Requires:       ros-indigo-segbot-gazebo
Requires:       ros-indigo-segbot-gui
Requires:       ros-indigo-segbot-logical-translator
Requires:       ros-indigo-segbot-navigation
Requires:       ros-indigo-segbot-sensors
Requires:       ros-indigo-segbot-simulation-apps
BuildRequires:  ros-indigo-catkin

%description
ROS packages for controlling Segway-based robots at the Learning Agents Research
Group (LARG), AI Laboratory, Department of Computer Science, University of Texas
at Austin.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Aug 27 2016 Piyush Khandelwal <piyushk@gmail.com> - 0.3.5-0
- Autogenerated by Bloom

* Mon Aug 08 2016 Piyush Khandelwal <piyushk@gmail.com> - 0.3.4-0
- Autogenerated by Bloom

* Wed Aug 05 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.3-0
- Autogenerated by Bloom

* Tue Mar 31 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.2-0
- Autogenerated by Bloom

* Thu Mar 26 2015 Piyush Khandelwal <piyushk@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

