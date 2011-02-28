%define abiquo_basedir /opt/abiquo

Name:           abiquo-server-community
Version:        1.7
Release:        4%{?dist}%{?buildstamp}
Url:            http://www.abiquo.com/
License:        Multiple
Group:          Development/Tools
Summary:        Abiquo Server Community Edition 
Source0:        server.war
Source1:        abiquo.properties.server
Source2:        kinton-schema.sql
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       abiquo-core abiquo-client-community mysql-server nfs-utils sos wget ruby ntp libvirt-client rabbitmq-server abiquo-server-tools abiquo-api-community
Requires:       /usr/sbin/sendmail /usr/bin/which
BuildRequires: /usr/bin/unzip
BuildArch: 	noarch

%description
Next Generation Cloud Management Solution

This package contains the server community component.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/database
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/examples
mkdir -p $RPM_BUILD_ROOT%{abiquo_basedir}
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/
mkdir -p %{buildroot}/%{_sysconfdir}/cron.d/
cp %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}/database/
cp -r %{SOURCE1} $RPM_BUILD_ROOT/%{abiquo_basedir}/config/examples/
/usr/bin/unzip -d $RPM_BUILD_ROOT/%{abiquo_basedir}/tomcat/webapps/server/ %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{abiquo_basedir}/tomcat/webapps/server
%{_docdir}/%{name}
%{abiquo_basedir}/config/examples/abiquo.properties.server

%changelog
* Mon Feb 14 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- updated release string

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-3
- set buildarch to noarch

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-2
- fixed files section

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-1
- Initial Release
