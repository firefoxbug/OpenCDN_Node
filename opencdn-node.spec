%define         VERSION 1.1
Name:           opencdn-node
Version:        %VERSION
Release:        2%{?dist}
Summary:        opencdn-node

Group:          tools
License:        GNU
URL:            http://www.ocdn.me
BuildRoot:      /tmp/billing-build-root
Requires:       rsync syslog-ng inotify-tools 
BuildArch: noarch
#BuildRequires: gcc
#Requires:      gcc
Autoreq:        no
%define _builddir           .
%define _rpmdir             .
%define _srcrpmdir          .
%define _build_name_fmt     %%{NAME}-%%{VERSION}-%%{RELEASE}-%%{ARCH}.rpm
%define __os_install_post   /usr/lib/rpm/brp-compress; echo 'Not stripping.'

%description
opencdn-node

%prep
#%setup -q

%build
#make 


%install
rm -rf $RPM_BUILD_ROOT
install -p -d -m 0755 $RPM_BUILD_ROOT/usr/local/opencdn/conf/
install -p -d -m 0755 $RPM_BUILD_ROOT/usr/local/opencdn/ocdn/
install -p -d -m 0755 $RPM_BUILD_ROOT/usr/local/opencdn/pipe/
install -p -d -m 0755 $RPM_BUILD_ROOT/usr/local/opencdn/sbin/
install -p -d -m 0755 $RPM_BUILD_ROOT/var/log/opencdn/
install -p -d -m 0755 $RPM_BUILD_ROOT/etc/init.d/
install -p -d -m 0755 $RPM_BUILD_ROOT/etc/httpd/conf.d/
install -p -d -m 0755 $RPM_BUILD_ROOT/etc/
install -p -d -m 0755 $RPM_BUILD_ROOT/tmp/

install -p -m 0755 opencdn.conf $RPM_BUILD_ROOT/usr/local/opencdn/conf/
install -p -m 0755 nginxmon $RPM_BUILD_ROOT/usr/local/opencdn/sbin/
install -p -m 0755 send_info $RPM_BUILD_ROOT/usr/local/opencdn/sbin/
install -p -m 0755 opencdn $RPM_BUILD_ROOT/etc/init.d/
install -p -m 0755 rsyncd.conf $RPM_BUILD_ROOT/etc/
install -p -m 0755 syslog-ng.conf $RPM_BUILD_ROOT/tmp/
PREFIX=$RPM_BUILD_ROOT make install
#make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/local/opencdn/pipe/
/usr/local/opencdn/sbin/
/var/log/opencdn/
/etc/init.d/opencdn
/etc/rsyncd.conf
/tmp/
%config(noreplace) /usr/local/opencdn/conf/opencdn.conf
%pre

if [ $1 -eq 1 ]; then
    getent group apache > /dev/null || groupadd -r apache
    getent passwd apache > /dev/null || \
        useradd -r -d apache -g apache \
        -s /sbin/nologin -c "apache web server" apache
    exit 0
fi
%post
echo "ocdn:ocdn.me" >/etc/rsyncd.pwd
chmod 600 /etc/rsyncd.pwd

echo "nohup /usr/local/opencdn/sbin/nginxmon > /var/log/opencdn/nginxmon.log 2>&1 &" >> /etc/rc.d/rc.local
nohup /usr/local/opencdn/sbin/nginxmon > /var/log/opencdn/nginxmon.log 2>&1 &
chkconfig --add opencdn
service opencdn restart

rm -f /etc/syslog-ng/syslog-ng.conf
mv /tmp/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf
%postun
sed -i '/nginxmon/d' /etc/rc.local
%changelog

