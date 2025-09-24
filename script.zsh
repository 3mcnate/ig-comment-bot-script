#!/bin/zsh

python_check=$(which python3)
if [[ $python_check =~ "not found" ]]; then
	echo "You need to install Python first."
	echo "Mac download: https://www.python.org/ftp/python/3.13.7/python-3.13.7-macos11.pkg"
	exit
fi

pip3 install curlconverter

