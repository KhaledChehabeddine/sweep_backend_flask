"""Summary: Worker Model

A worker model used to convert a worker document into a worker object
"""
from app.models.user.service_provider import ServiceProvider
from app.models.user.metadata.worker_metadata import WorkerMetadata
from bson import ObjectId
from app.aws.aws_cloudfront_client import create_cloudfront_url


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
        self.banner_image_path = str(worker_document.get('banner_image_path', ''))
        self.banner_image_url = create_cloudfront_url(image_path=self.banner_image_path)
        self.company_id = str(worker_document.get('company_id', ''))
        self.first_name = str(worker_document.get('first_name', ''))
        self._id = str(worker_document.get('_id', ''))
        self.last_name = str(worker_document.get('last_name', ''))
        self.metadata = WorkerMetadata(worker_document.get('metadata', {})).__dict__
        self.middle_name = str(worker_document.get('middle_name', ''))
        self.profile_image_path = str(worker_document.get('profile_image_path', ''))
        self.profile_image_url = create_cloudfront_url(image_path=self.profile_image_path)
        self.service_category_id = str(worker_document.get('service_category_id', ''))
        self.service_provider = ServiceProvider(worker_document.get('service_provider', {}))

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the worker object (without _id)
        """
        worker_dict = {
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
        }

        if isinstance(self._id, ObjectId):
            worker_dict['_id'] = str(self._id)

        if isinstance(self.service_provider, ServiceProvider):
            worker_dict['service_provider'] = self.service_provider.database_dict()

        return worker_dict
