# AnonymousBash

#### Anonymous Bash Environment powered with TOR and Proxychains
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This script automates the process of tor and proxychains and tunnels it to Bash Environment so you can run any aggressive commands anonymously

If you don't know what proxychains and Tor is, You may not know how to config those. Please Google it

![xbash](https://raw.githubusercontent.com/devwaseem/AnonymousBash/master/xbash.png)
![myip](https://raw.githubusercontent.com/devwaseem/AnonymousBash/master/myip.jpg)

| :warning:     | I AM NOT RESPONSIBLE FOR HOW YOU USE THIS SCRIPT. USE LEGALLY. DONT BE AN IMBECILE.  |
|---------------|:-------------------------------------------------------------------------------------|


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

## :gear: How to run

just type 
```
$ xbash
```
You'll be prompted for password, if you are non-root user. if your user account can't execute with root permissions, check sudoers file

![xbash](https://raw.githubusercontent.com/devwaseem/AnonymousBash/master/xbash.png)


Once you are inside the shell, run
```
$ myip
```
myip command will fetch your gelocation using your ip

![myip](https://raw.githubusercontent.com/devwaseem/AnonymousBash/master/myip.jpg)

:pray: Thanks to [@thehowl](https://github.com/thehowl) for [ipinfo clone](https://github.com/thehowl/ip.zxq.co)

## Contributions
Contributions are always welcome, have an idea or bug fix? please fork and pull request


## :balance_scale: LICENSE
[MIT](https://github.com/devwaseem/AnonymousBash/blob/master/LICENSE)

