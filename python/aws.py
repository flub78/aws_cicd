#!/usr/bin/python
# -*- coding:utf8 -*

"""
This file is a template for AWS python scripts.

The basic scripts handle a simple resource (key pair, EC2 instance, etc.).

The scripts are able to list, create and delete the resources.
"""
import argparse

description="aws python template"
resource='key_pair'

parser = argparse.ArgumentParser(description=description)

parser.add_argument('--list', dest='action', action='store_const',
                    const=list,
                    help='list the ' + resource)

parser.add_argument('--create', dest='action', action='store_const',
                    const=create,
                    help='create a ' + resource)

args = parser.parse_args()

print (description)
print('args = ')
print (args)