"""Summary: AWS S3 Operations

A client that contains operations related to AWS S3
"""
import os
import base64
from io import BytesIO
from typing import Any
import boto3
from PIL import Image
from botocore.client import BaseClient
from botocore.exceptions import ClientError
from flask import jsonify, Response
from app.aws.aws_cloudfront_client import create_cloudfront_invalidation

AWS_IMAGE_FORMATS = {
    'avif': 'image/avif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'svg': 'image/svg+xml',
    'webp': 'image/webp'
}
AWS_S3_CLIENT = None


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


def delete_image_from_aws_s3(image_path: str) -> Response:
    """
    :param image_path: The path of the image
    :return: Response object with a message describing if the image was deleted and the status code
    """
    try:
        get_aws_s3_client().delete_object(Bucket=os.getenv('AWS_S3_BUCKET'), Key=image_path)
    except ClientError:
        return jsonify(
            message='Image not deleted from the AWS S3 bucket.',
            status=500
        )
    return jsonify(
        message='Image deleted from the AWS S3 bucket.',
        status=200
    )


def delete_images_from_aws_s3(image_paths: list[str]) -> Response:
    """
    :param image_paths: A list of image paths
    :return: Response object with a message describing if the images were deleted and the status code
    """
    try:
        get_aws_s3_client().delete_objects(
            Bucket=os.getenv('AWS_S3_BUCKET'),
            Delete={
                'Objects': [{'Key': image_path} for image_path in image_paths]
            }
        )
    except ClientError:
        return jsonify(
            message='Images not deleted from the AWS S3 bucket.',
            status=500
        )
    return jsonify(
        message='Images deleted from the AWS S3 bucket.',
        status=200
    )


def upload_image_to_aws_s3(object_metadata_document: dict, object_image: tuple[str, Any, Any]) -> Response:
    """
    :param object_metadata_document: An object metadata document
    :param object_image: A tuple of the image info in the format [type, data, path]
    :return: Response object with a message describing if the image was uploaded and the status code
    """
    try:
        image_bytes = base64.b64decode(object_image[1])
        with BytesIO(image_bytes) as image_bytes_io:
            image = Image.open(image_bytes_io)
            image_size = image.size

            object_metadata_document[object_image[0] + 'image_format'] = image.format.lower()
            object_metadata_document[object_image[0] + 'image_height'] = image_size[0]
            object_metadata_document[object_image[0] + 'image_width'] = image_size[1]

            content_type = AWS_IMAGE_FORMATS[object_metadata_document[object_image[0] + 'image_format']]

            get_aws_s3_client().upload_fileobj(
                BytesIO(image_bytes),
                os.getenv('AWS_S3_BUCKET'),
                object_image[2],
                ExtraArgs={
                    'ContentType': content_type,
                }
            )
    except ClientError:
        return jsonify(
            message='Image not uploaded into the AWS S3 bucket.',
            status=500
        )
    return jsonify(
        data=object_metadata_document,
        message='Image uploaded into the AWS S3 bucket.',
        status=200
    )


def upload_images_to_aws_s3(object_metadata_document: dict, object_images: list[tuple[str, Any, Any]]) -> Response:
    """
    :param object_metadata_document: An object metadata document
    :param object_images: A list of tuples of each image info in the format [type, data, path]
    :return: Response object with a message describing if the images were uploaded to AWS S3 and CloudFront invalidation
    was done
    """
    for object_image in object_images:
        object_metadata_document = upload_image_to_aws_s3(
            object_metadata_document=object_metadata_document,
            object_image=object_image
        ).json['data']

    create_cloudfront_invalidation()

    return jsonify(
        data=object_metadata_document,
        message='Images uploaded to AWS S3 and CloudFront invalidation created.',
        status=200
    )
