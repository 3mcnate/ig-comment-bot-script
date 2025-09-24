#!/bin/zsh

echo "Version 0.2"

python_check=$(which python3)
pip_check=$(which pip3)
if [[ $python_check =~ "not found" || $pip_check =~ "not found" ]]; then
	echo "You need to install Python first."
	echo "Mac download: https://www.python.org/ftp/python/3.13.7/python-3.13.7-macos11.pkg"
	exit
fi

pip3 install pyperclip --disable-pip-version-check -q
curl -s https://raw.githubusercontent.com/3mcnate/ig-comment-bot-script/refs/heads/main/main.py -o ~/comment-bot.py 
python3 ~/comment-bot.py < /dev/tty
