"""Summary: AWS S3 Client Operations

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
        AWS_S3_CLIENT = boto3.client('s3',
                                     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    return AWS_S3_CLIENT


def create_presigned_url(bucket: str, file_name: str) -> str:
    """
    :param bucket: The bucket of the file
    :param file_name: The path of the file
    :return: Presigned URL for the file in the bucket
    """
    return get_aws_s3_client().generate_presigned_url('get_object',
                                                      ExpiresIn=3600,
                                                      Params={
                                                          'Bucket': bucket,
                                                          'Key': file_name
                                                      })


def upload_to_aws_s3(bucket: str, file_data: str, file_name: str) -> Response:
    """
    :param bucket: The bucket of the file
    :param file_data: The byte data of the file
    :param file_name: The path of the file
    :return: Response object with a message describing if the file was uploaded and the status code
    """
    try:
        file_bytes = base64.b64decode(file_data)
        with BytesIO(file_bytes) as file:
            get_aws_s3_client().upload_fileobj(file, bucket, file_name)
    except ClientError:
        return jsonify({
            'message': 'File not uploaded into AWS S3 bucket.',
            'status': 500
        })
    return jsonify({
        'message': 'File uploaded into AWS S3 bucket.',
        'status:': 200
    })