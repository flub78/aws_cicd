# Ansible

## Tutorials

[ANSIBLE - Tutos & Formation : automatiser vos configurations
(xavki)](https://www.youtube.com/playlist?list=PLn6POgpklwWoCpLKOSw3mXCqbRocnhrh-)

[Latest Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html)

https://github.com/geerlingguy/ansible-role-jenkins/blob/master/tasks/plugins.yml

[Ansible modules](https://docs.ansible.com/ansible/latest/collections/community/general/index.html#plugin-index)

## Ansible installation

    sudo apt-get update
    # There is no mysql_user: with ansible-core...
    # sudo apt install ansible-core
    # The ansible package includes the Ansible language and runtime plus a range of community curated Collections
    # Some of these collections are used in this project.
    sudo apt install ansible
    ansible --version
    ansible [core 2.12.0]
        config file = None
        configured module search path = ['/home/frederic/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
        ansible python module location = /usr/lib/python3/dist-packages/ansible
        ansible collection location = /home/frederic/.ansible/collections:/usr/share/ansible/collections
        executable location = /usr/bin/ansible
        python version = 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0]
        jinja version = 3.0.3
        libyaml = True

## First communication with an EC2 instance

Create the file /etc/ansible/hosts on the control host

and fill it

    cat /etc/ansible/hosts
```
[jenkins]
        ubuntu@flub78.net

ansible all -m ping
ubuntu@flub78.net | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}

ansible-playbook jenkins test_connection.yml
```

## Ansible vault

Some files containing private data are encrypted.

They can be modified that way:

    ansible-vault edit roles/apache/vars/main.yml

The ansible vault password can be store in a file

    ansible-playbook --vault-password-file "~/.ssh/ansible_vault_key" aws_dev_server.yml

## Variable organization

The objective of this project is to provide roles that can be reused to provision infrastructure.

So an infrastructure is defined by a set of variables (environment variables) and once defined the playbooks can be run.



## Ansible Playbooks Description

- test_connection.yml -	test ansible access to a node
- lamp.yml -				install Apache, MySQL and PHP
- jenkins.yml -			install jenkins
- jenkins_jobs_multi -	Create the jobs for the multitenant project
- jenkins_jobs_gvv - Create the jobs for gvv	 

## Ansible roles Description

### check_access

	Check that ansible can access a node and sudo as root

### apache

[How To Install the Apache Web Server on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04#step-5-%E2%80%94-setting-up-virtual-hosts-recommended)

[How To Install Linux, Apache, MySQL, PHP (LAMP) Stack on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-22-04)

- Install the Apache web server
- Create a virtual host for a domain

### https

[How To Secure Apache with Let's Encrypt on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04)

- Create a lets-encrypt certificate
- Create an https virtual host

### mysql

- Install a database server

### php

- Install php (currently 8.1 but I'll need to have it configurable)

### phpmyadmin

    https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-22-04

    https://www.hostinger.com/tutorials/how-to-install-and-setup-phpmyadmin-on-ubuntu

    https://tecadmin.net/switch-between-multiple-php-version-on-debian/

For an unknown reason the installation of phpmyadmin force the installation of some php 8.2 modules for CLI.

```sh
update-alternatives --list
update-alternatives --set php /usr/bin/php8.1

php -version
PHP 8.1.16 (cli) (built: Feb 14 2023 18:35:37) (NTS)
```

### jdk
- Java JDK

### jenkins
- Jenkins

### phptools
- The PHP static analyzer tools

### jenkins_jobs_xxx

- The jenkins jobs for the project project xxx 

### Detailed description of some roles

  - [https role](https_role.md)
  - [mysql role](mysql_role.md)

## [Testing Ansible roles](Testing_roles.md)