"""Summary: AWS CloudFront Operations

A client that contains operations related to AWS CloudFront
"""

import os
import boto3
from botocore.client import BaseClient
from app.utilities.aws_s3_client import create_presigned_url

AWS_CLOUDFRONT_CLIENT = None


# pylint: disable=global-statement
def get_aws_cloudfront_client() -> BaseClient:
    """
    :return: AWS CloudFront client
    """
    global AWS_CLOUDFRONT_CLIENT
    if AWS_CLOUDFRONT_CLIENT is None:
        AWS_CLOUDFRONT_CLIENT = boto3.client(
            'cloudfront',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
    return AWS_CLOUDFRONT_CLIENT


def get_cloudfront_url(file_path: str) -> str:
    """
    :param file_path: The path of the file
    :return: CloudFront URL for the file in the distribution origin
    """
    return os.getenv('AWS_CLOUDFRONT_URL') + file_path + '?url=' + create_presigned_url(file_path=file_path)
