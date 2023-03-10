# PHP multiple versions

Not sure that it is better to deploy several VMs or to install the same version of php. 

Here are some notes on the subject.

## Current defaults is 8.1.16

```sh
php -version
PHP 8.1.16 (cli) (built: Feb 14 2023 18:35:37) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.16, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.16, Copyright (c), by Zend Technologies
```

    https://ratus.flub78.net/info.php

PHP 8.2 is also installed 

```sh
ls -l php*
lrwxrwxrwx 1 root root      21 Feb 27 13:26 php -> /etc/alternatives/php
-rwxr-xr-x 1 root root 5568008 Feb 14 18:35 php8.1
-rwxr-xr-x 1 root root 5674792 Feb 14 16:58 php8.2
lrwxrwxrwx 1 root root      24 Feb 28 12:52 phpdbg -> /etc/alternatives/phpdbg
-rwxr-xr-x 1 root root 5732304 Feb 14 16:58 phpdbg8.2
```


CLI default version can be swapped with

    $ sudo update-alternatives --set php /usr/bin/php5.6

## Installing multiple versions

https://devanswers.co/run-multiple-php-versions-on-apache/

## Previous notes

https://www.tecmint.com/install-different-php-versions-in-ubuntu/

```
	    sudo apt install php7.2-mbstring php7.2-gettext php7.2-mysql php7.2-common php7.2-cli php7.2-bcmath php7.2-bz2
        sudo apt install php7.2-curl php7.2-gd php7.2-intl php7.2-json php7.2-readline
        sudo apt install php7.2-xml php7.2-zip php7.2-fpm
		
	sudo update-alternatives --set php /usr/bin/php7.2
	sudo a2dismod php7.3
	a2enmod proxy_fcgi setenvif
	a2enconf php7.2-fpm
	sudo a2enmod php7.2
	
	NOTICE: Not enabling PHP 7.2 FPM by default.
NOTICE: To enable PHP 7.2 FPM in Apache2 do:
NOTICE: a2enmod proxy_fcgi setenvif
NOTICE: a2enconf php7.2-fpm
NOTICE: You are seeing this message because you have apache2 package installed.

	sudo update-alternatives --set php /usr/bin/php7.3

	  392  sudo apt show php
  393  php --version
  394  ls /usr/bin/php*
  395  /usr/bin/php --version
  396  sudo apt show php -a
  397  sudo apt install python-software-properties
  398  sudo add-apt-repository ppa:ondrej/php
  399  sudo add-apt-repository ppa:ondrej/php
  400  sudo apt-get update
  401  sudo apt install php7.2
  402  php -v
  403  sudo apt install php7.2-mbstring php7.2-gettext php7.2-mysql php7.2-commo                                                                                                                                                             n php7.2-cli php7.2-bcmath php7.2-bz2
  404  sudo apt install php7.2-curl php7.2-gd php7.2-intl php7.2-json php7.2-rea                                                                                                                                                             dline
  405  sudo apt install php7.2-xml php7.2-zip php7.2-fpm
  406  sudo update-alternatives --set php /usr/bin/php7.2
  407  php --version
  408  sudo a2dismod php7.3
  409  sudo a2enmod php7.2
  410  history
  411  a2enmod proxy_fcgi setenvif
  412  a2enconf php7.2-fpm
  413  sudo a2enconf php7.2-fpm

```