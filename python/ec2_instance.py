#!/usr/bin/python
# -*- coding:utf8 -*

"""
AWS EC2 instances management.

The scripts are able to list, create and delete EC2 instances.
"""
import argparse
import os
import boto3

description="aws EC2 instances management"
resource='ec2_instance'
basename = os.environ.get('BASENAME')

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

amazon_linux_2="ami-0cc814d99c59f3789"
jenkins_7="ami-0e019d7e4645e931d"
ami=amazon_linux_2

keyname = 'ec2-keypair'
if basename:
    keyname = basename + '_' + keyname

# Parsing of the CLI arguments
parser = argparse.ArgumentParser(description=description)

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', action='store_true', help='list the ' + resource)
group.add_argument('-c', '--create', action='store_true', help='create a ' + resource)
group.add_argument('-d', '--delete', action='store_true', help='delete a ' + resource)

parser.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
parser.add_argument('--int', type=int, help='an integer value')
parser.add_argument('--float', type=float, help='a float value')
parser.add_argument('-i', '--instance', type=str, help='EC2 instance ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + resource + ' to create')
parser.add_argument('--bool', type=bool, help='a boolean value')

args = parser.parse_args()

###################################################
def list():
    """ list all the resources """
    if args.verbose:
        print ('list the ' + resource)
    response = ec2_client.describe_instances()
    # print(response)

    # Iterate through each instance and print its ID
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'], instance['ImageId'], instance['InstanceType'],
                instance['State']['Name'],
                instance['Placement']['AvailabilityZone'], 
                instance['PublicDnsName'])

def create():
    """ create a resource """
   
    if args.verbose:
        print ('creating ' + resource)

    # create a new EC2 instance
    instances = ec2.create_instances(
        ImageId=ami,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=keyname
    )

def delete():
    """ delete a resource """
    if not args.instance:
        print ("instance ID is required")
        exit

    if args.verbose:
        print ('deleting ' + resource, args.instance)

    ec2.instances.filter(InstanceIds = args.instance).terminate()
    # ec2.stop_instances(InstanceIds=args.instance)
    # ec2.start_instances(InstanceIds=args.instance)
    

###################################################
# Main processing

if args.list:
    list()    

if args.create:
    create()

if args.delete:
    delete()

if args.instance:
    print ('instance = ' + args.instance)