import boto3
ddb = boto3.client("dynamodb")

def handler(event, context):

    name = event['Name']
    email = event['Email']
    url = event['URL']

    try:
        data = ddb.put_item(
            TableName="testhistory",
            Item={
                'Name': {
                    'S': name
                },
                'Email': {
                    'S': email
                },
                'URL': {
                    'S': url
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
