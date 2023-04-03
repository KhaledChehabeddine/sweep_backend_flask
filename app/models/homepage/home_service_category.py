"""Home Service Category Model

A home service category model used to convert a home service category document into a home service category object
"""


class HomeServiceCategory:
    """
    A class to represent a home service category model

    Attributes
    ----------
    service_category_item_list : list
        service category item list

    Methods
    -------
    get_service_category_item_list() : list
        Returns the service category item list
    set_service_category_item_list(service_category_item_list) : None
        Sets the service category item list
    """

    def __init__(self, service_category_item_document: dict) -> None:
        self.service_category_item_list = service_category_item_document['service_category_item_list']

    def get_service_category_item_list(self) -> list:
        """
        :return: service category item list
        """
        return self.service_category_item_list

    def set_service_category_item_list(self, service_category_item_list: list) -> None:
        """
        :param service_category_item_list: service category item list
        """
        self.service_category_item_list = service_category_item_list
