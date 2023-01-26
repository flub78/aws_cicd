#!/usr/bin/python
# -*- coding:utf8 -*

"""
Python script to manage AWS elastic IPs

The scripts are able to list, create and delete the resources.
"""
import argparse
import os
import boto3
import json


description="AWS elastic IPs management"
resource='elastic_ip'
basename = os.environ.get('BASENAME')

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

keyname = 'ec2-keypair'
if basename:
    keyname = basename + '_' + keyname

# Parsing of the CLI arguments
parser = argparse.ArgumentParser(description=description)

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help='list the ' + resource)
group.add_argument('-c', '--create', action='store_true', help='create a ' + resource)
group.add_argument('-d', '--delete', action='store_true', help='delete a ' + resource)
group.add_argument('-s', '--stop', action='store_true', help='stop an ' + resource)
group.add_argument('-r', '--resume', action='store_true', help='restart an ' + resource)

parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
# parser.add_argument('--int', type=int, help='an integer value')
# parser.add_argument('--float', type=float, help='a float value')
parser.add_argument('-i', '--instance', type=str, help='EC2 instance ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + resource + ' to create')
parser.add_argument('-f', '--filter', type=str, help='process only the matching strings')
parser.add_argument('-k', '--keypair', type=str, help='keypair to use')

# parser.add_argument('--bool', type=bool, help='a boolean value')

args = parser.parse_args()

###################################################
def list():
    """ list all the resources """
    if args.verbose:
        print ('list the ' + resource)
    response = ec2_client.describe_addresses()

    for ip in response['Addresses']:
        json_string = json.dumps(ip, indent=2, default=str)
        print(json_string)
        print()

def create():
    """ create a resource """
   
    if args.verbose:
        print ('creating ' + resource + ' ' + keyname)

 
    # call the boto ec2 function to create a key pair
    key_pair = ec2.create_key_pair(KeyName=keyname)


def delete():
    """ delete a resource """
    if args.verbose:
        print ('delete ' + resource, keyname)
    response = ec2_client.delete_key_pair(KeyName=keyname)
    # print(response)

###################################################
# Main processing

# print('args = ')
# print (args)

if args.list:
    list()    

if args.create:
    create()

if args.delete:
    delete()

if args.instance:
    print ('instance = ' + args.instance)