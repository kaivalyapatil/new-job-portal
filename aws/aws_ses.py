import boto3
import os
from botocore.exceptions import ClientError

def send_email(subject, message, from_addr, to_addr) -> None :

    
    try:
        region=os.environ["AWS_REGION"]
        access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
        secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
        ses = boto3.client("ses", 
            region_name=region,
            aws_access_key_id=access_key_id,  
            aws_secret_access_key=secret_access_key)    
    except Exception  as ex:
        ses = boto3.client("ses")

    CHARSET = "UTF-8"
    try:
        #Provide the contents of the email.
        response = ses.send_email(
            Destination={ 'ToAddresses': [ to_addr ]  },
            Message={
                'Body': {                    
                    'Text': {
                        'Charset': CHARSET,
                        'Data': message,
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                },
            },
            Source=from_addr
        )    
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Email sent! Message ID:{response['MessageId']}")