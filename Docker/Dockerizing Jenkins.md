

```bash

FROM ubuntu
#jenkins:2.60.3
RUN apt update -y && apt install openjdk-17-jdk -y && java -version
RUN readlink -f $(which java)
#JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
RUN JAVA_HOME=$(which java)
RUN echo $JAVA_HOME
RUN export JAVA_HOME
RUN apt update -y && apt-get install gnupg2 -y
RUN apt install wget -y
RUN wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add -
RUN apt install curl -y


#RUN sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN curl -fsSL https://pkg.origin.jenkins.io/debian-stable/jenkins.io-2026.key | tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
RUN echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.origin.jenkins.io/debian-stable/ binary/" | tee /etc/apt/sources.list.d/jenkins.list > /dev/null


RUN apt update -y
RUN apt install jenkins -y

#RUN set rlim_fd_max = 166384
#RUN service jenkins start

#RUN java -jar /usr/share/java/jenkins.war


WORKDIR /opt/comingsoon/

COPY ./comingsoon/ /opt/comingsoon/

EXPOSE 8080
EXPOSE 5000

#RUN apt update -y && apt upgrade -y
#RUN service jenkins stop
#ENTRYPOINT ["/bin/bash"]
#"set rlim_fd_max = 166384",
#CMD ["set rlim_fd_max = 166384","service jenkins stop","service jenkins start"]
#CMD ["service","jenkins","start"]
#RUN $(which jenkins)
CMD ["java", "-jar", "/usr/share/java/jenkins.war"]
```