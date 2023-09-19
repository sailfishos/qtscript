Name:       qt5-qtscript
Summary:    Qt scripting module
Version:    5.6.2
Release:    1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the scripting module


%package devel
Summary:    Qt scripting - development files
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the scripting module development files


#### Build section

%prep
%setup -q -n %{name}-%{version}

%build
touch .git
%qmake5
%make_build

%install
%qmake5_install
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
#
# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_qt5_includedir}/Qt


%fdupes %{buildroot}/%{_includedir}




#### Pre/Post section

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig




#### File section


%files
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Script.so.5
%{_qt5_libdir}/libQt5Script.so.5.*
%{_qt5_libdir}/libQt5ScriptTools.so.5
%{_qt5_libdir}/libQt5ScriptTools.so.5.*

%files devel
%defattr(-,root,root,-)
%{_qt5_libdir}/libQt5Script.so
%{_qt5_libdir}/libQt5Script.prl
%{_qt5_libdir}/libQt5ScriptTools.so
%{_qt5_libdir}/libQt5ScriptTools.prl
%{_qt5_libdir}/pkgconfig/*
%{_qt5_includedir}/*
%{_qt5_archdatadir}/mkspecs/
%{_qt5_libdir}/cmake/



#### No changelog section, separate $pkg.changes contains the history
