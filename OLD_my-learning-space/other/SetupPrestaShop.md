# Setup MSPR project

## Setup user
```bash
lsb_release -a
sudo visudo
# user ALL = (ALL) NOPASSWD:ALL
sudo nano ~/.bashrc
# add alias l, ll, la
source .bashrc
```

## Install packages
```bash	
sudo apt install tree
# --- PHP7 ---
sudo apt-get install php7.2 php7.2-fpm php7.2-mysql
sudo apt install apt-transport-https lsb-release ca-certificates
sudo apt install php7.2-cli php7.2-common php7.2-json php7.2-opcache php7.2-mysql php7.2-zip php7.2-fpm php7.2-mbstring
sudo apt install php7.2-gd
sudo apt install php-zip
sudo apt install php7.2-curl
sudo apt install php7.2-intl
sudo apt install php7.2-xml

# --- Install NODEJS ---
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install nodejs npm

curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install yarn
yarn --version
node -v
npm -v

# --- GITLAB RUNNER ---
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
sudo apt-get update
sudo apt-get install gitlab-runner

# --- PYTHON3 ---
sudo apt install python3
sudo apt install python3-pip
sudo -H pip3 install psycopg2

# --- MARIADB ---
sudo apt install mariadb-server

# --- APACHE2 ---
sudo apt install apache2
sudo apt-get install libapache2-mod-php
sudo apt-get install php-fpm

# --- POSTGRESQL ---
sudo apt install postgresql
sudo apt install uuid-dev
sudo apt install finger
sudo apt install libpq-dev libgmp-dev
# --- GIT ---
sudo apt install git-all
sudo apt install unzip

# --- POSTGREST ---
sudo mkdir /gostyle
sudo mkdir /gostyle/postgrest
sudo chown -R user /gostyle/
sudo chmod 755 -R /gostyle
cd /gostyle/postgrest

# --- POSTGREST ---
uname -a
cd /gostyle/postgrest/
wget https://github.com/PostgREST/postgrest/releases/download/v6.0.2/postgrest-v6.0.2-ubuntu.tar.xz
tar xfJ postgrest-<version>-<platform>.tar.xz
./postgrest
# --- PRESTASHOP ---
cd /gostyle
mkdir /gostyle/prestashop
mkdir /gostyle/prestashop/www
mkdir /gostyle/prestashop/www/html
cd /gostyle/prestashop
wget https://download.prestashop.com/download/releases/prestashop_1.7.6.3.zip
cp prestashop_1.7.6.3.zip ./www/html
cd www/html
unzip prestashop_1.7.6.3.zip
chmod 777 -R /gostyle/prestashop/www
php -S localhost:8082
sudo ss -lptn 'sport = :8082'
```
```xml

```

## Setup apache2
```bash
cd /etc/apache2/
touch ./sites-avaiables/gostyle.conf
sudo touch ./sites-available/gostyle.conf
sudo nano ./sites-available/gostyle.conf
cd ./sites-available
sudo a2dissite 000-default.conf
sudo a2ensite gostyle.conf
sudo service apache2 reload
mkdir /gostyle/log
mkdir /gostyle/log/apache
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo sudo a2enmod proxy_ajp
sudo sudo a2enmod proxy_balancer
sudo a2enmod proxy_connect
sudo a2enmod proxy_html
sudo nano port.conf
# Change Listen port
sudo apache2ctl configtest
sudo service apache2 restart
sudo a2enmod proxy_fcgi setenvif
sudo a2enconf php7.2-fpm
sudo a2dismod php7.2 mpm_prefork
sudo a2enmod mpm_event
sudo systemctl restart apache2

apache2ctl configtest
```
```xml

```
## Setup mariadb
```bash
mkdir /gostyle/log/mariadb
chmod 777 /gostyle/log/mariadb

sudo service mariadb status
sudo mysql_secure_installation
# Press enter for root password
sudo mysql -u root -p
```

```sql
drop database prestashop;
CREATE USER 'ps_admin'@'localhost' IDENTIFIED BY 'EPSI_2020';
create database prestashop;
GRANT USAGE ON prestashop.* TO 'ps_admin'@'localhost' IDENTIFIED BY 'EPSI_2020';
GRANT ALL ON prestashop.* TO 'ps_admin'@'localhost' IDENTIFIED BY 'EPSI_2020';
FLUSH PRIVILEGES;
```

