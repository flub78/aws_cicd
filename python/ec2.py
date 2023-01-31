#!/usr/bin/python3
# -*- coding:utf8 -*

"""
AWS EC2 instances management.

The scripts are able to list, create and delete EC2 instances.
"""
import argparse
import os
from lib.aws_ec2 import *

# Initialization
# --------------
description="aws EC2 instances management"
resource='ec2_instance'

# Parsing of the CLI arguments
# ----------------------------
parser = argparse.ArgumentParser(description=description)

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help='list the ' + resource)
group.add_argument('-c', '--create', action='store_true', help='create an ' + resource)
group.add_argument('-d', '--delete', action='store_true', help='delete an ' + resource)
group.add_argument('-s', '--stop', action='store_true', help='stop an ' + resource)
group.add_argument('-r', '--resume', action='store_true', help='restart an ' + resource)

parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')

parser.add_argument('-i', '--id', type=str, help='EC2 instance ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + resource + ' to create')
parser.add_argument('-f', '--filter', type=str, help='process only the matching strings')
parser.add_argument('-k', '--keypair', type=str, help='keypair to use')
parser.add_argument('-t', '--type', type=str, help='instance type')
parser.add_argument('-a', '--ami', type=str, help='image')

args = parser.parse_args()

###################################################
# Main processing
ids = ec2_select_ids(verbose=args.verbose, name=args.name, id=args.id, filter=args.filter)

if args.list:
     ec2_print_list(ids, args.verbose)

if args.create:
    ec2_create(name=args.name, keyname=args.keypair, verbose=args.verbose)

if args.delete:
    ec2_delete(ids, args.verbose)

if args.resume:
    ec2_resume(ids, args.verbose)

if args.stop:
    ec2_stop(ids, args.verbose)