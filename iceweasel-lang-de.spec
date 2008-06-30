%define		_lang		de
Summary:	German resources for Iceweasel
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Iceweasel
Name:		iceweasel-lang-%{_lang}
Version:	3.0
Release:	3
License:	GPL
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/%{_lang}.xpi
# Source0-md5:	635d3d7ab3d00d216cb536597da10811
URL:		http://www.mozilla.org/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-de
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_langpackdir	%{_datadir}/iceweasel/extensions/langpack-%{_lang}@firefox.mozilla.org

%description
German resources for Iceweasel.

%description -l pl.UTF-8
Niemieckie pliki językowe dla Iceweasel.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_langpackdir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_langpackdir}

# rebrand locale for iceweasel
cd $RPM_BUILD_ROOT%{_langpackdir}/chrome
unzip de.jar locale/branding/brand.dtd locale/branding/brand.properties \
	locale/browser/appstrings.properties locale/browser/aboutDialog.dtd
sed -i -e 's/Mozilla Firefox/Iceweasel/g; s/Firefox/Iceweasel/g;' \
	locale/branding/brand.dtd locale/branding/brand.properties
sed -i -e 's/Firefox/Iceweasel/g;' locale/browser/appstrings.properties
grep -e '\<ENTITY' locale/browser/aboutDialog.dtd \
	> locale/browser/aboutDialog.dtd.new
sed -i -e '/copyrightInfo/s/^\(.*\)\..*Firefox.*/\1\./g; s/\r//g; /copyrightInfo/s/$/" >/g;' \
	locale/browser/aboutDialog.dtd.new
mv -f locale/browser/aboutDialog.dtd.new locale/browser/aboutDialog.dtd
zip -0 de.jar locale/branding/brand.dtd locale/branding/brand.properties \
	locale/browser/appstrings.properties locale/browser/aboutDialog.dtd
rm -f locale/branding/brand.dtd locale/branding/brand.properties \
	locale/browser/appstrings.properties locale/browser/aboutDialog.dtd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_langpackdir}
