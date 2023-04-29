"""Summary: Company Model

A company model used to convert a company document into a company object
"""
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.models.user.service_provider import ServiceProvider
from app.models.user.metadata.company_metadata import CompanyMetadata


class Company:
    """
    A class to represent a company model


    Attributes
    ----------
    banner_image_path : str
        Company's banner image path
    banner_image_url : str
        Company's banner image url
    _id : str
        Company's id
    logo_image_path : str
        Company's logo image path
    logo_image_url : str
        Company's logo image url
    name : str
        Company's name
    metadata : dict
        Company's metadata document
    service_category_ids : list[str]
        Service provider's service category ids
    service_provider : dict
        Company's service provider document
    """

    def __init__(self, company_document: dict) -> None:
        self.banner_image_path = company_document['banner_image_path']
        self.banner_image_url = create_cloudfront_url(file_path=self.banner_image_path)
        self._id = str(company_document['_id'])
        self.logo_image_path = company_document['logo_image_path']
        self.logo_image_url = create_cloudfront_url(file_path=self.logo_image_path)
        self.name = company_document['name']
        self.metadata = CompanyMetadata(company_document['metadata']).__dict__
        self.service_category_ids = company_document['service_category_ids']
        self.service_provider = ServiceProvider(company_document['service_provider']).__dict__

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the company object (without _id)
        """
        return {
            'banner_image_path': self.banner_image_path,
            'banner_image_url': self.banner_image_url,
            'logo_image_path': self.logo_image_path,
            'logo_image_url': self.logo_image_url,
            'name': self.name,
            'metadata': self.metadata,
            'service_category_ids': self.service_category_ids,
            'service_provider': self.service_provider,
        }
