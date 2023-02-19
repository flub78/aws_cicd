# Ansible roles test plan

## Test ssh access

To test that an instance has been created use the command from the output.

    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ec2-35-180-72-146.eu-west-3.compute.amazonaws.com
    

## Test the basic web server

For testing a minimal web server is installed on port 8080

http://ec2-35-180-72-146.eu-west-3.compute.amazonaws.com:8080/

## Testing DNS

Once that the DNS table have been updated it is possible to use the full domain name.

    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ratus.flub78.net

    http://ratus.flub78.net:8080


## Testing basic ansible access

    ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/test_connection.yml

## Test Apache

    http://ratus.flub78.net
    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ratus.flub78.net
        sudo service apache2 status
        grep ratus /var/www/ratus.flub78.net/index.html
        ls /etc/apache2/sites-enabled/

## Test https



## Test MySql

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

## Test PHP
```
php --version
PHP 8.1.16 (cli) (built: Feb 14 2023 18:35:37) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.16, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.16, Copyright (c), by Zend Technologies
```

    http://ratus.flub78.net/index.php

## Test phpmyadmin