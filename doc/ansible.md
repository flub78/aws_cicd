# Ansible

## Ansible installation

    sudo apt-get update
    sudo apt install ansible-core

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

create the file /etc/ansible/hosts on the control host

and fill it
cat /etc/ansible/hosts
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
