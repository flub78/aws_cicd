#!/usr/bin/python
# -*- coding:utf8 -*

"""
This file is a template for AWS python scripts.

The basic scripts handle a simple resource (key pair, EC2 instance, etc.).

The scripts are able to list, create and delete the resources.
"""
import argparse
from lib.aws import *
from lib.aws_key_pair import *

description="aws python template"
resource='key_pair'

# Parsing of the CLI arguments
parser = argparse.ArgumentParser(description=description)

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help='list the ' + resource)
group.add_argument('-c', '--create', action='store_true', help='create a ' + resource)
group.add_argument('-d', '--delete', action='store_true', help='delete a ' + resource)
group.add_argument('-s', '--stop', action='store_true', help='stop an ' + resource)
group.add_argument('-r', '--resume', action='store_true', help='restart an ' + resource)

# parser.add_argument('--int', type=int, help='an integer value')
# parser.add_argument('--float', type=float, help='a float value')
# parser.add_argument('--bool', type=bool, help='a boolean value')
parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
parser.add_argument('-i', '--id', type=str, help='EC2 instance ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + resource + ' to create')
parser.add_argument('-f', '--filter', type=str, help='process only the matching strings')
parser.add_argument('-k', '--keypair', type=str, help='keypair to use')
parser.add_argument('-t', '--test', action='store_true', help='test mode')


args = parser.parse_args()

###################################################
def list():
    """ list all the resources """
    list = key_pair_list(args.verbose, args.filter)
    for key_pair in list:
        print(key_pair['KeyName'], key_pair['KeyPairId'], key_pair['KeyType'])

def create():
    """ create a resource """
    key_pair_create(name=args.name, verbose=args.verbose)

def delete():
    ids = key_pair_select_ids(verbose=args.verbose, name=args.name, id=args.id, filter=args.filter)
    key_pair_delete(ids, args.verbose)

###################################################
# Main processing

if args.list:
    list()    

if args.create:
    create()

if args.delete:
    delete()
