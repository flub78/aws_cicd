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

def print_infra(infra):
    """ Print the current infrastructure """
    # print(to_json(infra))
    print("Infrastructure: ")
    print("\tName: " + infra["name"])
    print("\tDomain: " + infra["domain"])
    print("\tDefault security group: " + infra["default_sg"])
    print("\tDefault key pair: " + infra["default_key_pair"])
    print("\tRegion: " + infra["region"])
    print("\tKey pairs: ")
    for key_pair in infra["key_pairs"]: 
        print("\t\tName: " + key_pair["name"])
        print("\t\tFile: " + key_pair["file"])
    print("\tEC2s: ")
    for ec2 in infra["ec2s"]: 
        print("\t\tName: " + ec2["name"])
        print("\t\tDomain: " + ec2["domain"])
        print("\t\tType: " + ec2["type"])
        print("\t\tAMI: " + ec2["ami"])
        print("")