import logging
import boto3
import json
import os
from botocore.vendored import requests

# Initialize logger and set log level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

session = boto3.Session(
    region_name="us-west-2"
)
sns_client = session.client('sns')
sqs_client = boto3.client('sqs')
sqs = boto3.resource('sqs')
queue_url = 'https://sqs.us-west-2.amazonaws.com/457946912569/fb_app'

queue = sqs.Queue(queue_url)

def lambda_handler(event, context):

    # TODO implement

    logger.info('fuck monish')
    a=json.loads(event['Records'][0]['body'])
    b=a['data']
    logger.info('b4 monish ')
    logger.info(a)
    logger.info('after monish')
    logger.info(b)
    texta=' '
    for messages in b:
        if 'message' in messages.keys():
            logger.info('in loop ')
            logger.info(messages)
            texta=texta + ' . '+messages['message']


    # for record in event['Records']:
    #     # print(record['body'])
    #     logger.info('fuck monish',record['data'])
    # for data in record['body']['data']:
    #     pass






    # response = sns_client.publish(
    # PhoneNumber='+19295309076',
    # Message='fucku v v much monish',
    # MessageAttributes={
    #     'AWS.SNS.SMS.SenderID': {
    #         'DataType': 'String',
    #         'StringValue': 'SENDERID'
    #     },
    #     'AWS.SNS.SMS.SMSType': {
    #         'DataType': 'String',
    #         'StringValue': 'Promotional'
    #     }
    # }
    # )

    #Sending notification about new post to SNS
    client = boto3.client('sns')
    client.publish(
        TopicArn = 'arn:aws:sns:us-west-2:457946912569:SNS_TOPIC',
        Message = texta
    )
    logger.info('fucked up gada is here')

    return
    # entries = [{'Id': msg['MessageId'], 'ReceiptHandle': msg['ReceiptHandle']} for msg in resp['Messages']]
    # resp_del = sqs_client.delete_message_batch(QueueUrl=queue_url, Entries=entries)
    # print ((resp['Messages']))
    # logger.info ((resp['Messages']))
    # return (resp['Messages'])
