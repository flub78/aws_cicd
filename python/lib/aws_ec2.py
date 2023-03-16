#!/usr/bin/python
# -*- coding:utf8 -*

"""
    AWS library

    This module is a collection of functions to handle AWS objects to manage a CI/CD pipeline.

"""

import boto3
import json
import os

ec2_client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

def ec2_select_ids(verbose = False, name="", id="", filter=""):
    """ 
        return a list of instances
    """
    response = ec2_client.describe_instances()

    if verbose:
        print("EC2 instances")
    list = []   
    ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:

            str = ''
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if (tag['Key'] == 'Name'):
                        instancename = tag['Value']

            str = instancename + ' '
            str += instance['InstanceId'] + ' '
            str += instance['ImageId'] + ' '
            str += instance['InstanceType'] + ' '
            str += instance['State']['Name'] + ' '
            if 'KeyName' in instance: str += instance['KeyName'] + ' '
            str += instance['Placement']['AvailabilityZone'] + ' '
            str += instance['PublicDnsName'] + ' '

            if (name and (name == instancename)):
                if (not instance['InstanceId'] in ids):
                    if (not filter or (filter in str)):
                        list.append(instance)
                        ids.append(instance['InstanceId'])

            elif (id and (id == instance['InstanceId'])):
                if (not instance['InstanceId'] in ids):
                    if (not filter or (filter in str)):
                        list.append(instance)
                        ids.append(instance['InstanceId'])
            else:
                if (filter):
                    if ((filter in str) and (not instance['InstanceId'] in ids)):
                        list.append(instance)
                        ids.append(instance['InstanceId'])
                elif (not name and not id):
                    list.append(instance)
                    ids.append(instance['InstanceId'])
    return list


def ec2_create(name="", verbose=False, keyname=""):
    """ Create an EC2 instance """

    amazon_linux_2="ami-0cc814d99c59f3789"
    jenkins_7="ami-0e019d7e4645e931d"
    ubuntu="ami-0afd55c0c8a52973a"
    ami=ubuntu

    instancetype='t2.micro'
    sg='sg-0b864f5c5c2ceb714'

    if verbose:
        print ('creating an EC2 instance')

    if (not name):
        basename = os.environ.get('BASENAME')
        name = basename + '_ec2-i' if (basename) else 'ec2-i'

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
                    'Value': name
                },
            ]
        }]
    )

def ec2_delete(list = [], verbose=False):
    """ Delete a list of EC2 instances """
    for instance in list:
        id=instance['InstanceId']
        if (verbose):
            print ('deleting EC2 id=' + id)
        ec2.instances.filter(InstanceIds = [id]).terminate()

def ec2_print_list(list, verbose=False):
    """ Print a list of EC2 instances """
    for instance in list:
        name = ""
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if (tag['Key'] == 'Name'):
                        name = tag['Value']
        
        print(name)
        print("\t" + instance['ImageId'])
        print("\t" + instance['InstanceType'])
        print("\t" + instance['KeyName'] if 'KeyName' in instance else "") 
        print("\t" + instance['State']['Name'])
        print("\t" + instance['Placement']['AvailabilityZone'])
        print("\t" + instance['PublicDnsName'])


def ec2_stop(list, verbose=False):
    """ Stop EC2 instances """
    for instance in list:
        id=instance['InstanceId']
        if (verbose):
            print ('stopping EC2 id=' + id)
        ec2_client.stop_instances(InstanceIds=[id])

def ec2_resume(list, verbose=False):
    """ Resume EC2 instances """
    for instance in list:
        id=instance['InstanceId']
        if (verbose):
            print ('resuming EC2 id=' + id)
        ec2_client.start_instances(InstanceIds=[id])
