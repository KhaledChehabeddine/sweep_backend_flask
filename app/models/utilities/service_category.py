"""Summary: Service Category Model

    A service category model used to convert a service category document into a service category object
"""


class ServiceCategory:
    """
    A class to represent a service category model

    Attributes
    ----------
    _id : str
        Service Category's id
    name : str
        Service Category's name
    icon : str
        Service Category's icon
    active : bool
        Service Category's active status
    """

    def __init__(self, service_category_document: dict) -> None:
        self.active = service_category_document['active']
        self.icon = service_category_document['icon']
        self._id = service_category_document['_id']
        self.name = service_category_document['name']

    def create_dict(self) -> dict:
        """
        :return: Service Category's dict (without _id)
        """
        return {
            'active': self.active,
            'icon': self.icon,
            'name': self.name,
        }
