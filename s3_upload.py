# Chandler Thomas
# July 2nd, 2025
# Simple CLI tool for AWS S3

import boto3 # AWS SDK for Python
import argparse # For parsing command-line arguments
import os # For working with file paths
from botocore.exceptions import NoCredentialsError, ClientError


def upload_file(file_path, bucket_name):
    """
    Uploads a file to the specified S3 bucket.
    
    Parameters:
        file_path (str): Path to the local file
        bucket_name (str): Name of the target S3 Bucket
    """
    s3 = boto3.client('s3') # Create S3 client using default AWS credentials
    try:
        file_name = os.path.basename(file_path) # Extract the file name from the full path
        s3.upload_file(file_path, bucket_name, file_name) # Upload file to S3
        region = s3.meta.region_name # Get AWS region from the client metadata
        print(f"File uploaded successfully! S3 Key: {file_name}, Region: {region}")
    except FileNotFoundError:
        print("File not found.")
    except NoCredentialsError:
        print("AWS credentials not found.")
    except ClientError as e:
        print(f"Upload failed: {e}")


if __name__ == '__main__':
    # Set up command-line arguments for the script
    parser = argparse.ArgumentParser(description="Upload a file to AWS S3")
    parser.add_argument("file_path", help="Local file path")
    parser.add_argument("bucket_name", help="Target S3 bucket name")
    args = parser.parse_args()
    
    # Call the upload function with parsed arguments
    upload_file(args.file_path, args.bucket_name)
