"""Summary: Worker Model

A worker model used to convert a worker document into a worker object
"""
from app.models.components.service_provider import ServiceProvider
from app.models.user.metadata.worker_metadata import WorkerMetadata
from app.models.user.user import User


class Worker:
    """
    A class to represent a worker model


    Attributes
    ----------
    banner_file_path : str
        Worker's banner file path
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
    profile_file_path : str
        Worker's profile file path
    profile_image_url : str
        Worker's profile image url
    service_provider : dict
        Worker's service provider document
    user : dict
        Worker's user document
    """

    def __init__(self, worker_document: dict) -> None:
        self.banner_file_path = worker_document['banner_file_path']
        self.banner_image_url = ''
        self.company_id = worker_document['company_id']
        self.first_name = worker_document['first_name']
        self._id = str(worker_document['_id'])
        self.last_name = worker_document['last_name']
        self.metadata = WorkerMetadata(worker_document['metadata']).__dict__
        self.middle_name = worker_document['middle_name']
        self.profile_file_path = worker_document['profile_file_path']
        self.profile_image_url = ''
        self.service_provider = ServiceProvider(worker_document['service_provider']).__dict__
        self.user = User(user_document=worker_document['user']).__dict__

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the worker object (without _id and image_urls)
        """
        return {
            'banner_file_path': self.banner_file_path,
            'company_id': self.company_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'metadata': self.metadata,
            'middle_name': self.middle_name,
            'profile_file_path': self.profile_file_path,
            'service_provider': self.service_provider,
            'user': self.user
        }
