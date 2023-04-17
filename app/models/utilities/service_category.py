"""Summary: Service Category Model

A service category model used to convert a service category document into a service category object
"""


class ServiceCategory:
    """
    A class to represent a service category model

    Attributes
    ----------
    active : bool
        Service Category's active status
    file_path : str
        Service Category's file path
    _id : str
        Service Category's id
    image_url : str
        Service Category's image url
    name : str
        Service Category's name
    """

    def __init__(self, service_category_document: dict) -> None:
        self.active = service_category_document['active']
        self.file_path = service_category_document['file_path']
        self._id = service_category_document['_id']
        self.image_url = ''
        self.name = service_category_document['name']

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the service category object (without _id and image_url)
        """
        return {
            'active': self.active,
            'file_path': self.file_path,
            'name': self.name,
        }
