
# Config exemple application 

## Install
```sh
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install nodejs npm
nodejs -v
npm -v
sudo apt install apache2
#sudo a2enmod cgid


nano /etc/apache2/apache2.conf
# IncludeOptional /mnt/e/Documents/EPSI/CDA_B3/Orale/app/apache/*.conf 

sudo a2dissite cdapres
sudo a2ensite cdapres

chmod a+x fileName.py
# sudo chown -R $USER:www-data /mnt/e/Documents/EPSI/CDA_B3/Orale/app/apache2/www/
```


```
# /mnt/e/Documents/EPSI/CDA_B3/Orale/app

ServerTokens Prod
ServerSignature On

<VirtualHost *:80>
	
	#ServerName www.example.com
	ServerAdmin webmaster@localhost
	#ServerSignature Off
	#ServerTokens Prod


	# -------------------- WEB --------------------
	DocumentRoot /mnt/e/Documents/EPSI/CDA_B3/Orale/app/apache/www/
	<Directory "/mnt/e/Documents/EPSI/CDA_B3/Orale/app/apache/www/">
		Options +FollowSymLinks
		AllowOverride all
		Require all granted
	</Directory>
	# -------------------- CGI --------------------
	ScriptAlias /api/ /mnt/e/Documents/EPSI/CDA_B3/Orale/app/python/cdapres.py
	<Directory "/mnt/e/Documents/EPSI/CDA_B3/Orale/app/python/">
		#SetHandler cgi-script
		#AllowOverride None
		#Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
		#allow from all
		Require all granted
		Options +ExecCGI
		AddHandler cgi-script .py
	</Directory>
	# -------------------- LOG --------------------
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

#sudo apt install libapache2-mod-python

#ServerTokens   Full (or not specified) 
#Info sent to clients: Server: Apache/2.4.2 (Unix) PHP/4.2.2 MyMod/1.2 
#ServerTokens   Prod[uctOnly] 
#Info sent to clients: Server: Apache 
#ServerTokens   Major 
#Info sent to clients: Server: Apache/2 
#ServerTokens   Minor 
#Info sent to clients: Server: Apache/2.4 
#ServerTokens   Min[imal] 
#Info sent to clients: Server: Apache/2.4.2 
#ServerTokens   OS 
#Info sent to clients: Server: Apache/2.4.2 (Unix) 
```

## Code
```python
#!/usr/bin/env python3
# -*- coding : utf-8 -*-
import cgi
import cgitb

# Active debug mod, print error in browser windows
cgitb.enable()

print ('Content-type: text/html')
print ('Content-Language: Latin')
print ('Age: 1234567980')
print ('Status: 442 Coroned')
print ('Location: https://www.google.com')
print ('MyHeader: Chech')
print ('Connection: Coroned')
print ('Server: Unknown')
print('\n\n')

print ("<h1>It's Work !</h1><br/>")
data = cgi.FieldStorage()
print(data)

print("<hr/>")
cgi.print_environ()
```


