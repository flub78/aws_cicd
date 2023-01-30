#!/usr/bin/python
# -*- coding:utf8 -*

"""
    AWS library

    This module is a collection of functions to handle AWS objects to manage a CI/CD pipeline.

"""

import boto3
import json

ec2_client = boto3.client('ec2')

def to_json(result):
    """ Format a result from boto3 """
    return json.dumps(result, indent=2, default=str)

def print_json(result):
    """ Pretty print a result from boto3 """
    print(to_json(result))

def key_pair_list(verbose = False, filter = ""):
    """ return a list of key pairs"""
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