# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import json

print('Loading function')

def lambda_handler(event, context):
    Body = {
    "response":{
        "resultStatus": "SUCCESS"
        }    
    }

    return {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json"
    },
    "body": json.dumps(Body)
    }
