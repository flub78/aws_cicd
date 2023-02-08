#!/usr/bin/python
# -*- coding:utf8 -*

"""
    AWS library

    This module is a collection of functions to handle AWS key pairs to manage a CI/CD pipeline.

"""

import boto3
import json
import os

ec2_client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

def key_pair_list(verbose = False, filter = ""):
    """ return a list of key pairs """
    response = ec2_client.describe_key_pairs()
    if (verbose):
        print("Key pair list")
        print_json(response)

    if (filter):
        list = []
        for key in response['KeyPairs']:
            str = key['KeyName'] + key['KeyPairId'] +  key['KeyType']
            if filter in str:
                list.append(key)
        return list
    
    else:
        return response['KeyPairs']


def key_pair_select_ids(verbose = False, name="", id="", filter=""):
    """ 
        return a list of ids
    """
    response = ec2_client.describe_key_pairs()
 
    list = []   

    for key in response['KeyPairs']:
        str = key['KeyName'] + key['KeyPairId'] +  key['KeyType']

        if (name and (name == key['KeyName'])):
            if (not key in list):
                if (not filter or (filter in str)):
                    list.append(key)
        elif (id and (id == key['KeyPairId'])):
            if (not key in list):
                if (not filter or (filter in str)):
                    list.append(key)
        else:
            if (filter):
                if ((filter in str) and (not key in list)):
                    list.append(key)
    return list


def key_pair_create(name="", verbose=False):
    """ Create a key pair """
    if verbose:
        print ('creating key pair name=' + name)

    if (not name):
        basename = os.environ.get('BASENAME')
        name = basename + '_' + 'ec2-keypair'
    filename = name + '.pem'

    # create a file to store the key locally
    outfile = open(filename,'w')

    # call the boto ec2 function to create a key pair
    key_pair = ec2.create_key_pair(KeyName=name)

    # capture the key and store it in a file
    KeyPairOut = str(key_pair.key_material)
    if verbose:
        print(KeyPairOut)
    outfile.write(KeyPairOut)   


def key_pair_delete(ids = [], verbose=False):
    """ Delete a list of key pairs from ids """
    for id in ids:
        if (verbose):
            print ('deleting key pair id=' + id['KeyPairId'])
        response = ec2_client.delete_key_pair(KeyPairId=id['KeyPairId'])
        filename = id['KeyName'] + '.pem'
        os.remove(filename) 
