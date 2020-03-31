# AnonymousBash

#### Anonymous Bash Environment powered with TOR and Proxychains

| :warning:     | I AM NOT RESPONSIBLE FOR HOW YOU USE THIS SCRIPT. USE LEGALLY. DONT BE AN IMBECILE.  |
|---------------|:-------------------------------------------------------------------------------------|


This script automates the process of tor and proxychains and tunnels it to Bash Environment so you can run any aggressive commands anonymously

If you don't know what proxychains and Tor is, You may not know how to config those. Please Google it

## :computer: Supported OS
```
Arch linux (systemctl)
```
This script is made and tested in Arch Linux
If you want to port and test it in your Linux distro, you are more than welcome.
Please contact me: waseem07799@gmail.com


## :scroll: Requirements
- Python 3
- Proxychains
- Tor

## :wrench: Installation
```
$ git clone https://github.com/devwaseem/AnonymousBash.git
$ cd AnonymousBash/
$ sudo make install
```
You'll be prompted for password, if you are non-root user. if your user account can't execute with root permissions, check sudoers file

## How to run

just type 
```
$ xbash
```
You'll be prompted for password, if you are non-root user. if your user account can't execute with root permissions, check sudoers file


Once you are inside the shell, run
```
myip
```
myip script will fetch your gelocation using your ip

:pray: Thanks to [@thehowl](https://github.com/thehowl) for [ipinfo clone](https://github.com/thehowl/ip.zxq.co)

## LICENSE


