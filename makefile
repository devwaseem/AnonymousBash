install:
	pip3 install termcolor requests
	echo "Installing scripts..."
	cp ./myip.py /usr/bin/myip
	chmod +x /usr/bin/myip
	cp ./securebash.py /usr/bin/sbash
	chmod +x /usr/bin/sbash
	echo "Installation Complete"
