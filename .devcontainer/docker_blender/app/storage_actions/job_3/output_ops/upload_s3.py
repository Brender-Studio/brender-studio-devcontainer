import os
import boto3
from botocore.exceptions import ClientError

bucket_name = os.environ.get('BUCKET_NAME')
bucket_key = os.environ.get('BUCKET_KEY')
access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

def upload_to_s3(render_output_path, zip_path, thumbnail_path):
    if not (bucket_name and bucket_key and access_key_id and secret_access_key):
        print("Error: Missing environment variables.")
        return False

    # Upload the /output folder and output.zip to the specified S3 bucket
    print("Subiendo a S3...")
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    try:
        for root, dirs, files in os.walk(render_output_path):
            for file in files:
                local_path = os.path.join(root, file)
                s3_path = os.path.join(bucket_key, 'output', os.path.relpath(local_path, render_output_path))
                s3.upload_file(local_path, bucket_name, s3_path)

        s3.upload_file(zip_path, bucket_name, f"{bucket_key}/output.zip")
        s3.upload_file(thumbnail_path, bucket_name, f"{bucket_key}/bs_thumbnail.png")
        print("Files uploaded to S3")
        return True
    except ClientError as e:
        print(f"Error uploading to S3: {e}")
        return False