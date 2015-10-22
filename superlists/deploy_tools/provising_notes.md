Provisioning a new site
=======================
## Required packages:
*
*
*
*
*
nginx
Python 3
Git
pip
virtualenv
eg, on Ubuntu:
sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv
## Nginx Virtual Host config
* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com
## Upstart Job
* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com
## Folder structure:
Assume we have a user account at /home/username
/home/username
└── sites
└── SITENAME
├── database
├── source
├── static
└── virtualenv





elspeth@TestPython:~/sites/mylistspython.tk/source/superlists$ tree -I __pycache
.
├── deploy_tools
│   ├── fabfile.py
│   ├── gunicorn-upstart.template.conf
│   ├── nginx.template.conf
│   └── provising_notes.md
├── functional_tests
│   ├── __init__
│   └── tests.py
├── lists
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_item_text.py
│   │   ├── 0004_item_list.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-34.pyc
│   │       ├── 0002_item_text.cpython-34.pyc
│   │       ├── 0004_item_list.cpython-34.pyc
│   │       └── __init__.cpython-34.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── __init__.cpython-34.pyc
│   │   ├── models.cpython-34.pyc
│   │   ├── tests.cpython-34.pyc
│   │   ├── urls.cpython-34.pyc
│   │   └── views.cpython-34.pyc
│   ├── static
│   │   ├── base.css
│   │   └── bootstrap
│   │       ├── css
│   │       │   ├── bootstrap.css
│   │       │   ├── bootstrap.css.map
│   │       │   ├── bootstrap.min.css
│   │       │   ├── bootstrap-theme.css
│   │       │   ├── bootstrap-theme.css.map
│   │       │   └── bootstrap-theme.min.css
│   │       ├── fonts
│   │       │   ├── glyphicons-halflings-regular.eot
│   │       │   ├── glyphicons-halflings-regular.svg
│   │       │   ├── glyphicons-halflings-regular.ttf
│   │       │   └── glyphicons-halflings-regular.woff
│   │       └── js
│   │           ├── bootstrap.js
│   │           └── bootstrap.min.js
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   └── list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requerements.txt
├── requerimientos.txt
└── superlists
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-34.pyc
    │   ├── settings.cpython-34.pyc
    │   ├── urls.cpython-34.pyc
    │   └── wsgi.cpython-34.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py



//etc/nginx/site-ava/testinggoat.tk

server {
listen 80;
server_name testinggoat.tk;
location /static {
alias /home/elspeth/sites/mylistspython.tk/static;
}

location / {
proxy_set_header Host $host;
proxy_pass http://unix:/tmp/testinggoat.tk.socket;
}
#location / {
#proxy_pass http://localhost:8000;
#}
}



//etc/init/testinggoat.conf
description "Gunicorn server for superlists.testinggoat.tk"
start on net-device-up
stop on shutdown
respawn
setuid elspeth
chdir /home/elspeth/sites/mylistspython.tk/source/superlists
exec ../../virtualenv/bin/gunicorn --bind unix:/tmp/testinggoat.tk.socket superlists.wsgi:application

