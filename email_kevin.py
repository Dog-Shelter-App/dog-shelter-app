import os
import boto3

# create dotenv data store
from dotenv import load_dotenv
load_dotenv('.env')
# get aws access key
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")


SES_CLIENT = boto3.client(
  'ses',
  aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
  aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
)

print(SES_CLIENT)

response = SES_CLIENT.send_email(
  Destination={
    'ToAddresses': ['houstonseosolutions@gmail.com'],
  },
  Message={
    'Body': {
      'Text': {
        'Charset': 'UTF-8',
        'Data': 'This is the message body in text format.',
      },
    },
    'Subject': {'Charset': 'UTF-8', 'Data': 'Test email'},
  },
  Source='houstonseosolutions@gmail.com',
)

print(response)