## SetUp PrestaShop
> Utilisateur prestashop
```text
username : gostyle
email : gostyle@gostyle.gostyle
password : EPSI_2020
```
> Set nginx timeout to 320
```text
proxy_connect_timeout       350;
proxy_send_timeout          350;
proxy_read_timeout          350;
send_timeout                350;
```
## Install PostgreSQL

## Install
`sudo -i -u postgres`
```sql
psql
\l # List databases
\dt # List table in current database
\d tableName # Describe table
SELECT version();
\g # Print previous command
\? # Print all avalaible commands
\e # Editor
-- ----------------------------------------
-- --- CREATE DATABASE and SCHEMA       ---
-- ---                                  ---
drop database if exists mspr_prestashop;
create database mspr_prestashop;
\c mspr_prestashop;
drop schema if exists mspr;
create schema mspr;
-- -------------------------
-- ---     CREATE USER   ---
-- ---                   ---
CREATE USER ps_admin WITH encrypted PASSWORD 'EPSI_2020';
GRANT ALL privileges ON database mspr_prestashop to ps_admin;
GRANT ALL privileges on SCHEMA mspr TO ps_admin;
GRANT ALL privileges ON ALL TABLES IN SCHEMA mspr TO ps_admin;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA mspr TO ps_admin;
-- -------------------------
-- --- CREATE TABLE USER ---
-- ---                   ---
drop table if exists mspr.user;
CREATE TABLE mspr.user(
   -- user_id SERIAL PRIMARY KEY,
   user_id integer PRIMARY KEY,
   email VARCHAR (355) NOT NULL,
   passwd VARCHAR (355) NOT NULL
);
-- alter table mspr.user  ALTER COLUMN passwd TYPE varchar(355);
\d mspr.user
delete from mspr.user;
insert into mspr.user(user_id, email,passwd) values (0,'email@email.fr','$2a$10$gt/8moSeQUxRsy13qbeE4edMnfbhKxIkSDB5NzYkY4BFz12KLn/MS');
select * from mspr.user;
-- ----------------------------
-- --- CREATE TABLE COUPON ---
-- ---                     ---
create extension if not exists "uuid-ossp";
drop table if exists mspr.coupon;
CREATE TABLE  mspr.coupon(
	coupon_id UUID NOT NULL DEFAULT uuid_generate_v4(), 
   	product_id integer NOT NULL,
   	value integer NOT NULL,
   	start_date date not null,
   	end_date date not null,
   	message varchar(355) not null,
   	description varchar(355) not null,
   	CONSTRAINT PK_COUPON PRIMARY KEY(coupon_id)
);
delete from mspr.coupon;
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(1,25,'01/01/2020','01/01/2021','REDUC','Utiliser ce coupon sur l article carnet de note en liege');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(2,5,'01/01/2020','01/01/2021','PAPER','Utiliser ce coupon sur l article carnet de note en carton');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(3,3,'01/01/2020','01/01/2021','PAPER','Utiliser ce coupon sur l article carnet de note en papier');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(4,2,'01/01/2020','01/01/2021','TOPCADOC','Utiliser ce coupon sur l article carnet de note en tissu');
insert into mspr.coupon(product_id,value,start_date,end_date,message,description) values(5,0.50,'01/01/2020','01/01/2021','FOXY','Utiliser ce coupon sur l article fox');
select * from mspr.coupon;

-- --------------------------
-- --- CREATE TABLE ADMIN ---
-- ---                    ---
drop table if exists mspr.admin;
CREATE TABLE mspr.admin(
   admin_id UUID NOT NULL DEFAULT uuid_generate_v4(), 
   email VARCHAR (355) NOT NULL,
   passwd VARCHAR (355) NOT NULL,
   CONSTRAINT PK_ADMIN PRIMARY KEY(admin_id)
);
\d mspr.admin
insert into mspr.admin(email,passwd) values ('email@email.fr','password');
insert into mspr.admin(email,passwd) values ('admin@email.fr','$2y$10$ehWoifyiW1tKUIgMZA9fmOLkOHpGw9oTniXkVlrTs889IY0LR58Uq');
insert into mspr.admin(email,passwd) values ('test@test.fr','$2a$10$gt/8moSeQUxRsy13qbeE4edMnfbhKxIkSDB5NzYkY4BFz12KLn/MS');

-- -------------------------------
-- --- CREATE TABLE HISTORIQUE ---
-- ---                         ---
drop table if exists mspr.historique;
CREATE TABLE mspr.historique(
   id UUID NOT NULL DEFAULT uuid_generate_v4(), 
   _date date null default CURRENT_DATE,
   coupon UUID not null,
   user integer null,
   CONSTRAINT PK_HISTORIQUE PRIMARY KEY(id)
);
\d mspr.historique
insert into mspr.historique(email,passwd) values ('email@email.fr','password');

```

