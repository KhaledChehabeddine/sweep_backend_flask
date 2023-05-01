"""Summary: Service Category Metadata Model

A service category metadata model used to convert a service category metadata document into a service category metadata
object
"""


class ServiceCategoryMetadata:
    """
    A class to represent a service category metadata model

    Attributes
    ----------
    created_date : datetime
        Service Category's created date
    image_format : str
        Service Category's image format
    image_height : int
        Service Category's image height
    image_width : int
        Service Category's image width
    updated_date : datetime
        Service Category's updated date
    """

    def __init__(self, service_category_metadata_document: dict) -> None:
        self.created_date = service_category_metadata_document['created_date']
        self.image_format = str(service_category_metadata_document['image_format'])
        self.image_height = int(service_category_metadata_document['image_height'])
        self.image_width = int(service_category_metadata_document['image_width'])
        self.updated_date = service_category_metadata_document['updated_date']
