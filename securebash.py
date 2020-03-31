#!/bin/env python3
from urllib.request import urlopen
import sys
import os,subprocess
from termcolor import colored

err = colored("[!] ","red")
succ = colored("[+] ","green")
runn = colored("[*] ","blue")
warn = colored("[?]","yellow")

def internet_on():
	try:
		urlopen('https://google.com',timeout=3)
		return True
	except:
		return False
		
def tor_on():
	torstatus = subprocess.getoutput('systemctl is-active tor')
	return torstatus == 'active'

if not internet_on():
	print(err+"Internet not connected...")
	sys.exit(1)
print(colored(succ+"Internet Connected...","green"))
if not tor_on():
	print(err+"TOR STATUS: "+colored("INACTIVE","red"))
	print(runn+"Starting tor...")
	status = subprocess.getoutput("systemctl start tor ;echo $?")
	if status == "0":
		print(succ+"Tor Started...")
	else:
		print(err+"Problem starting tor...")
		print(warn+"Check tor using: systemctl status tor")
		sys.exit(1)
print(succ+"TOR STATUS: "+colored("ACTIVE","green"))
print(runn+"tunneling Tor to Bash...")
os.system("proxychains -q bash ")	
print(runn+"Stopping TOR")
status = subprocess.getoutput("systemctl stop tor; echo $?")
if status == "0":
	print(succ+"TOR stopped")
else:
	print(err+"Error Stopping TOR")
	print(warn+"You can stop TOR using: systemctl stop tor")
	

