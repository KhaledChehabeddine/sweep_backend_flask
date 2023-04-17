"""Summary: Category Model

A category model used to convert a category document into a category object
"""


class Category:
    """
    A class to represent a category model

    Attributes
    ----------
    _id : str
        Category's id
    name : str
        Category's name
    services : List[Service]
        Category's services
    """

    def __init__(self, category_document) -> None:
        self._id = category_document['_id']
        self.name = category_document['name']
        self.services = category_document['services']

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the category object (without _id)
        """
        return {
            'name': self.name,
            'services': self.services
        }
