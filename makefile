install:
	pip3 install termcolor requests
	echo "Installing scripts..."
	cp ./myip.py /usr/bin/myip
	chmod +x /usr/bin/myip
	cp ./anonbash.py /usr/bin/xbash
	chmod +x /usr/bin/xbash
	echo "Installation Complete"
