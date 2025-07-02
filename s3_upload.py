# Chandler Thomas
# July 2nd, 2025
# Simple CLI tool for AWS S3

import boto3
import argparse
import os
from botocore.exceptions import NoCredentialsError, ClientError


def upload_file(file_path, bucket_name):
    s3 = boto3.client('s3')
    try:
        file_name = os.path.basename(file_path)
        s3.upload_file(file_path, bucket_name, file_name)
        region = s3.meta.region_name
        print(f"File uploaded successfully! S3 Key: {file_name}, Region: {region}")
    except FileNotFoundError:
        print("File not found.")
    except NoCredentialsError:
        print("AWS credentials not found.")
    except ClientError as e:
        print(f"Upload failed: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Upload a file to AWS S3")
    parser.add_argument("file_path", help="Local file path")
    parser.add_argument("bucket_name", help="Target S3 bucket name")
    args = parser.parse_args()

    upload_file(args.file_path, args.bucket_name)
