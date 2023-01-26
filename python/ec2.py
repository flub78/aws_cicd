#!/usr/bin/python3
# -*- coding:utf8 -*

"""
AWS EC2 instances management.

The scripts are able to list, create and delete EC2 instances.
"""
import argparse
import os
import boto3
import json

# Initialization
# --------------
description="aws EC2 instances management"
resource='ec2_instance'
basename = os.environ.get('BASENAME')

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

amazon_linux_2="ami-0cc814d99c59f3789"
jenkins_7="ami-0e019d7e4645e931d"
ubuntu="ami-0afd55c0c8a52973a"
ami=ubuntu

instancetype='t2.micro'
sg='sg-0b864f5c5c2ceb714'

keyname = 'ec2-keypair'
instancename = 'ec2-i'
if basename:
    keyname = basename + '_' + keyname
    instancename = basename + '_' + instancename
instanceid = ""

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
# parser.add_argument('--int', type=int, help='an integer value')
# parser.add_argument('--float', type=float, help='a float value')
parser.add_argument('-i', '--instance', type=str, help='EC2 instance ID')
parser.add_argument('-n', '--name', type=str, help='name of the ' + resource + ' to create')
parser.add_argument('-f', '--filter', type=str, help='process only the matching strings')
parser.add_argument('-k', '--keypair', type=str, help='keypair to use')
parser.add_argument('-t', '--type', type=str, help='instance type')
parser.add_argument('-a', '--ami', type=str, help='image')
# parser.add_argument('--bool', type=bool, help='a boolean value')

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
            # json_string = json.dumps(instance, indent=2, default=str)
            # print(json_string)

            str = ''
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if (tag['Key'] == 'Name'):
                        str = tag['Value'] + ' '

            str += instance['InstanceId'] + ' '
            str += instance['ImageId'] + ' '
            str += instance['InstanceType'] + ' '
            str += instance['State']['Name'] + ' '
            str += instance['Placement']['AvailabilityZone'] + ' '
            str += instance['PublicDnsName'] + ' '
            if (args.filter):
                if args.filter in str:
                    print(str)
            else:
                print(str)

def name_to_id(needle, reverse=False):
    """ look for the id matching a name """
 
    response = ec2_client.describe_instances()
    # print(response)

    # Iterate through each instance and print its ID
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # json_string = json.dumps(instance, indent=2, default=str)
            # print(json_string)

            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if (tag['Key'] == 'Name'):
                        ec2_name = tag['Value']

            ec2_id = instance['InstanceId']

            if reverse and (ec2_id == needle):
                return ec2_name
            
            if (ec2_name == needle):
                return ec2_id
             
    return ""


def create():
    """ create a resource """
   
    if args.verbose:
        print ('creating ' + resource)

    # create a new EC2 instance
    instances = ec2.create_instances(
        ImageId=ami,
        MinCount=1,
        MaxCount=1,
        InstanceType=instancetype,
        KeyName=keyname,
        SecurityGroupIds=[sg],
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instancename
                },
            ]
        }]
    )

def delete():
    """ delete a resource """
    if not args.instance:
        print ("instance ID is required")
        exit

    if args.verbose:
        print ('deleting ' + resource, args.instance)

    ec2.instances.filter(InstanceIds = [args.instance]).terminate()
 

def resume(id):
    """ resume an ec2 instance """

    if not id:
        print ("instance ID is required")
        exit

    if args.verbose:
        print ('resuming ' + resource, id)

    ec2_client.start_instances(InstanceIds=[id])
    
def stop(id):
    """ stop an ec2 instance """

    if not id:
        print ("instance ID is required")
        exit

    if args.verbose:
        print ('stopping ' + resource, id)

    ec2_client.stop_instances(InstanceIds=[id])
###################################################
# Main processing

if args.name:
    instancename = args.name
    instanceid = name_to_id(instancename)
    # print ('name = ' + instancename + ', id = ' + instanceid)

if args.instance:
    instanceid = args.instance
    instancename = name_to_id(instanceid, True)
    # print ('name = ' + instancename + ', id = ' + instanceid)

if args.list:
    list()    

if args.create:
    create()

if args.delete:
    delete()

if args.resume:
    resume(instanceid)
    args.filter = instanceid
    list()

if args.stop:
    stop(instanceid)
    args.filter = instanceid
    list()