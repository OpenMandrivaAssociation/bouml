Summary:	UML 2 tool box to specify and generate code in C++, Java, IDL, PHP and Python
Name:		bouml
Version:	4.22.2
%define file_project_version	4.22
%define bouml_doc_version	4.21
Release:	2
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


%changelog
* Tue Jul 20 2010 Luc Menut <lmenut@mandriva.org> 4.22.2-1mdv2011.0
+ Revision: 556287
- update to 4.22.2

* Sat Jul 10 2010 Luc Menut <lmenut@mandriva.org> 4.22.1-1mdv2011.0
+ Revision: 550520
- update to 4.22.1

* Sun Apr 25 2010 Luc Menut <lmenut@mandriva.org> 4.20-1mdv2010.1
+ Revision: 538709
- update to 4.20

* Mon Apr 12 2010 Luc Menut <lmenut@mandriva.org> 4.19.3-1mdv2010.1
+ Revision: 533733
- update to 4.19.3

* Sat Apr 03 2010 Luc Menut <lmenut@mandriva.org> 4.19.2-1mdv2010.1
+ Revision: 530859
- update to 4.19.2

* Sun Mar 21 2010 Luc Menut <lmenut@mandriva.org> 4.19.1-1mdv2010.1
+ Revision: 526157
- update to 4.19.1
- update source URL

* Fri Mar 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.19-1mdv2010.1
+ Revision: 514427
- update to 4.19

* Sun Feb 07 2010 Luc Menut <lmenut@mandriva.org> 4.18.1-1mdv2010.1
+ Revision: 501670
- update to version 4.18.1

* Sun Jan 10 2010 Luc Menut <lmenut@mandriva.org> 4.17.1-1mdv2010.1
+ Revision: 488890
- update to version 4.17.1

* Tue Jan 05 2010 Luc Menut <lmenut@mandriva.org> 4.17-1mdv2010.1
+ Revision: 486505
- update to version 4.17

* Wed Sep 30 2009 Luc Menut <lmenut@mandriva.org> 4.15-1mdv2010.0
+ Revision: 451111
- update to new version 4.15

* Wed Sep 23 2009 Emmanuel Andry <eandry@mandriva.org> 4.14-1mdv2010.0
+ Revision: 447921
- New version 4.14

* Tue Sep 01 2009 Luc Menut <lmenut@mandriva.org> 4.13.1-1mdv2010.0
+ Revision: 424046
- update to new version 4.13.1

* Thu Mar 19 2009 Nicolas Vigier <nvigier@mandriva.com> 4.12-1mdv2009.1
+ Revision: 358204
- version 4.12

* Wed Feb 18 2009 Nicolas Vigier <nvigier@mandriva.com> 4.11-1mdv2009.1
+ Revision: 342648
- update to version 4.11 (thank to Luc Menut for help)

* Thu Sep 11 2008 Frederik Himpe <fhimpe@mandriva.org> 4.5.1-2mdv2009.0
+ Revision: 283946
- Integrated suggestions by Luc Menut:
  * suggest new bouml-doc version
  * set file version to 4.5
- use %%makeinstall_std

* Tue Sep 09 2008 Frederik Himpe <fhimpe@mandriva.org> 4.5.1-1mdv2009.0
+ Revision: 283179
- update to new version 4.5.1

* Sat Aug 23 2008 Emmanuel Andry <eandry@mandriva.org> 4.4.3-1mdv2009.0
+ Revision: 275353
- New version

* Thu Aug 07 2008 Emmanuel Andry <eandry@mandriva.org> 4.4.2-1mdv2009.0
+ Revision: 266428
- New version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.3.5-5mdv2009.0
+ Revision: 266341
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 4.3.5-4mdv2009.0
+ Revision: 216917
- adopt to new doc file path

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 4.3.5-3mdv2009.0
+ Revision: 216810
- add patch to comply mandriva doc path
- use xdg-open to open help docs

* Sat Jun 07 2008 Funda Wang <fwang@mandriva.org> 4.3.5-2mdv2009.0
+ Revision: 216666
- fix suggest of doc package

* Sat Jun 07 2008 Funda Wang <fwang@mandriva.org> 4.3.5-1mdv2009.0
+ Revision: 216660
- New version 4.3.5

* Fri Mar 21 2008 Nicolas Vigier <nvigier@mandriva.com> 4.2-1mdv2009.0
+ Revision: 189364
- Package updated by Luc Menut <Luc.Menut@supagro.inra.fr>
- new version 4.2
- correct BuildRequires - desktop-file-utils is needed only for mdkversion < 200800
- add Suggests bouml-doc

* Tue Feb 12 2008 Nicolas Vigier <nvigier@mandriva.com> 4.1-1mdv2008.1
+ Revision: 166117
- new version

* Wed Jan 23 2008 Nicolas Vigier <nvigier@mandriva.com> 3.5-1mdv2008.1
+ Revision: 157013
- new version

* Tue Jan 08 2008 Nicolas Vigier <nvigier@mandriva.com> 3.4.1-1mdv2008.1
+ Revision: 146915
- import bouml


* Wed Jan 02 2008 Luc Menut <Luc.Menut@supagro.inra.fr> 3.4.1-1mdv2008.1
- initial Mandriva package
