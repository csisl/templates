#!/bin/bash
set -e

# script to run after installing Ubuntu for quick customizations 
# usage: ./linux-setup

# color codes 
CRED='\e[31m'
CGREEN='\e[32m'
CBLUE='\e[34m'
CRESET='\e[39m'

# first ensure the system is up to date
update_system(){
	sudo apt-get update
	sudo apt-get upgrade
}

# create vimrc file 
create_vimrc(){
	echo -e "${CGREEN}CREATING .vimrc FILE${CRESET}"
	echo "set ai sw=4" > ~/.vimrc_TEST
	echo "set number" >> ~/.vimrc_TEST
	echo "set smartindent" >> ~/.vimrc_TEST
	echo "syntax on" >> ~/.vimrc_TEST
	echo "filetype indent on" >> ~/.vimrc_TEST
	echo "set showmatch" >> ~/.vimrc_TEST
	echo "set hlsearch" >> ~/.vimrc_TEST
	echo "set tabstop=4" >> ~/.vimrc_TEST
}

# install java
install_java() {
	echo -e "${CGREEN}INSTALLING JAVA 8$CRESET"
	sudo add-apt-repository ppa:webupd8team/java
	sudo apt-get update
	sudo apt-get install oracle-java8-installer
	sudo apt-get install oracle-java8-set-default
	# verify the installation version
	java -version
}

# install spotify
install_spotify(){
	echo -e "${CGREEN}INSTALLING SPOTIFY$CRESET"
	# 1. Add the Spotify repository signing keys to be able to verify downloaded packages
	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0DF731E45CE24F27EEEB1450EFDC8610341D9410
	# 2. Add the Spotify repository
	echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list
	# 3. Update list of available packages
	sudo apt-get update
	# 4. Install Spotify
	sudo apt-get install spotify-client
}

main() {
	update_system
	create_vimrc
	install_java
	install_spotify
}

main
