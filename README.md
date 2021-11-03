# Fast-rails

## Install rails in one command!

## Usage (Ubuntu 16.04)
I recommend changing the directory to /home and doing nothing from the root

run main script
```
cd ./fast-rails
sudo ./fast-rails.sh -sys YOUR_USER_NAME -rb YOUR_RUBY_VERSION -node YOUR_NODE_VERSION
```
YOUR_USER_NAME - working user on whose behalf the connection to the database and work with the project will be performed

YOUR_RUBY_VERSION - desired ruby version (do not forget that ruby version must be equal with project ruby version)

YOUR_NODE_VERSION - desired node js version

this script will install  nessary libraries
 - nodejs
 - postgresql
 - nginx
 - ruby-build
 - rbenv
 - bundler
 
and dependencies
 
## Configure postgresql
open config file
```
sudo nano /etc/postgresql/9.5/main/pg_hba.conf
```
and after “put your actual configuration here" write:

```
host  all     YOUR_USER_NAME    127.0.0.1/32      trust
host  all     YOUR_USER_NAME    ::1/128           trust
```

then restart postgres

```
sudo systemctl restart postgresql
```

## Configure nginx
after successful script performing you need to configure nginx

create file with name of your domain(in our example - "example.com") in dir: /etc/nginx/sites-available
```
nano /etc/nginx/sites-available/example.com
```
open file and write something like

```
upstream puma {
  server 127.0.0.1:5000;
}
server {
  listen 80;
  listen [::]:80;
  
  server_name example.com;
  
  root /path/to/your/public/directory;
  try_files $uri/index.html $uri @rails;
  
  location @rails {
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_pass http://puma$request_uri;
  }
  location ^~ /assets/ {
    gzip_static on;
    expires max;
    add_header Cache-Control public;
  }
  location ^~ /system/ {
    gzip_static on;
    expires max;
    add_header Cache-Control public;
  }
  error_page 500 502 503 504 /500.html;
  error_page 404 /404.html;
  error_page 422 /422.html;
  client_max_body_size 10M;
  keepalive_timeout 10;
}
```

/path/to/your/public/directory - public folder in rails project
