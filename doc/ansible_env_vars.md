# Ansible environment variables

Here is the list of environment variables which are used in the ansible roles. They are typically managed in a setenv file and kept in private source code management repository.

## Global variables

* $ANSIBLE_HOST ansible host to apply the playbook
* $INVENTORY name of the ansible inventory
* $PRIVATE_KEY name of the RSA private key file
* $PLAYBOOK directory where playbooks are stores

## Roles and playbook variables

* $DOMAIN   domain of the server to provision, subdomain names may be derived from the domain.
