"""Summary: Company Model

A company model used to convert a company document into a company object
"""
from app.models.components.service_provider import ServiceProvider
from app.models.user.metadata.company_metadata import CompanyMetadata
from app.models.user.user import User


class Company:
    """
    A class to represent a company model


    Attributes
    ----------
    banner_file_path : str
        Company's banner file path
    banner_image_url : str
        Company's banner image url
    _id : str
        Company's id
    logo_file_path : str
        Company's logo file path
    logo_image_url : str
        Company's logo image url
    name : str
        Company's name
    metadata : dict
        Company's metadata document
    service_provider : dict
        Company's service provider document
    user : dict
        Company's user document
    """

    def __init__(self, company_document: dict) -> None:
        self.banner_file_path = company_document['banner_file_path']
        self.banner_image_url = ''
        self._id = str(company_document['_id'])
        self.logo_file_path = company_document['logo_file_path']
        self.logo_image_url = ''
        self.name = company_document['name']
        self.metadata = CompanyMetadata(company_document['metadata']).__dict__
        self.service_provider = ServiceProvider(company_document['service_provider']).__dict__
        self.user = User(company_document['user']).__dict__

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the company object (without _id and image_urls)
        """
        return {
            'banner_file_path': self.banner_file_path,
            'logo_file_path': self.logo_file_path,
            'name': self.name,
            'metadata': self.metadata,
            'service_provider': self.service_provider,
            'user': self.user
        }
