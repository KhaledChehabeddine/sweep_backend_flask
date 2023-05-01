"""Summary: Company Metadata Model

A company metadata model used to convert a company metadata document into a company metadata object
"""


class CompanyMetadata:
    """
    A class to represent a company metadata model


    Attributes
    ----------
    banner_image_format : str
        Company's banner image format
    banner_image_height : int
        Company's banner image height
    banner_image_width : int
        Company's banner image width
    logo_image_format : str
        Company's logo image format
    logo_image_height : int
        Company's logo image height
    logo_image_width : int
        Company's logo image width
    total_employees : int
        Company's total employees
    total_service_categories : int
        Service provider's total service categories
    """

    def __init__(self, company_metadata_document: dict) -> None:
        self.banner_image_format = str(company_metadata_document['banner_image_format'])
        self.banner_image_height = int(company_metadata_document['banner_image_height'])
        self.banner_image_width = int(company_metadata_document['banner_image_width'])
        self.logo_image_format = str(company_metadata_document['logo_image_format'])
        self.logo_image_height = int(company_metadata_document['logo_image_height'])
        self.logo_image_width = int(company_metadata_document['logo_image_width'])
        self.total_employees = int(company_metadata_document['total_employees'])
        self.total_service_categories = int(company_metadata_document['total_service_categories'])
