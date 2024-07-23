import os
import boto3
from botocore.exceptions import ClientError

bucket_name = os.environ.get('BUCKET_NAME')
bucket_key = os.environ.get('BUCKET_KEY')
access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

def find_files_with_prefix(directory, prefix):
    files = []
    for file_name in os.listdir(directory):
        if file_name.startswith(prefix):
            files.append(os.path.join(directory, file_name))
    return files

def upload_animation_videos(efs_project_path):
    if not (bucket_name and bucket_key and access_key_id and secret_access_key):
        print("Error: Falta alguna variable de entorno.")
        return False

    # Upload the /output folder and output.zip to the specified S3 bucket
    print("Subiendo a S3...")
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    try:
        playblast_files = find_files_with_prefix(efs_project_path, 'bs_playblast')
        full_resolution_files = find_files_with_prefix(efs_project_path, 'bs_full_resolution')

        for playblast_file in playblast_files:
            s3_key = f"{bucket_key}/{os.path.basename(playblast_file)}"
            s3.upload_file(playblast_file, bucket_name, s3_key)
            print(f"File uploaded: {playblast_file} to {s3_key}")

        for full_resolution_file in full_resolution_files:
            s3_key = f"{bucket_key}/output/{os.path.basename(full_resolution_file)}"
            s3.upload_file(full_resolution_file, bucket_name, s3_key)
            print(f"File uploaded: {full_resolution_file} to {s3_key}")

        print("Upload complete to S3")
        return True
    except ClientError as e:
        print(f"Error uploading files to s3 {e}")
        return False