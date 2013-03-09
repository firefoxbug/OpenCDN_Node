###Node端安装手册

###配置

**本文档以 Centos 6.x 86_64 为蓝本** 本文档约定 所有命令以#打头
	
	#wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

	#wget http://58.215.133.101:801/rpm/inotify-tools-3.14-1.el6.x86_64.rpm
	
	#wget http://58.215.133.101:801/rpm/nginx-1.2.0-5.el6.x86_64.rpm

	#wget http://58.215.133.101:801/rpm/opencdn-node-1.1-2.el6-noarch.rpm

	#rpm -ivh epel-release-6-8.noarch.rpm

	#rpm -ivh inotify-tools-3.14-1.el6.x86_64.rpm

	#rpm -ihv nginx-1.2.0-5.el6.x86_64.rpm

	**yum -y localinstall opencdn-node-1.1-2.el6-noarch**推荐这么安装。会动解决依赖关系.

	检查Selinux状态

	#sestatus
	
	如果输出不为 SELinux status:    disabled .可以昨时先关闭 .命令如下：

	#setenforce 0

	永久关闭方法：

	#vim  /etc/sysconfig/selinux  把SELINUX=disabled 并重启系统


####修改配置

	#sed -i 's#localhost#8.8.8.8.#g' /usr/local/opencdn/conf/opencdn.conf  设置为你主控端ip 这里以8.8.8.8.为例

	#sed -i  's#0.0.0.0#119.147.0.239#g' /etc/syslog-ng/syslog-ng.conf 修改syslog-ng 上传的日志中心（一般为主控端）

####重启webserver->http

	/etc/init.d/httpd restart
	
####启动opencdn

	#/etc/init.d/opencdn restart

检查一下opencdn开启状态,查看日志。查看有没有异常.
	
	#cd /var/log/opencdn/ 相看相关日志


