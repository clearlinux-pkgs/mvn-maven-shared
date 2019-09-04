#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-shared
Version  : 1.0
Release  : 9
URL      : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-artifact-resolver/1.0/maven-artifact-resolver-1.0.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-artifact-resolver/1.0/maven-artifact-resolver-1.0.jar
Source1  : https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/15/maven-shared-components-15.pom
Source2  : https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/17/maven-shared-components-17.pom
Source3  : https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/18/maven-shared-components-18.pom
Source4  : https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom
Source5  : https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/21/maven-shared-components-21.pom
Source6  : https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/22/maven-shared-components-22.pom
Source7  : https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/30/maven-shared-components-30.pom
Source8  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-artifact-resolver/1.0/maven-artifact-resolver-1.0.pom
Source9  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.10/maven-dependency-analyzer-1.10.jar
Source10  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.10/maven-dependency-analyzer-1.10.pom
Source11  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.5/maven-dependency-analyzer-1.5.jar
Source12  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.5/maven-dependency-analyzer-1.5.pom
Source13  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.7/maven-dependency-analyzer-1.7.jar
Source14  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.7/maven-dependency-analyzer-1.7.pom
Source15  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/1.2/maven-dependency-tree-1.2.jar
Source16  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/1.2/maven-dependency-tree-1.2.pom
Source17  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.jar
Source18  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.pom
Source19  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.2/maven-dependency-tree-2.2.jar
Source20  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/2.2/maven-dependency-tree-2.2.pom
Source21  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/3.0.1/maven-dependency-tree-3.0.1.jar
Source22  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-dependency-tree/3.0.1/maven-dependency-tree-3.0.1.pom
Source23  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar
Source24  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom
Source25  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-io/1.0/maven-shared-io-1.0.jar
Source26  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-io/1.0/maven-shared-io-1.0.pom
Source27  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.jar
Source28  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.pom
Source29  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-io/3.0.0/maven-shared-io-3.0.0.jar
Source30  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-io/3.0.0/maven-shared-io-3.0.0.pom
Source31  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-resources/2/maven-shared-resources-2.jar
Source32  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-shared-resources/2/maven-shared-resources-2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-shared-data = %{version}-%{release}
Requires: mvn-maven-shared-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-shared package.
Group: Data

%description data
data components for the mvn-maven-shared package.


%package license
Summary: license components for the mvn-maven-shared package.
Group: Default

%description license
license components for the mvn-maven-shared package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-maven-shared
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-maven-shared/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-maven-shared/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-artifact-resolver/1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-artifact-resolver/1.0/maven-artifact-resolver-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/15
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/15/maven-shared-components-15.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/17
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/17/maven-shared-components-17.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/18
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/18/maven-shared-components-18.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/19
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/21
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/21/maven-shared-components-21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/22
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/22/maven-shared-components-22.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/30
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/30/maven-shared-components-30.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-artifact-resolver/1.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-artifact-resolver/1.0/maven-artifact-resolver-1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.10
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.10/maven-dependency-analyzer-1.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.10
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.10/maven-dependency-analyzer-1.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.5
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.5/maven-dependency-analyzer-1.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.5
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.5/maven-dependency-analyzer-1.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.7
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.7/maven-dependency-analyzer-1.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.7
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.7/maven-dependency-analyzer-1.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/1.2
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/1.2/maven-dependency-tree-1.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/1.2
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/1.2/maven-dependency-tree-1.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.1
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.1
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.2
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.2/maven-dependency-tree-2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.2
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.2/maven-dependency-tree-2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/3.0.1
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/3.0.1/maven-dependency-tree-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/3.0.1
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/3.0.1/maven-dependency-tree-3.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-incremental/1.1
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-incremental/1.1
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.0
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.0/maven-shared-io-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.0
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.0/maven-shared-io-1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.1
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.1
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/3.0.0
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/3.0.0/maven-shared-io-3.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/3.0.0
cp %{SOURCE30} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/3.0.0/maven-shared-io-3.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-resources/2
cp %{SOURCE31} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-resources/2/maven-shared-resources-2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-resources/2
cp %{SOURCE32} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-resources/2/maven-shared-resources-2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-artifact-resolver/1.0/maven-artifact-resolver-1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-artifact-resolver/1.0/maven-artifact-resolver-1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.10/maven-dependency-analyzer-1.10.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.10/maven-dependency-analyzer-1.10.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.5/maven-dependency-analyzer-1.5.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.5/maven-dependency-analyzer-1.5.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.7/maven-dependency-analyzer-1.7.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-analyzer/1.7/maven-dependency-analyzer-1.7.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/1.2/maven-dependency-tree-1.2.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/1.2/maven-dependency-tree-1.2.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.1/maven-dependency-tree-2.1.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.2/maven-dependency-tree-2.2.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/2.2/maven-dependency-tree-2.2.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/3.0.1/maven-dependency-tree-3.0.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-dependency-tree/3.0.1/maven-dependency-tree-3.0.1.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/15/maven-shared-components-15.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/17/maven-shared-components-17.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/18/maven-shared-components-18.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/21/maven-shared-components-21.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/22/maven-shared-components-22.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-components/30/maven-shared-components-30.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.0/maven-shared-io-1.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.0/maven-shared-io-1.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/1.1/maven-shared-io-1.1.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/3.0.0/maven-shared-io-3.0.0.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-io/3.0.0/maven-shared-io-3.0.0.pom
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-resources/2/maven-shared-resources-2.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-shared-resources/2/maven-shared-resources-2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-maven-shared/LICENSE
/usr/share/package-licenses/mvn-maven-shared/NOTICE
