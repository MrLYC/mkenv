sys_install = apt-get -y install
pip = pip install -i http://pypi.douban.com/simple
k_vim = /opt/k-vim

about:
	@echo "LYC"

recommend: system git-flow k-vim python python-dev ssh
	@echo "Enjoy!"

usr-bin:
	[ -e "~/bin/" ] || mkdir "~/bin/"

clean:
	rm ./* -rf
	git checkout -- .

source-list:
	cp /etc/apt/sources.list ./sources.list.old
	./add_source_list.py

add-apt-repository:
	add-apt-repository ppa:fcwu-tw/ppa -y

apt-update: source-list add-apt-repository
	apt-get update

system: apt-update
	$(sys_install) npm
	$(sys_install) lrzsz
	$(sys_install) vim

git:
	$(sys_install) git

git-flow:
	$(sys_install) git-flow

git-config:
	git config --global user.name lyc
	git config --global user.email saber000@vip.qq.com
	git config --global core.editor vim
	git config --global merge.tool vimdiff
	git config --global color.ui true

k-vim: git system
	[ -e $(k_vim) ] || git clone https://github.com/wklken/k-vim.git $(k_vim)
	$(sys_install) ctags
	$(sys_install) build-essential cmake python-dev

python:
	$(sys_install) python-dev
	[ -e setuptools.zip ] || wget https://bootstrap.pypa.io/ez_setup.py -O setuptools.zip | python
	rm setuptools*.zip
	easy_install pip

python-dev: python k-vim
	$(pip) -r requirements-dev.txt
	sh -x $(k_vim)/install.sh

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
	[ -e redis-2.8.14.tar.gz ] || wget http://download.redis.io/releases/redis-2.8.14.tar.gz
	tar xzf redis-2.8.14.tar.gz
	rm redis-2.8.14.tar.gz
	cd redis-2.8.14 && make && cp redis.conf /etc/
	cd redis-2.8.14/src && cp redis-benchmark redis-cli redis-server /usr/bin/

clr: usr-bin
	echo printf \"\\ec\" > ~/bin/clr && chmod 777 ~/bin/clr

hide-sysui:
	sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"/GRUB_CMDLINE_LINUX_DEFAULT="text"/g' /etc/default/grub
	update-grub

compile-YCM:
	cd ~/.vim/bundle/YouCompleteMe && ./install.sh

stackless:
	$(sys_install) install libreadline-dev
	$(sys_install) build-dep python2.7
	[ -e stackless.tar.bz2 ] || wget http://www.stackless.com/binaries/stackless-272-export.tar.bz2 -O stackless.tar.bz2
	bunzip2 stackless.tar.bz2
	tar xf stackless.tar
	cd stackless-272-export/ && ./configure --prefix=/opt/stackless --enable-unicode=ucs4 && make && make install
