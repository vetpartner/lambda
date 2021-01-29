import json

def lambda_handler(event, context):
    # TODO implement
    print("This is a test from Github action"）
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
