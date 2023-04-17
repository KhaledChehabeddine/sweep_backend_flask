"""Summary: AWS Update Operation Status Function

A function to perform the AWS S3 and CloudFront update operations
"""

from app.aws.aws_cloudfront_client import create_cloudfront_invalidation
from app.aws.aws_s3_client import upload_to_aws_s3


def aws_update_operations(object_document: dict) -> None:
    """
    :param object_document: A dictionary representing a object document
    """
    if object_document['image']:
        upload_to_aws_s3(file_data=object_document['image'], file_path=object_document['file_path'])
        create_cloudfront_invalidation()