## Install PostgREST
https://postgrest.org/en/v6.0/tutorials/tut0.html
https://postgrest.org/en/v3.2/api_reading.html

```bash
wget https://github.com/PostgREST/postgrest/releases/download/v6.0.2/postgrest-v6.0.2-ubuntu.tar.xz
tar xfJ postgrest-<version>-<platform>.tar.xz
./postgrest

./postgrest confFile.conf

```

```sql
create role web_anon nologin;
grant usage on schema mspr to web_anon;
grant select on mspr.user to web_anon;
grant select on mspr.coupon to web_anon;
grant select on mspr.admin to web_anon;
grant select on mspr.historique to web_anon;

grant insert on mspr.coupon to web_anon;
grant insert on mspr.historique to web_anon;
create role authenticator noinherit login password '123';
grant web_anon to authenticator;
```

/home/clement/postgrest.conf
```text
db-uri = "postgres://authenticator:123@localhost:5432/mspr_prestashop"
db-schema = "mspr"
db-anon-role = "web_anon"
server-port = 3002
jwt-secret = "G1ScV9Jv3bRBhcx18/kEziY4ElcUgF78M5W8J8SwbGU="
```



## Reverse engineering password hash in PrestaShop

Dans `PrestaShop\src\Core\Crypto` On trouve un fichier `Hashing.php` qui contient les deux fonctions de hashage utilisé à savoir MD5 et CRYPT_BLOWFISH (BCrypt). Le salt prend la valeur de `_COOKIE_KEY_`

$2y$10$wX9PDXl0WckFOvabaQouRuKwz0ahiexSAEWITWF2oTmhg.t2V6aKq
salt : wX9PDXl0WckFOvabaQouRu
hash : Kwz0ahiexSAEWITWF2oTmhg.t2V6aKq
password : password

$2y$10$k1j.66fpIizV6yoCW.hOtOHYDkCuc0BSTr.CEW4SjkYLqQ0MoV.Ya
Hash:	HYDkCuc0BSTr.CEW4SjkYLqQ0MoV.Ya
Salt:	$2y$10$k1j.66fpIizV6yoCW.hOtO
Password : password

### Conclusion

PrestaShop utilise Bcrypt avec un round de 10 et un salt égale à la variable php _COOKIE_KEY_

## Maria-DB trigger

```sql
SHOW VARIABLES LIKE 'plugin_dir';
-- /usr/lib/x86_64-linux-gnu/mariadb18/plugin/
```
```bash
wget https://github.com/mysqludf/lib_mysqludf_sys/archive/master.zip
sudo apt install unzip
sudo apt install default-libmysqlclient-dev
unzip master.zip

cd ./lib_mysqludf_sys-master/
gcc -DMYSQL_DYNAMIC_PLUGIN -fPIC -Wall -m64 -I/usr/include/mysql -I. -shared lib_mysqludf_sys.c -o lib_mysqludf_sys.so
sudo cp ./lib_mysqludf_sys.so /usr/lib/x86_64-linux-gnu/mariadb18/plugin/

sudo service mysql status
sudo service mysql stop
sudo service mysql start
sudo service mysql status

sudo mkdir /test_area
sudo mkdir /test_area/sys_execSQL
sudo chmod 777 sys_execSQL/
```

