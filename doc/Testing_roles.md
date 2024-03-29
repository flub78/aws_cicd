# Ansible roles test plan

Minimal smoke test plan for the pipeline deployment.

## Test ssh access to a node

To test that an instance has been created use the command from the output.

    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ec2-35-180-72-146.eu-west-3.compute.amazonaws.com
    

## Test the basic web server

For testing a minimal web server is installed on port 8888

http://ec2-35-180-72-146.eu-west-3.compute.amazonaws.com:8888/

## Testing DNS

Once that the DNS table have been updated it is possible to use the full domain name.

    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ratus.flub78.net

    http://ratus.flub78.net:8888


## Testing basic ansible access

    ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/test_connection.yml

## Testing Apache

    http://ratus.flub78.net
    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ratus.flub78.net
        sudo service apache2 status
        grep ratus /var/www/ratus.flub78.net/index.html
        ls /etc/apache2/sites-enabled/

## Testing https

    https://ratus.flub78.net

    https://ratus.flub78.net/info.php

## Testing MySql

```
sudo service mysql status

mysql -u root -p
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)
``` 

## Testing PHP
```
php --version
PHP 8.1.16 (cli) (built: Feb 14 2023 18:35:37) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.16, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.16, Copyright (c), by Zend Technologies
```

    http://ratus.flub78.net/index.php

## Testing phpmyadmin

    https://ratus.flub78.net/phpmyadmin/

    root + password

## Testing JDK installation

    java -version

## Testing jenkins

    sudo service jenkins status

    http://ratus.flub78.net:8080/

## PHP tools

```
phing -version
PHP Deprecated:  Creation of dynamic property Phing::$searchForThis is deprecated in phar:///usr/local/bin/phing/classes/phing/Phing.php on line 362
Phing 2.17.4

phploc --version
phploc 7.0.2 by Sebastian Bergmann.
```


