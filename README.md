Project Title
==========================

This project implemented to touch and feel of light weight containers

Installation and Configuration set up
======================================

Step 1:
$yum update -y && yum upgrade -y

$yum install git -y && yum install wget -y && yum install unzip -y && yum install curl -y

Step2:
Option 1:

$ curl -fsSL https://get.docker.com -o get-docker.sh

$ sudo sh get-docker.sh

$sudo usermod -aG docker $(whoami) or sudo chmod 666 /var/run/docker.sock


Option 2:

$sudo yum install docker -y

Step 3:
$sudo usermod -aG docker <user-name> or sudo chmod 666 /var/run/docker.sock


EXecution Flow
=========================

# Flask

$git clone https://github.com/krishnamaram2/container_engine.git

$cd container_engine/src/flask

$docker image build -t flask --network host .

$docker run -d --name flask -p 5001:5001 flask


# MySQL

$git clone https://github.com/krishnamaram2/container_engine.git

$cd container_engine/src/mysql

$docker image build -t mysql .

$docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=Root_123 mysql

or

$docker login

$docker pull csporg/mysql

$docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=Root_123 csporg/mysql














Apache HTTP server
------------------------
$git clone https://github.com/krishnamaram2/Container_Engine.git

$cd Container_Engine/src/webserver

$docker image build -t <image_name> .

$docker container run -d --name <container_name> -p 80:80 <image_name>


Apache Tomcat server
-------------------------
$git clone https://github.com/krishnamaram2/container-engine.git

$cd container-engine/src/appserver

$docker image build -t <image_name> .

$docker container run -d -it --name <container_name> -p 8080:8080 <image_name>

 
 Optional steps:
$docker exec -it <container_name> bash

vi /usr/local/tomcat/webapps/conf/server.xml

<!--        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"

               prefix="localhost_access_log" suffix=".txt"
               
               pattern="%h %l %u %t &quot;%r&quot; %s %b" /> -->


$git clone https://github.com/krishnamaram2/WebApp.git

$docker cp WebApp/binary/Student.war <container_name>:/usr/local/tomcat/webapps/

$sh /usr/local/tomcat/bin/catalina.sh start

Reference: https://www.cprime.com/resources/blog/deploying-your-first-web-app-to-tomcat-on-docker/
  
MySQL DB server
---------------------

$git clone https://github.com/krishnamaram2/Container_Engine.git

$cd Container_Engine/src/dbserver

$docker image build -t <image_name> .

$docker run -d --name <container_name> -e MYSQL_ROOT_PASSWORD=Root_123 <image_name>

Step 3: create database and user for MySQL and import data into database
$docker exec -it <container_name> sh

$mysql -u root -p

mysql>create database indigo;

mysql>CREATE USER '<user_name>'@'%' IDENTIFIED BY '';

mysql>GRANT ALL ON . TO ''@'%';

mysql>FLUSH PRIVILEGES;

$git clone https://github.com/krishnamaram2/WebApp.git

$cd WebApp/binary
$mysql -u <user_name> -p indigo < indigo.sql







