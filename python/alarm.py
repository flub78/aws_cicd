#!/usr/bin/python
# -*- coding:utf8 -*

"""
AWS alarms management.

The scripts are able to list, create and delete the resources.
"""
import argparse
import os
import boto3
import json

from lib.aws import *
from lib.aws_alarm import *

description="aws alarms"
resource='alarm'
basename = os.environ.get('BASENAME')

ec2 = boto3.resource('ec2')

# Parsing of the CLI arguments
parser = argparse.ArgumentParser(description=description)

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help='list the ' + resource)
group.add_argument('-c', '--create', action='store_true', help='create a ' + resource)
group.add_argument('-d', '--delete', action='store_true', help='delete a ' + resource)
group.add_argument('-s', '--stop', action='store_true', help='stop an ' + resource)
group.add_argument('-r', '--resume', action='store_true', help='restart an ' + resource)

parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
parser.add_argument('-i', '--instance', type=str, help='EC2 instance ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + resource + ' to create')
parser.add_argument('-f', '--filter', type=str, help='process only the matching strings')
parser.add_argument('-k', '--keypair', type=str, help='keypair to use')
args = parser.parse_args()

###################################################
def list():
    """ list all the resources """
    list = alarm_list(args.verbose, args.filter)
    for alarm in list:
        s = ', '
        ec2_list = []
        for dim in  alarm['Dimensions']:
            ec2_list.append(dim['Value'])
        print(alarm['AlarmName'], alarm['AlarmDescription'], s.join(alarm['AlarmActions']), s.join(ec2_list) )

def create():
    """ create a resource """
   
    if args.verbose:
        print ('creating ' + resource)
    if (not args.instance):
        print("instance arguments is mandatory to create an alarm")
        exit()

    alarm_create([args.instance])

def delete():
    """ delete a resource """
    if args.verbose:
        print ('deleting ' + resource)
    alarm_delete()

###################################################
# Main processing

if args.list:
    list()    

if args.create:
    create()

if args.delete:
    delete()