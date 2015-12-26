sys_install = apt-get -y install
pip = pip install -i http://pypi.douban.com/simple
k_vim = /opt/k-vim
gitconf = git config --global

about:
	@echo "LYC"

recommend: system git-flow k-vim python python-dev ssh
	@echo "Enjoy!"

usr-bin:
	[ -e "~/bin/" ] || mkdir -p ~/bin/

clean:
	rm ./* -rf
	git checkout -- .

source-list:
	cp /etc/apt/sources.list ./sources.list.old
	./add_source_list.py

add-apt-repository:
	which add-apt-repository || $(sys_install) python-software-properties software-properties-common
	add-apt-repository ppa:fcwu-tw/ppa -y

apt-update: source-list
	apt-get update

system: apt-update
	$(sys_install) lrzsz
	$(sys_install) vim

git:
	$(sys_install) git

git-flow:
	$(sys_install) git-flow

git-config:
	$(gitconf) user.name MrLYC
	$(gitconf) user.email imyikong@gmail.com
	$(gitconf) core.editor vim
	$(gitconf) merge.tool vimdiff
	$(gitconf) color.ui true
	$(gitconf) push.default simple

k-vim: git system
	[ -e $(k_vim) ] || git clone https://github.com/wklken/k-vim.git $(k_vim)
	$(sys_install) build-essential cmake ctags
	sh -x $(k_vim)/install.sh

python:
	$(sys_install) python-dev
	[ `which pip` ] || [ -e setuptools.py ] || wget https://bootstrap.pypa.io/ez_setup.py -O setuptools.py | python
	rm setuptools*.zip || true
	easy_install pip

python-dev: python k-vim
	$(pip) -r requirements-dev.txt

python3-dev:
	$(sys_install) python3-dev python3-pip

javascript-dev: k-vim
	$(sys_install) nodejs
	$(sys_install) npm
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

redis-tools:
	$(sys_install) redis-tools

clr:
	echo printf \"\\ec\" > /bin/clr && chmod 777 /bin/clr

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

q-text: usr-bin
	git clone https://github.com/harelba/q.git
	cp q/bin/q ~/bin/

lxml: python
	$(sys_install) libxml2-dev libxslt1-dev
	apt-get build-dep python-lxml
	$(pip) lxml

cheat: python
	pip install docopt pygments
	[ -e "cheat" ] || git clone https://github.com/chrisallenlane/cheat.git
	cd cheat && python setup.py install
	cheat -v

pptpd:
	$(sys_install) pptpd
	./pptpd_cfg.py
	service pptpd restart
	$(eval ethn ?= eth0)
	iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o $(ethn) -j MASQUERADE
	echo "selected $(ethn)"

profile:
	cp ./lyc_profile.sh /etc/profile.d/
	chmod 777 /etc/profile.d/lyc_profile.sh

rsync:
	wget http://rsync.samba.org/ftp/rsync/src/rsync-3.0.9.tar.gz
	tar xf rsync-3.0.9.tar.gz
	cd rsync-3.0.9
	./configure && make && make install

synctime:
	ntpdate cn.pool.ntp.org
	cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
	hwclock --systohc

git-alias:
	$(gitconf) alias.co 'checkout'
	$(gitconf) alias.br 'branch'
	$(gitconf) alias.cm 'commit -m'
	$(gitconf) alias.st 'status'
	$(gitconf) alias.last 'log -1 HEAD'
	$(gitconf) alias.rpo 'pull --rebase origin'
	$(gitconf) alias.rp 'pull --rebase'
	$(gitconf) alias.po 'push origin'
	$(gitconf) alias.hist 'log --pretty=format:"%h | %ad | %an: %s%d" --graph --date=short'
	$(gitconf) alias.diffh 'diff HEAD'
	$(gitconf) alias.cbr 'checkout -b'
	$(gitconf) alias.amend 'commit --amend'

docker:
	curl -sSL https://get.docker.com/ | sh

puppet:
	wget https://apt.puppetlabs.com/puppetlabs-release-precise.deb
	dpkg -i puppetlabs-release-precise.deb
	apt-get update
	
puppet-master: puppet
	$(sys_install) puppetmaster-passenger
	puppet resource package puppet ensure=latest
	
puppet-agent: puppet
	$(sys_install) puppet
	puppet resource package puppet ensure=latest
	/etc/init.d/puppet start