```sql
mysql -u admin -p 
-- DROP FUNCTION IF EXISTS sys_get;
-- DROP FUNCTION IF EXISTS sys_set;
DROP FUNCTION IF EXISTS sys_exec;
-- DROP FUNCTION IF EXISTS sys_eval;
-- CREATE FUNCTION lib_mysqludf_sys_info RETURNS string SONAME 'lib_mysqludf_sys.so';
-- CREATE FUNCTION sys_get RETURNS string SONAME 'lib_mysqludf_sys.so';
-- CREATE FUNCTION sys_set RETURNS int SONAME 'lib_mysqludf_sys.so';
CREATE FUNCTION sys_exec RETURNS int SONAME 'lib_mysqludf_sys.so';
-- CREATE FUNCTION sys_eval RETURNS string SONAME 'lib_mysqludf_sys.so';
SELECT sys_exec('curl http://stackoverflow.com/');
SELECT sys_exec('touch /test_area/sys_execSQL/test.txt');
```

```sql
SELECT sys_exec('curl http://stackoverflow.com/');
SELECT sys_exec('touch /test_area/sys_execSQL/test.txt');
\! ls /test_area/sys_execSQL/
```

```bash
mkdir /gostyle/mariadb/trigger
chmod 777 /gostyle/mariadb/trigger
```
```sql
select sys_exec('touch /gostyle/mariadb/trigger/mariaTrigger.py');
select sys_exec('python3 /gostyle/mariadb/trigger/mariaTrigger.py');
```
```bash
sudo nano /gostyle/mariadb/trigger/mariaTrigger.py
# Add python script
```

```sql
select sys_exec('python3 /gostyle/mariadb/trigger/mariaTrigger.py');

-- select sys_exec('python3 /gostyle/mariadb/trigger/mariaTrigger.py insert 11 jeanbon@jeanbon.jeanbon yz0TShAG29Xjk4x4jcAzt.bZgOeML3JL5lh5wZjfyQ9ajdyPqrfNu');
-- update ps_customer set email = 'testemail' where id_customer = 11;
```

### Check apparmor
```bash
sudo apparmor_status
sudo ln -s /etc/apparmor.d/usr.sbin.mysqld /etc/apparmor.d/disable/
sudo apparmor_parser -R /etc/apparmor.d/usr.sbin.mysqld

# Reset
sudo rm /etc/apparmor.d/disable/usr.sbin.mysqld
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.mysqld
sudo aa-status
```

### Conclusion, trigger final
```sql
-- INSERT TRIGGER
DELIMITER @@
CREATE or REPLACE TRIGGER ps_customer_insert
AFTER INSERT ON ps_customer
FOR EACH ROW 
BEGIN
	DECLARE cmd CHAR(255);
 	DECLARE result int;
 	DECLARE state CHAR(50);
 	SET state = 'insert';
 	SET cmd= CONCAT('python3 /gostyle/mariadb/trigger/mariaTrigger.py ',state,' ',NEW.id_customer,' ',NEW.email,' ',REPLACE(NEW.passwd, '$', '\\$'));
 	SET result = sys_exec(cmd);
 	SET result = sys_exec(CONCAT('echo "',cmd,'">> /gostyle/log/mariadb/command.log'));
END;
@@
DELIMITER ;
-- UPDATE TRIGGER
DELIMITER @@
CREATE or REPLACE TRIGGER ps_customer_update
AFTER UPDATE ON ps_customer
FOR EACH ROW 
BEGIN
	DECLARE cmd CHAR(255);
 	DECLARE result int;
 	DECLARE state CHAR(50);
 	SET state = 'update';
 	SET cmd= CONCAT('python3 /gostyle/mariadb/trigger/mariaTrigger.py ',state,' ',NEW.id_customer,' ',NEW.email,' ',REPLACE(NEW.passwd, '$', '\\$'));
 	SET result = sys_exec(cmd);
 	SET result = sys_exec(CONCAT('echo "',cmd,'">> /gostyle/log/mariadb/command.log'));
END;
@@
DELIMITER ;
-- DELETE TRIGGER
DELIMITER @@
CREATE or REPLACE TRIGGER ps_customer_delete
AFTER DELETE ON ps_customer
FOR EACH ROW 
BEGIN
	DECLARE cmd CHAR(255);
 	DECLARE result int;
 	DECLARE state CHAR(50);
 	SET state = 'delete';
 	SET cmd= CONCAT('python3 /gostyle/mariadb/trigger/mariaTrigger.py ',state,' ',OLD.id_customer);
 	SET result = sys_exec(cmd);
 	SET result = sys_exec(CONCAT('echo "',cmd,'">> /gostyle/log/mariadb/command.log'));
END;
@@
DELIMITER ;
```

