import json
import boto3
from datetime import datetime
import os
import urllib.request

def lambda_handler(event, context):

    api_url = 'https://randomuser.me/api/?results=10'

    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read().decode())

    bucket_name = os.environ['STG_BUCKET']           
    folder_name = os.environ['STG_FOLDER']    

    
    file_name = f"{folder_name}/randomuser.json"

    # Upload to S3
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data),
        ContentType='application/json'
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'File saved to {file_name}'}) 
        
    }
