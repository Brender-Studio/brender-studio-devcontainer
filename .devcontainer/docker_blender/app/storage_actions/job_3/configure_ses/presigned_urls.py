import os
import boto3
from botocore.exceptions import ClientError
from botocore.client import Config
import boto3.session
import logging
logging.basicConfig(level=logging.DEBUG)

bucket_name = os.environ.get('BUCKET_NAME')
bucket_key = os.environ.get('BUCKET_KEY')
access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')


def generate_presigned_urls(region):
    try:
        session = boto3.session.Session(
            region_name=region,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key)

        s3_client = session.client('s3', 
                                   endpoint_url=f"https://s3.{region}.amazonaws.com",
                                   aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, config=Config(signature_version='s3v4'))

        # Generate presigned url for thumbnail
        thumbnail_presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': f"{bucket_key}/bs_thumbnail.png"
            },
            ExpiresIn=604800  # 1 week
        )
        # Generate presigned url for output.zip
        output_zip_presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': f"{bucket_key}/output.zip"
            },
            ExpiresIn=604800  # 1 week
        )
        return thumbnail_presigned_url, output_zip_presigned_url
    except ClientError as e:
        print(f"Error: {e.response['Error']['Code']}")
        return None, None 