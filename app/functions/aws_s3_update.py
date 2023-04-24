"""Summary: AWS Update Operation Status Function

A function to perform the AWS S3 and CloudFront update operations
"""
from flask import Response, jsonify
from app.aws.aws_cloudfront_client import create_cloudfront_invalidation
from app.aws.aws_s3_client import upload_to_aws_s3


def aws_s3_update(object_image_list: list[tuple[str, str]]) -> Response:
    """
    :param object_image_list: A list of tuple(s) of for each image in the format [file_path, image]
    :return: Response object with a message describing if the image(s) were uploaded to AWS S3 and CloudFront
    invalidation was done
    """
    for object_image in object_image_list:
        if upload_to_aws_s3(file_data=object_image[1], file_path=object_image[0]).json['status'] != 200:
            return jsonify(
                message='Image(s) not uploaded to AWS S3.',
                status=500
            )
    if create_cloudfront_invalidation().json['status'] != 200:
        return jsonify(
            message='CloudFront invalidation not created.',
            status=500
        )
    return jsonify(
        message='Image(s) uploaded to AWS S3 and CloudFront invalidation created.',
        status=200
    )