JWT secret password : G1ScV9Jv3bRBhcx18/kEziY4ElcUgF78M5W8J8SwbGU=
jwt-secret = "G1ScV9Jv3bRBhcx18/kEziY4ElcUgF78M5W8J8SwbGU="


HEADER : {
  "alg": "HS256",
  "typ": "JWT"
}
PAYLOAD : {
  "role":"web_anon"
}
SIGNATURE:
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload), "G1ScV9Jv3bRBhcx18/kEziY4ElcUgF78M5W8J8SwbGU="
) 

result token : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoid2ViX2Fub24ifQ.GwMCqBzBEjoLCL9zW69xziOa_XsCYlfoDYxmXMGPHwI
export TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoid2ViX2Fub24ifQ.GwMCqBzBEjoLCL9zW69xziOa_XsCYlfoDYxmXMGPHwI"

curl https://pgrest.julespeguet.fr/historique -X POST      -H "Authorization: Bearer $TOKEN"        -H "Content-Type: application/json"      -d '{"_date": "01/01/2020","coupon":"36742bb1-b8cd-40a8-ad02-312db5d57bc8"}'


## Upload file

```bash
scp '-P 443' ./* ct@82.229.120.121:/tmp/gostyle
scp ./* ct@192.168.0.14:/gostyle/admin
tar xvf zip.tar
tar -ygz 
```


## Install admin website

```bash
mkdir /gostyle/admin
mkdir /gostyle/admin/html
mkdir /gostyle/admin/html/www
```

## NGINX conf

```c
server {
        listen 80;
        server_name _;
        return 301 https://$host$request_uri;
}

server {
        listen 443 ssl;
        server_name gitlab.julespeguet.fr;
        ssl on;
#        ssl_certificate /etc/nginx/ssl/gitlab.julespeguet.fr.crt;
#        ssl_certificate_key /etc/nginx/ssl/gitlab.julespeguet.fr.key;
        ssl_certificate /etc/letsencrypt/live/julespeguet.fr/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/julespeguet.fr/privkey.pem;
        location / {
                proxy_pass https://192.168.1.41;
                proxy_set_header Host $host;
                proxy_redirect http:// https://;
        }
}
server {
        listen 80;
        server_name shop.julespeguet.fr;
        location / {
                proxy_pass http://192.168.1.93;
                proxy_set_header Host $host;
               	proxy_redirect http:// https://;
                proxy_connect_timeout 350;
                proxy_send_timeout 350;
                proxy_read_timeout 350;
                send_timeout 350;
        }
}


server {
        listen 443 ssl;
#        listen 80;
        server_name pgrest.julespeguet.fr admin.julespeguet.fr shop.julespeguet.fr dotnet.julespeguet.fr;
        ssl on;
        ssl_certificate /etc/letsencrypt/live/julespeguet.fr/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/julespeguet.fr/privkey.pem;
        location / {
        #       import proxy_params;
                proxy_pass http://192.168.1.93;
                proxy_set_header Host $host;
#               proxy_set_header X-Real-IP $remote_addr;
#               proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#               proxy_set_header X-Forwarded-Proto $scheme;
                proxy_redirect http:// https://;
                proxy_connect_timeout       350;
                proxy_send_timeout          350;
                proxy_read_timeout          350;
                send_timeout                350;
        }
}
```

## DOTNET

```bash
sudo a2enmod headers

```

## Sonarqube

