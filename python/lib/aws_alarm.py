#!/usr/bin/python
# -*- coding:utf8 -*

"""
    AWS library

    This module is a collection of functions to handle AWS alarms to manage a CI/CD pipeline.

"""

import boto3
import json
import os

ec2_client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
cloudwatch = boto3.client('cloudwatch')

def dump_alarm(alarm):
    """ pretty print an alarm """
    json_string = json.dumps(alarm, indent=2, default=str)
    print(json_string)
    print()

def alarm_list (verbose = False, filter = ""):
    """ return a list of alarms """
    
    response = cloudwatch.describe_alarms()

    result = []
    for alarm in response['MetricAlarms']:
        s = ''
        strg = alarm['AlarmName'] + alarm['AlarmDescription'] + s.join(alarm['AlarmActions'])

        if filter:
            if filter in strg:
                result.append(alarm)
                if verbose:
                    dump_alarm(alarm)
        else:
            result.append(alarm)
            if verbose:
                dump_alarm(alarm)

    return result
    
def alarm_create(ec2_ids=[]):
    # Create alarm
    # when CPU percentage is inferior to 5 % for more than one hour
    dimentions=[]
    for id in ec2_ids:
        dimentions.append(
            {
                'Name': 'InstanceId',
                'Value': id
            }
        )
    alarm_actions = ["arn:aws:automate:eu-west-3:ec2:stop"]
    cloudwatch.put_metric_alarm(
        AlarmName='Unused instance',
        ComparisonOperator='LessThanOrEqualToThreshold',
        AlarmActions = alarm_actions,
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Period=3600,
        Statistic='Average',
        Threshold=2.0,
        ActionsEnabled=False,
        AlarmDescription='Alarm when CPU is below 2%',
        Dimensions=dimentions,
        Unit='Seconds'
    )

def alarm_delete():
    # Delete alarm
    cloudwatch.delete_alarms(
        AlarmNames=['Unused instance'],
    )