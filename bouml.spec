Summary:	UML 2 tool box to specify and generate code in C++, Java, IDL, PHP and Python
Name:		bouml
Version:	4.3.5
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
URL:		http://bouml.free.fr
Source0:	http://bouml.free.fr/%{name}_%{version}.tar.gz
BuildRequires:	qt3-devel
%if %{mdkversion} < 200800
BuildRequires:	desktop-file-utils
%endif
Suggests:	bouml-doc = 4.2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
BOUML is a free Unified Modeling Language (UML 2) tool box allowing you
to specify and generate code in C++, Java, Idl, Php and Python.
You can use it to create nearly all of UML diagrams.
BOUML can generate code from those diagrams in
C++, Java, IDL, PHP and Python, and can also reverse existing code.

The program supports class diagrams, sequence diagrams, collaboration diagrams,
object diagrams, use case diagrams, component diagrams, state diagrams,
activity diagrams, component diagrams and deployment diagrams.

%prep
%setup -q -n %{name}_%{version}

%build
%make QMAKE=%{qt3dir}/bin/qmake BOUML_LIB=%{_libdir}/%{name}

%install
rm -rf %{buildroot}
make install BOUML_LIB=%{_libdir}/%{name} DESTDIR=%{buildroot}
%if %{mdkversion} < 200800
desktop-file-install \
	--vendor="" \
	--add-category="X-MandrivaLinux-MoreApplications-Development" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
%endif

%post
%update_icon_cache hicolor
%{update_menus}

%postun
%update_icon_cache hicolor
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README historic.html licence.txt
%{_bindir}/%{name}
%{_bindir}/projectControl
%{_bindir}/projectSynchro
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/projectControl.png
%{_iconsdir}/hicolor/16x16/apps/projectSynchro.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/projectControl.png
%{_iconsdir}/hicolor/32x32/apps/projectSynchro.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/projectControl.png
%{_iconsdir}/hicolor/48x48/apps/projectSynchro.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/projectControl.png
%{_iconsdir}/hicolor/64x64/apps/projectSynchro.png

