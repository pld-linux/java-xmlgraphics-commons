Summary:	Apache XML Graphics Commons
Summary(pl):	Apache XML Graphics Commons - wspólne komponenty graficzne
Name:		xmlgraphics-commons
Version:	1.0
Release:	1
License:	Apache v2.0
Group:		Libraries
# http://svn.apache.org/repos/asf/xmlgraphics/commons/branches/commons-1_0/
Source0:	%{name}-%{version}-svn.tar.bz2
# Source0-md5:	c9b1e2a23cb164a4255ecff1941dc0aa
URL:		http://xmlgraphics.apache.org/commons/
BuildRequires:	ant >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
# disable internal-codecs in build.properities for compatibility with other jre's
Requires:	java-sun-jre
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

%description -l pl
Apache XML Graphics Commons to biblioteka sk³adaj±ca siê z kilku
wspólnych komponentów u¿ywanych przez Apache Batik i Apache POP. Wiele
z tych komponentów mo¿e byæ ³atwo wykorzystanych poza dziedzin± SVG i
XSL-FO. Mo¿na tu znale¼æ komponenty takie jak biblioteka PDF,
biblioteka RTF czy implementacje Graphics2D pozwalaj±ce generowaæ
pliki PDF oraz PostScript i wiele wiêcej.

%prep
%setup -q -n %{name}

%build
export JAVAC=%{javac}
export JAVA=%{java}

%{ant}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/*.jar		$RPM_BUILD_ROOT%{_javadir}
install lib/commons-io-1.1.jar	$RPM_BUILD_ROOT%{_javadir}
ln -s       commons-io-1.1.jar	$RPM_BUILD_ROOT%{_javadir}/commons-io.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README lib/README* examples
%{_javadir}/*.jar
