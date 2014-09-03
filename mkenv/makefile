sys_install = apt-get -y install
pip = pip install -i http://pypi.douban.com/simple

about:
	@echo "LYC"

recommend: system git k-vim python python-dev ssh mysql
	rm -rf k-vim
	@echo "Enjoy!"

system:
	$(sys_install) npm
	$(sys_install) lrzsz
	$(sys_install) vim

git:
	$(sys_install) git

k-vim: git system
	git clone https://github.com/wklken/k-vim.git || true
	$(sys_install) ctags
	$(sys_install) build-essential cmake python-dev

python:
	$(sys_install) python
	wget https://bootstrap.pypa.io/ez_setup.py -O - | python
	rm setuptools*.zip
	easy_install pip

python-dev: python k-vim
	$(pip) pyflakes pylint pep8 pytest ipython virtualenv
	sh -x k-vim/install.sh

javascript-dev: k-vim
	$(sys_install) nodejs
	npm install -g jslint
	npm install jshint -g

java-jre:
	$(sys_install) default-jre

lein:
	mkdir ~/bin/;wget -O ~/bin/lein https://raw.github.com/technomancy/leiningen/stable/bin/lein && chmod +x ~/bin/lein && ~/bin/lein

mysql:
	$(sys_install) mysql-server mysql-client

ssh: system
	$(sys_install) ssh
	/etc/init.d/ssh restart
