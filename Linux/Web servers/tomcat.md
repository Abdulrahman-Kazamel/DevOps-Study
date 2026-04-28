

curl --user admin:admin --upload-file /opt/tomcat/webapps/ROOT.war "http://localhost:8080/manager/text/deploy?path=/stapp02"




docerize tomcat 



to deploy on webapps directly 
```
rm -rf /usr/tomcat/tomcat_11/webapps/ROOT
rm -rf /usr/tomcat/tomcat_11/webapps/ROOT.war
```


```FROM centos:centos7.9.2009

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Base.repo
RUN sed -i 's/#baseurl=http:\/\/mirror.centos.org\/centos\/$releasever/baseurl=http:\/\/vault.centos.org\/centos\/$releasever/g' /etc/yum.repos.d/CentOS-Base.repo

RUN yum clean all && yum makecache && yum update -y
RUN yum install wget -y && yum install iproute -y && yum install tar -y


RUN useradd -s /bin/bash tomcat

RUN mkdir -p /usr/java/java_21
RUN mkdir -p /usr/tomcat/tomcat_11


#RUN su - tomcat
#USER tomcat
RUN wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz
RUN wget  https://dlcdn.apache.org/tomcat/tomcat-11/v11.0.21/bin/apache-tomcat-11.0.21.tar.gz
RUN wget https://tomcat.apache.org/tomcat-6.0-doc/appdev/sample/sample.war

RUN tar -xzf apache*
RUN tar -xzf jdk*


RUN mv apache-tomcat-11.*/* /usr/tomcat/tomcat_11/
RUN mv jdk-21.0.10*/* /usr/java/java_21/

RUN mv sample.war /usr/tomcat/tomcat_11/webapps/

RUN chown -R tomcat:tomcat /usr/tomcat /usr/java
USER tomcat

ENV JAVA_HOME=/usr/java/java_21
ENV CATALINA_BASE=/usr/tomcat/tomcat_11
ENV PATH=$PATH:$JAVA_HOME/bin

EXPOSE 8080

#RUN source ~/.bashrc

#ENTRYPOINT ["bash"]
#CMD ["/usr/tomcat/tomcat_11/bin/startup.sh"]
CMD ["/usr/tomcat/tomcat_11/bin/catalina.sh", "run"]
```



```
yum update -y
yum install wget -y && yum install iproute -y && yum install tar -y


useradd -s /bin/bash tomcat

 mkdir -p /usr/java/java_21
 mkdir -p /usr/tomcat/tomcat_11

wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz
wget  https://dlcdn.apache.org/tomcat/tomcat-11/v11.0.21/bin/apache-tomcat-11.0.21.tar.gz


 tar -xzf apache*
tar -xzf jdk*


 mv apache-tomcat-11.*/* /usr/tomcat/tomcat_11/
 mv jdk-21.0.10*/* /usr/java/java_21/



chown -R tomcat:tomcat /usr/tomcat /usr/java


export JAVA_HOME=/usr/java/java_21 
export CATALINA_BASE=/usr/tomcat/tomcat_11  
export PATH=$PATH:$JAVA_HOME/bin  

EXPOSE 8080

#RUN source ~/.bashrc

#ENTRYPOINT ["bash"]
#CMD ["/usr/tomcat/tomcat_11/bin/startup.sh"]
CMD ["/usr/tomcat/tomcat_11/bin/catalina.sh", "run"]
```
