"""Summary: Service Item Metadata Model

A service item metadata model used to convert an service item metadata document into an service item metadata object
"""


class ServiceItemMetadata:
    """
    A class to represent a review metadata model

    Attributes
    ----------
    created_date : datetime
        Service item's created date
    image_format : str
        Service item's banner image format
    image_height : int
        Service item's banner image height
    image_width : int
        Service item's banner image width
    updated_date : datetime
        Service item's updated date
    """

    def __init__(self, service_item_metadata_document) -> None:
        self.created_date = service_item_metadata_document['created_date']
        self.image_format = service_item_metadata_document['image_format']
        self.image_height = service_item_metadata_document['image_height']
        self.image_width = service_item_metadata_document['image_width']
        self.updated_date = service_item_metadata_document['updated_date']
