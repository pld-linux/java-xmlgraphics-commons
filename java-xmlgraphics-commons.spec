Summary:	Apache XML Graphics Commons
Summary(pl):	Apache XML Graphics Commons
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
#BuildRequires:	junit
BuildRequires:	rpmbuild(macros) >= 1.300
# disable internal-codecs in build.properities for compatibility with other jre's
Requires:	java-sun-jre
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache XML Graphics Commons is a library that consists of several
reusable components used by Apache Batik and Apache FOP. Many of these
components can easily be used separately outside the domains of SVG and
XSL-FO. You will find components such as a PDF library, an RTF library,
Graphics2D implementations that let you generate PDF & PostScript files,
and much more.

#%description -l pl

%prep
%setup -q -n %{name}

%build
#required_jars='junit'
#export CLASSPATH="$CLASSPATH:`/usr/bin/build-classpath $required_jars`"
export JAVAC=%{javac}
export JAVA=%{java}

%{ant}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install lib/commons-io-1.1.jar $RPM_BUILD_ROOT%{_javadir}
ln -s       commons-io-1.1.jar $RPM_BUILD_ROOT%{_javadir}/commons-io.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README lib/README* examples
%{_javadir}/*.jar
