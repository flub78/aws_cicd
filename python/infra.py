#!/usr/bin/python3
# -*- coding:utf8 -*

"""
AWS infrastructure management

This script handles a formal description of the infrastructure and is able to
list, create and delete AWS items in this infrastructure.

The list 
"""
import argparse
import os
from lib.aws import *
from lib.aws_ec2 import *
from lib.aws_infra import *
###################################################
# Infrasturcture definition
###################################################

"""
In infrastructure is made of a set of EC2 instances plus all the resources to access them in ssh. 
"""

domain = "flub78.net"
region = "eu-west-3"
amazon_linux_2="ami-0cc814d99c59f3789" # Amazon Linux 2
jenkins_7="ami-0e019d7e4645e931d" # Jenkins 7
ubuntu="ami-0afd55c0c8a52973a" # Ubuntu 18.04 LTS

infra = {
    "name": 'infra',
    "domain": domain,
    "default_sg": 'sg-0b864f5c5c2ceb714',
    "default_key_pair": 'ratus_ec2-keypair',
    "region": region,
    "key_pairs": [
        {
            "name": "ratus_ec2-keypair",
            "file": "ratus_ec2-keypair.pem"
        }
    ],
    "ec2s": [
        {
            "name": "ratus_ec2-i",
            "domain": domain,
            "type": "t2.medium",
            "ami": ubuntu,
            "elastic_ip": "",
            "key_pair": "ratus_ec2-keypair",
            "security_group": "sg-0b864f5c5c2ceb714"
        },
        {
            "name": "test",
            "domain": "test." + domain,
            "type": "t2.nano",
            "ami": ubuntu,
            "elastic_ip": ""
        }
    ]
}
    
# Initialization
# --------------
description="aws infrastructure management"

# Parsing of the CLI arguments
# ----------------------------
parser = argparse.ArgumentParser(description=description)

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help='list the items of the infrastructure')
group.add_argument('-c', '--create', action='store_true', help='create missing nodes and resources ')
group.add_argument('-d', '--delete', action='store_true', help='delete all resources associated with the infrastructure')
group.add_argument('-s', '--stop', action='store_true', help='stop all instances of the infrastructure')
group.add_argument('-r', '--resume', action='store_true', help='restart all instances of the infrastructure')

parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
parser.add_argument('--check', action='store_true', help='Dry run, no action')

parser.add_argument('-i', '--id', type=str, help='EC2 instance ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + ' to create')
parser.add_argument('-f', '--filter', type=str, help='process only the matching strings')
# parser.add_argument('-k', '--keypair', type=str, help='keypair to use')
# parser.add_argument('-t', '--type', type=str, help='instance type')
# parser.add_argument('-a', '--ami', type=str, help='image')

args = parser.parse_args()

###################################################
# Main processing
ids = ec2_select_ids(verbose=args.verbose, name=args.name, id=args.id, filter=args.filter)

if args.create:
    ec2_create(name=args.name, keyname=args.keypair, verbose=args.verbose)
    ids = ec2_select_ids(verbose=args.verbose, name=args.name, id=args.id, filter=args.filter)
    ec2_print_list(ids, args.verbose)


if args.delete:
    ec2_delete(ids, args.verbose)
    ec2_print_list(ids, args.verbose)

if args.resume:
    ec2_resume(ids, args.verbose)
    ec2_print_list(ids, args.verbose)

if args.stop:
    ec2_stop(ids, args.verbose)
    ec2_print_list(ids, args.verbose)

print_infra(infra)
