sys_install = "apt-get -y install"
pip = "pip install -i http://pypi.douban.com/simple"

about:
	echo "LYC"

system:
	$(sys_install) npm
	$(sys_install) lrzsz
	$(sys_install) vim

git:
	$(sys_install) git

k-vim: git system
	git clone https://github.com/wklken/k-vim.git
	$(sys_install) ctags
	$(sys_install) build-essential cmake python-dev

python:
	$(sys_install) python
	wget https://bootstrap.pypa.io/ez_setup.py -O - | python
	easy_install pip

python-dev: python k-vim
	$(pip) pyflakes pylint pep8 pytest ipython virtualenv
	cd k-vim/
	install.sh
	cd ../

javascript-dev: k-vim
	$(sys_install) nodejs
	npm install -g jslint
	npm install jshint -g

mysql:
	$(sys_install) mysql-server mysql-client
