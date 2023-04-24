"""Summary: AWS CloudFront Operations

A client that contains operations related to AWS CloudFront
"""

import os
import uuid
import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError
from flask import Response, jsonify

AWS_CLOUDFRONT_CLIENT = None


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


def create_cloudfront_invalidation() -> Response:
    """
    :return: Response object with a message describing if the invalidation was created and the status code
    """
    try:
        get_aws_cloudfront_client().create_invalidation(
            DistributionId=os.getenv('AWS_CLOUDFRONT_DISTRIBUTION_ID'),
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': ['/*']
                },
                'CallerReference': str(uuid.uuid4())
            }
        )
    except ClientError:
        return jsonify(
            message='Invalidation not created.',
            status=500
        )
    return jsonify(
        message='Invalidation created.',
        status=200
    )


def create_cloudfront_url(file_path: str) -> str:
    """
    :param file_path: The path of the file
    :return: CloudFront URL for the file in the distribution origin
    """
    return os.getenv('AWS_CLOUDFRONT_DOMAIN_NAME') + file_path
