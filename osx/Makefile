sys_install = brew install
pip = pip install -i http://pypi.douban.com/simple

.PHONY: about
about:
	@echo "LYC"

.PHONY: homebrew
homebrew:
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

.PHONY: pyaudio
pyaudio:
	$(sys_install) portaudio
	$(pip) pyaudio

.PHONY: crontab
crontab:
	echo "export EDITOR=vim" >> ~/.bashrc
	echo "alias crontab="VIM_CRONTAB=true crontab" >> ~/.bashrc

	echo 'if $VIM_CRONTAB == "true"' >> ~/.vimrc
	echo "    set nobackup" >> ~/.vimrc
	echo "    set nowritebackup" >> ~/.vimrc
	echo "endif" >> ~/.vimrc
