sys_install = apt-get -y install
pip = pip install -i http://pypi.douban.com/simple

about:
	@echo "LYC"

recommend: system git-flow k-vim python python-dev ssh
	@echo "Enjoy!"

usr-bin:
	[ -e "~/bin/" ] || mkdir "~/bin/"

run:
	@mkdir .temp-floder
	@cp makefile .temp-floder/

	cd .temp-floder && make recommend || true
	@rm -rf .temp-floder

system:
	$(sys_install) npm
	$(sys_install) lrzsz
	$(sys_install) vim

git:
	$(sys_install) git

git-flow:
	$(sys_install) git-flow

k-vim: git system
	git clone https://github.com/wklken/k-vim.git || true
	$(sys_install) ctags
	$(sys_install) build-essential cmake python-dev

python:
	$(sys_install) python-dev
	wget https://bootstrap.pypa.io/ez_setup.py -O - | python
	rm setuptools*.zip
	easy_install pip

python-dev: python k-vim
	$(pip) -r requirements-dev.txt
	sh -x k-vim/install.sh

javascript-dev: k-vim
	$(sys_install) nodejs
	npm install -g jslint
	npm install jshint -g

java-jre:
	$(sys_install) default-jre

lein: usr-bin
	wget -O ~/bin/lein https://raw.github.com/technomancy/leiningen/stable/bin/lein && chmod +x ~/bin/lein && ~/bin/lein

mysql:
	$(sys_install) mysql-server mysql-client
	$(sys_install) libmysqld-dev

ssh: system
	$(sys_install) ssh
	/etc/init.d/ssh restart

redis:
	wget http://download.redis.io/releases/redis-2.8.14.tar.gz
	tar xzf redis-2.8.14.tar.gz
	rm redis-2.8.14.tar.gz
	cd redis-2.8.14 && make && cp redis.conf /etc/
	cd redis-2.8.14/src && cp redis-benchmark redis-cli redis-server /usr/bin/

clr: usr-bin
	echo printf \"\\ec\" > ~/bin/clr && chmod 777 ~/bin/clr

hide-sysui:
	sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"/GRUB_CMDLINE_LINUX_DEFAULT="text"/g' /etc/default/grub
	update-grub
