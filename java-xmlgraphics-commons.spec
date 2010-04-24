
%include	/usr/lib/rpm/macros.java

%define		srcname	xmlgraphics-commons
Summary:	Apache XML Graphics Commons
Summary(pl.UTF-8):	Apache XML Graphics Commons - wspólne komponenty graficzne
Name:		java-xmlgraphics-commons
Version:	1.3.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Java
# http://svn.apache.org/repos/asf/xmlgraphics/commons/branches/commons-1_0/
Source0:	http://www.apache.net.pl/xmlgraphics/commons/source/xmlgraphics-commons-%{version}-src.tar.gz
# Source0-md5:	4dcac6600df8282685be6972bf9b4de4
URL:		http://xmlgraphics.apache.org/commons/
BuildRequires:	ant >= 1.6.5
BuildRequires:	java-commons-io
BuildRequires:	java-commons-logging
BuildRequires:	java-junit >= 3.8.1
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
# disable internal-codecs in build.properities for compatibility with other jre's
Requires:	java-commons-io
Requires:	java-commons-logging
Requires:	jre >= 1.4
BuildArch:	noarch
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
%setup -q -n %{srcname}-%{version}

rm lib/*.jar

%build
required_jars="commons-io commons-logging"
export JAVA_HOME=%{java_home}
CLASSPATH=$(build-classpath $required_jars)
%ant -Dbuild.sysclasspath=first

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/xmlgraphics-commons-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS README lib/README.txt examples
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar
