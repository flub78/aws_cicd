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
