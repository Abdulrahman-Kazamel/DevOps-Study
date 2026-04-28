Local Repo

Sunday, December 10, 2023

4:35 PM

 

copy the ISO files to local repository directory

#cp -pr /mnt/\* /localrepo

 

create repository file

#vi /etc/yum.repos.d/localrepo.repo

 

Press \"i\" to enter insert mode

 

\[localrepo\]

name=Centos 7 Local or offline repository

baseurl=file:///localrepo

enable=1

gpgcheck=0

 

Press \"Esc\"

press \":wq\" + Enter

 

install yum utilities from local packages

\# rpm -ivh /localrepo/Packages/python-chardet-2.2.1-1.el7_1.noarch.rpm

 

\# rpm -ivh /localrepo/Packages/python-kitchen-1.1.1-5.el7.noarch.rpm

 

\# rpm -ivh /localrepo/Packages/libxml2-python-2.9.1-6.el7_2.3.x86_64.rpm

 

\# rpm -ivh /localrepo/Packages/yum-utils-1.1.31-42.el7.noarch.rpm

 

disable all yum repository and enable local repository

\# yum-config-manager \--disable \\\*

 

\# yum-config-manager \--enable localrepo

 

check avaiable repository list

\# yum clean all

#y um repolist

 

test local repository

\# yum install net-tools

 

#Centos 7 offline Yum repo

 

 

 

 
