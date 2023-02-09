#!/usr/bin/python
# -*- coding:utf8 -*

"""
    AWS library

    This module is a collection of functions to handle AWS security groups.
"""

import boto3
import json
import os
from lib.aws import *

ec2_client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

def security_group_list(verbose = False, filter = ""):
    """ return a list of security groupss """
    response = ec2_client.describe_security_groups()
    if (verbose):
        print("security groups list")
        print_json(response)

    if (filter):
        list = []
        for key in response['KeyPairs']:
            str = key['KeyName'] + key['KeyPairId'] +  key['KeyType']
            if filter in str:
                list.append(key)
        return list
    
    else:
        return response['SecurityGroups']


def security_group_select_ids(verbose = False, name="", id="", filter=""):
    """ 
        return a list of ids
    """
    response = ec2_client.describe_security_groups()
 
    list = []   

    for sg in response['SecurityGroups']:
        str = sg['GroupName'] + sg['GroupId'] +  sg['Description']

        if (name and (name == sg['GroupName'])):
            if (not sg in list):
                if (not filter or (filter in str)):
                    list.append(sg)
        elif (id and (id == sg['GroupId'])):
            if (not sg in list):
                if (not filter or (filter in str)):
                    list.append(sg)
        else:
            if (filter):
                if ((filter in str) and (not sg in list)):
                    list.append(sg)
    return list


def security_group_create(name="", verbose=False):
    """ Create a security groups """
    if verbose:
        print ('creating security groups name=' + name)

    if (not name):
        basename = os.environ.get('BASENAME')
        name = basename + '_' + 'ec2-keypair'
    filename = name + '.pem'

    # create a file to store the key locally
    outfile = open(filename,'w')

    # call the boto ec2 function to create a security groups
    security_group = ec2.create_security_group(KeyName=name)

    # capture the key and store it in a file
    KeyPairOut = str(security_group.key_material)
    if verbose:
        print(KeyPairOut)
    outfile.write(KeyPairOut)   


def security_group_delete(ids = [], verbose=False):
    """ Delete a list of security groupss from ids """
    for id in ids:
        if (verbose):
            print ('deleting security groups id=' + id['KeyPairId'])
        response = ec2_client.delete_security_group(KeyPairId=id['KeyPairId'])
        filename = id['KeyName'] + '.pem'
        os.remove(filename) 
