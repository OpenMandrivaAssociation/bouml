Summary:	UML 2 tool box to specify and generate code in C++, Java, IDL, PHP and Python
Name:		bouml
Version:	4.20
%define file_project_version	4.20
%define bouml_doc_version	4.19
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
URL:		http://bouml.free.fr
Source0:	http://downloads.sourceforge.net/bouml/%{name}_%{version}.tar.gz
Patch01:	bouml-mandriva-doc-path-fix.patch
Patch02:	bouml-help-use-xdg-open.patch
BuildRequires:	gcc-c++
BuildRequires:	qt3-devel
%if %{mdkversion} < 200800
BuildRequires:	desktop-file-utils
%endif
Requires:	xdg-utils
Suggests:	bouml-doc >= %{bouml_doc_version}
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
%patch01 -p1 -b .mandriva-doc-path-fix
%patch02 -p1 -b .help-use-xdg-open

%build
%make QTDIR=%{qt3dir} QMAKE=%{qt3dir}/bin/qmake BOUML_LIB=%{_libdir}/%{name}

%install
rm -rf %{buildroot}
%makeinstall_std BOUML_LIB=%{_libdir}/%{name}
%if %{mdkversion} < 200800
desktop-file-install \
	--vendor="" \
	--add-category="X-MandrivaLinux-MoreApplications-Development" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*
%endif

cat > README.%{file_project_version}.upgrade.urpmi <<EOF
Because the format of the BOUML files is changed in BOUML %{file_project_version},
the previous releases (BOUML < %{file_project_version}) cannot read a project
saved with this version. Obviously this release is able to read
the projects made by previous releases of BOUML.
EOF

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%update_icon_cache hicolor
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README README.*.upgrade.urpmi historic.html licence.txt
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
