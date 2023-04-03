"""Summary: Service Category Item Model

A service category item model used to convert a service category item document into a service category item object
"""


class ServiceCategoryItem:
    """
    A class to represent a service category item model


    Attributes
    ----------
    active : bool
        Service category item's activity
    icon : str
        Service category item's icon
    name : str
        Service category item's name

    Methods
    -------
    get_active() : bool
        Returns the service category item's activity
    set_active(active) : None
        Sets the service category item's activity
    get_icon() : str
        Returns the service category item's icon
    set_icon(icon) : None
        Sets the service category item's icon
    get_name() : str
        Returns the service category item's name
    set_name(name) : None
        Sets the service category item's name
    """

    def __init__(self, service_category_item_document: dict) -> None:
        self.active = service_category_item_document['active']
        self.icon = service_category_item_document['icon']
        self.name = service_category_item_document['name']

    def get_active(self) -> bool:
        """
        :return: Service category item's activity
        """
        return self.active

    def set_active(self, active: bool) -> None:
        """
        :param active: Service category item's activity
        """
        self.active = active

    def get_icon(self) -> str:
        """
        :return: Service category item's icon
        """
        return self.icon

    def set_icon(self, icon: str) -> None:
        """
        :param icon: Service category item's icon
        """
        self.icon = icon

    def get_name(self) -> str:
        """
        :return: Service category item's name
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        :param name: Service category item's name
        """
        self.name = name
