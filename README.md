# AWS S3 Upload CLI Tool

A simple Python command-line tool that uploads local files to an AWS S3 bucket using the `boto3` SDK.

## Author and Programmer
Chandler Thomas

July 2, 2025

## Features

- Accepts a local file path and S3 bucket name via command-line arguments
- Uploads the file to the specified bucket using AWS SDK
- Prints a success message including the file's S3 key and region
- Handles basic errors such as file not found or missing AWS credentials

## Requirements

- Python 3.x
- boto3 (`pip install boto3`)
- AWS CLI (`pip install awscli`) and credentials configured via `aws configure`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/s3-upload-cli-tool.git
   cd s3-upload-cli-tool

2. Install dependencies:
   pip install boto3

3. Configure AWS credentials if not already set up:
   aws configure

## Usage

1. Run the script with:
   python s3_upload.py <file_path> <bucket_name>  \\Example: python s3_upload.py ./myfile.txt my-s3-bucket

## Assumptions

- AWS credentials are pre-configured via AWS CLI, environment variables, or credentials file
- The target S3 bucket already exists
- Only public or authorized buckets will accept uploads

  
