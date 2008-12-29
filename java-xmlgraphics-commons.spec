#
Summary:	Apache XML Graphics Commons
Summary(pl.UTF-8):	Apache XML Graphics Commons - wspólne komponenty graficzne
Name:		xmlgraphics-commons
Version:	1.3.1
Release:	1
License:	Apache v2.0
Group:		Libraries
# http://svn.apache.org/repos/asf/xmlgraphics/commons/branches/commons-1_0/
Source0:	http://www.apache.net.pl/xmlgraphics/commons/source/%{name}-%{version}-src.tar.gz
# Source0-md5:	4dcac6600df8282685be6972bf9b4de4
URL:		http://xmlgraphics.apache.org/commons/
BuildRequires:	ant >= 1.6.5
BuildRequires:	java-commons-io
BuildRequires:	java-commons-logging
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.8.1
BuildRequires:	rpmbuild(macros) >= 1.300
# disable internal-codecs in build.properities for compatibility with other jre's
Requires:	java-commons-io
Requires:	java-commons-logging
Requires:	java-sun-jre >= 1.4
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache XML Graphics Commons is a library that consists of several
reusable components used by Apache Batik and Apache FOP. Many of these
components can easily be used separately outside the domains of SVG
and XSL-FO. You will find components such as a PDF library, an RTF
library, Graphics2D implementations that let you generate PDF &
PostScript files, and much more.

%description -l pl.UTF-8
Apache XML Graphics Commons to biblioteka składająca się z kilku
wspólnych komponentów używanych przez Apache Batik i Apache POP. Wiele
z tych komponentów może być łatwo wykorzystanych poza dziedziną SVG i
XSL-FO. Można tu znaleźć komponenty takie jak biblioteka PDF,
biblioteka RTF czy implementacje Graphics2D pozwalające generować
pliki PDF oraz PostScript i wiele więcej.

%prep
%setup -q

rm lib/*.jar
ln -s $(find-jar commons-io) lib
ln -s $(find-jar commons-logging) lib

%build
export JAVAC=%{javac}
export JAVA=%{java}

%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/xmlgraphics-commons-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS README lib/README.txt examples
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
