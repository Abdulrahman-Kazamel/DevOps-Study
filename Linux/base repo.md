
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Base.repo
sed -i 's/#baseurl=http:\/\/mirror.centos.org/baseurl=https:\/\/vault.centos.org/g' /etc/yum.repos.d/CentOS-Base.repo
yum clean all
yum makecache
