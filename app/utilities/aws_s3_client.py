"""Summary: AWS S3 Operations

A client that contains operations related to AWS S3
"""

import os
import base64
from io import BytesIO
import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError
from flask import jsonify, Response

AWS_S3_CLIENT = None


# pylint: disable=global-statement
def get_aws_s3_client() -> BaseClient:
    """
    :return: AWS S3 client
    """
    global AWS_S3_CLIENT
    if AWS_S3_CLIENT is None:
        AWS_S3_CLIENT = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
    return AWS_S3_CLIENT


def upload_to_aws_s3(file_data: str, file_path: str) -> Response:
    """
    :param file_data: The byte data of the file
    :param file_path: The path of the file
    :return: Response object with a message describing if the file was uploaded and the status code
    """
    try:
        file_bytes = base64.b64decode(file_data)
        with BytesIO(file_bytes) as file:
            get_aws_s3_client().upload_fileobj(file, os.getenv('AWS_S3_BUCKET'), file_path)
    except ClientError:
        return jsonify({
            'message': 'File not uploaded into the AWS S3 bucket.',
            'status': 500
        })
    return jsonify({
        'message': 'File uploaded into the AWS S3 bucket.',
        'status:': 200
    })
