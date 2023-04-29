"""Summary: Worker Model

A worker model used to convert a worker document into a worker object
"""
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.models.user.service_provider import ServiceProvider
from app.models.user.metadata.worker_metadata import WorkerMetadata


class Worker:
    """
    A class to represent a worker model


    Attributes
    ----------
    banner_image_path : str
        Worker's banner image path
    banner_image_url : str
        Worker's banner image url
    company_id : str
        Worker's company id
    first_name : str
        Worker's first name
    _id : str
        Worker's id
    last_name : str
        Worker's last name
    metadata : dict
        Worker's metadata document
    middle_name : str
        Worker's middle name
    profile_image_path : str
        Worker's profile image path
    profile_image_url : str
        Worker's profile image url
    service_category_id : str
        Service provider's service category id
    service_provider : dict
        Worker's service provider document
    """

    def __init__(self, worker_document: dict) -> None:
        self.banner_image_path = worker_document['banner_image_path']
        self.banner_image_url = create_cloudfront_url(file_path=self.banner_image_path)
        self.company_id = worker_document['company_id']
        self.first_name = worker_document['first_name']
        self._id = str(worker_document['_id'])
        self.last_name = worker_document['last_name']
        self.metadata = WorkerMetadata(worker_document['metadata']).__dict__
        self.middle_name = worker_document['middle_name']
        self.profile_image_path = worker_document['profile_image_path']
        self.profile_image_url = create_cloudfront_url(file_path=self.profile_image_path)
        self.service_category_id = worker_document['service_category_id']
        self.service_provider = ServiceProvider(worker_document['service_provider']).__dict__

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the worker object (without _id)
        """
        return {
            'banner_image_path': self.banner_image_path,
            'banner_image_url': self.banner_image_url,
            'company_id': self.company_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'metadata': self.metadata,
            'middle_name': self.middle_name,
            'profile_image_path': self.profile_image_path,
            'profile_image_url': self.profile_image_url,
            'service_category_id': self.service_category_id,
            'service_provider': self.service_provider,
        }