```bash
sudo apt install default-jdk
java -version

# Oracle version
#sudo apt install software-properties-common
#sudo add-apt-repository ppa:linuxuprising/java
#sudo apt update
#sudo apt install oracle-java11-installer
#java -version
#sudo update-alternatives --config java
#sudo nano /etc/environment
# OpenJDK 11 is located at /usr/lib/jvm/java-11-openjdk-amd64/bin/java
# OpenJDK 8 is located at /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
#sudo nano /etc/environment
#JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
#source /etc/environment
#echo $JAVA_HOME
#sudo apt remove openjdk-8-jdk
sudo apt install default-jdk
java -version
sudo apt install docker.io
docker run -d --name sonarqube -p 9000:9000 sonarqube
openssl rand -base64 32
mkdir /gostyle/sonarqube
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.2.0.1873-linux.zip
unzip sonar-scanner-cli-4.2.0.1873-linux.zip
nano /gostyle/sonarqube/sonar-scanner-4.2.0.1873-linux/conf/sonar-scanner.properties
#/conf/sonar-scanner.properties:
#----- Default SonarQube server
#sonar.host.url=http://localhost:9000
# FAUT ALLER SUR localhost:9000
cd /gostyle/sonarqube/
git clone https://gitlab.julespeguet.fr/Clement/mspr_admin_vuejs.git
cd /gostyle/sonarqube/mspr_admin_vuejs
git pull
/gostyle/sonarqube/sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner \
  -Dsonar.projectKey=vuejs \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonar.julespeguet.fr \
  -Dsonar.login=01694fcefff4cc9856fd2c7d8938b3cda2e56525


cd /gostyle/sonarqube/
git clone https://gitlab.julespeguet.fr/Jules/mspr_dev_react.git
cd /gostyle/sonarqube/mspr_dev_react
git pull
/gostyle/sonarqube/sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner \
  -Dsonar.projectKey=react-native \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonar.julespeguet.fr \
  -Dsonar.login=ff60967c9133b9d47490007c3c47c667b624603d


cd /gostyle/sonarqube/
git clone https://gitlab.julespeguet.fr/Jules/mspr_api_dotnet.git
cd /gostyle/sonarqube/mspr_api_dotnet
git pull
/gostyle/sonarqube/sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner \
  -Dsonar.projectKey=dotnet \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonar.julespeguet.fr \
  -Dsonar.login=a6e07c0dae141dff4568779deef1b5550b613eb3

cd /gostyle/sonarqube/
git clone https://gitlab.julespeguet.fr/Clement/python_trigger.git
cd /gostyle/sonarqube/python_trigger
git pull
/gostyle/sonarqube/sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner \
  -Dsonar.projectKey=python_trigger \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonar.julespeguet.fr \
  -Dsonar.login=1788355faf26d273f77f3adc00a3740a0c05fc33


cd /gostyle/sonarqube/
git clone https://gitlab.julespeguet.fr/Clement/testapi_pytest.git
cd /gostyle/sonarqube/testapi_pytest/
git pull
/gostyle/sonarqube/sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner \
  -Dsonar.projectKey=testapi_pytest \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://sonar.julespeguet.fr \
  -Dsonar.login=505a166400325b76523e13a98b3d9dbaaa19b2a6


```


> sonarqube : https://sonar.julespeguet.fr/
> username : admin
> passwd : +0r8b2MphS1O2r7eW3050+EW0LcFn/YH6Uf3yhj4S4Y=
> token vuejs: 01694fcefff4cc9856fd2c7d8938b3cda2e56525
> token react-native: ff60967c9133b9d47490007c3c47c667b624603d
> token dotnet: a6e07c0dae141dff4568779deef1b5550b613eb3
> token dotnet_api: 54e7471a8457b94846fc621a5c33cd9c781f2424
> token python_trigger: 1788355faf26d273f77f3adc00a3740a0c05fc33
> token testapi_pytest: 505a166400325b76523e13a98b3d9dbaaa19b2a6






git init
git remote add origin git@gitlab.julespeguet.fr:Clement/python_trigger.git
git add .
git commit -m "Initial commit"
git push -u origin master
git checkout -b develop
git add .
git commit -m "Add develop branch"
git push --set-upstream origin develop


## Setup pytest

```bash
pip3 install -U pytest
pytest --version
touch test_firstTest.py
nano test_firstTest.py
pytest -q test_sysexit.py # -q for quiet
pytest
```

```py
# content of test_sysexit.py
import pytest

def f():
    raise SystemExit(1)

def func(x):
    return x + 1

def test_mytest():
    with pytest.raises(SystemExit):
        f()
def test_answer():
    assert func(3) == 5
```

```bash
apache2ctl -V
mysql select version();
uname -a

```