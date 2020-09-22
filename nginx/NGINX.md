# NGINX
> cbarange | September 21th 2020
---

**Sources :**
* https://medium.com/@jovanshernandez/what-is-nginx-f0a9c3a49a41
* https://medium.com/adrixus/beginners-guide-to-nginx-configuration-files-527fcd6d5efd 
* https://medium.com/javarevisited/nginx-better-and-faster-web-server-technology-72ce5ad6305a
* https://medium.com/@admantium/nginx-as-a-reverse-proxy-38ed79762a7c
* https://tutorials.botsfloor.com/top-tutorials-to-learn-nginx-for-web-server-dc8638c48fae
* https://upcloud.com/community/tutorials/configure-load-balancing-nginx/


## Installation
Build a LEMP (Linux, NGINX, MySQL, and PHP/Python) not a LAMP (Linux, Apache , MySQL, and PHP)
```bash
sudo apt-get update
sudo apt-get install nginx -y
# Check service status
sudo systemctl status nginx
# Stop service
sudo systemctl stop nginx
# Start service
sudo systemctl start nginx
# Restart service, stop and start service
sudo systemctl restart nginx
# Reload without dropping connections
# if your config is bad nginx will still running opposite to restart command
sudo systemctl reload nginx
# Start automatically NGINX at machine boot
sudo systemctl enable nginx
# Disable automatic start at machine boot
sudo systemctl disable nginx
# Test config file
sudo nginx -t
```
**Some Familiar Files**
```bash
# Directory of default web content
/var/www/html
# Configuration directory
/etc/nginx
# Main NGINX configuration file
/etc/nginx/nginx.conf
# Directory of all web site special configurations
/etc/nginx/sites-available/
# Directory of all active web sites
/etc/nginx/sites-enabled/
# Directory of configuration fragments
/etc/nginx/snippets

# Every request to web server
/var/log/nginx/access.log
# Every NGINX errors
/var/log/nginx/error.log
```

## Setup

### Basic

```bash
# /etc/nginx/sites-enabled
server {
    listen 80 default_server;
    listen [::]:80 default_server; 
    root /var/www/html;  
    index index.html; 
    server_name _;  
    location / {
       try_files $uri $uri/ =404;
     }
}
```

```bash
server {
    listen 80 default_server;
    listen [::]:80 default_server; 
    root /var/www/html;  
    index index.html; 
    server_name _;  
    location / {
       try_files $uri $uri/ =404;
    }
    location /api/ {
           proxy_pass http://localhost:8080/;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
    }
    location /images {
           alias uploads/images/;
    }
}
```

```bash
# Make sur to use full path not relative 
sudo ln -s /etc/nginx/sites-available/mwa.conf /etc/nginx/sites-enabled/
```

```bash

server {
	listen 80;
	listen [::]:80;

	# server_name example.com;
	server_name _;

	root /var/www/html/;
	index index.html;

	location / {
		try_files $uri $uri/ =404;
	}

	location /8080 {
       proxy_pass http://localhost:8080/;
    }

    location /8081 {
       proxy_pass http://localhost:8081/;
    }

    location /8082 {
       proxy_pass http://localhost:8082/;
    }
}

server {
	listen 8080;
	#listen [::]:8080;
	server_name _;
	root /var/www/html/;
	index index_8080.html;
}
server {
	listen 8081;
	server_name _;
	root /var/www/html/;
	index index_8081.html;
}
server {
	listen 8082;
	#listen [::]:8082;
	server_name _;
	root /var/www/html/;
	index index_8082.html;
}
```

### Log

```bash

```


```bash

```

### Proxy

```bash

```


```bash

```

### SSL

```bash

```


```bash

```

### Secure NGINX installation




### Varnish

```bash

```


```bash

```

### Cache

```bash

```


```bash

```

### Monitoring

```bash

```


```bash

```

## Maintenance

```bash

```


```bash

```

## Evolution

```bash

```


```bash

```

## Remove

```bash

```


```bash

```





