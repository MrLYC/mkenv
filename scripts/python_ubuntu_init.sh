#!/bin/bash

sudo apt-get install -y python-dev python-pip
sudo pip install virtualenv

sudo apt-get install -y build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev

wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
tar -xvf Python-3.5.2.tgz
cd Python-3.5.2
./configure --prefix=/usr/
make
sudo make install

sudo cp /usr/bin/pip* /usr/local/bin/
sudo cp /usr/bin/pip /usr/local/bin/pip2

common_packages='
PyYAML
wheel
gunicorn
celery
ipython
pep8
pylint
pytest
redis
wrapt
jsonschema
requests
tornado
Django
Flask
six
'

sudo apt-get install -y libmysqlclient-dev

sudo pip2 install -q \
    fabric \
    supervisor \
    MySQL-python \
    pathlib2 \
    backports.shutil_get_terminal_size \
    ${common_packages}

sudo pip3 install -q \
    mysqlclient \
    ${common_packages}
