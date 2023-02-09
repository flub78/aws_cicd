#!/usr/bin/python
# -*- coding:utf8 -*

"""
AWS security groups management.

The scripts are able to list, create and delete security groups.
"""
import argparse
from lib.aws import *
from lib.aws_sg import *

description="AWS security groups management"
resource='security_group'

# Parsing of the CLI arguments
parser = argparse.ArgumentParser(description=description)

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help='list the ' + resource)
group.add_argument('-c', '--create', action='store_true', help='create a ' + resource)
group.add_argument('-d', '--delete', action='store_true', help='delete a ' + resource)

parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
parser.add_argument('-i', '--id', type=str, help='Key pair ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + resource + ' to create')
parser.add_argument('-f', '--filter', type=str, help='process only the matching strings')

args = parser.parse_args()

###################################################
def list():
    """ list all the resources """    
    list = security_group_list(args.verbose, args.filter)
    return
    for security_group in list:
        print(security_group['KeyName'], security_group['KeyPairId'], security_group['KeyType'])

def create():
    """ create a resource """
    security_group_create(name=args.name, verbose=args.verbose)

def delete():
    ids = security_group_select_ids(verbose=args.verbose, name=args.name, id=args.id, filter=args.filter)
    security_group_delete(ids, args.verbose)

###################################################
# Main processing

if args.list:
    list()    

if args.create:
    create()

if args.delete:
    delete()
