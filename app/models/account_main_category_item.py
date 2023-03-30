"""Summary: Account Main Category Item Model

An account main category item model used to convert an account main category item document into an account main category
item object
"""


class AccountMainCategoryItem:
    """
    A class to represent an account main category item model


    Attributes
    ----------
    icon : str
        Account main category item's icon
    name : str
        Account main category item's name

    Methods
    -------
    get_icon() : str
        Returns the account main category item's icon
    set_icon(icon) : None
        Sets the account main category item's icon
    get_name() : str
        Returns the account main category item's name
    set_name(name) : None
        Sets the account main category item's name
    """

    def __init__(self, icon: str, name: str) -> None:
        self.icon = icon
        self.name = name

    def get_icon(self) -> str:
        """
        :return: Account main category item's icon
        """
        return self.icon

    def set_icon(self, icon: str) -> None:
        """
        :param icon: Account main category item's icon
        """
        self.icon = icon

    def get_name(self) -> str:
        """
        :return: Account main category item's name
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        :param name: Account main category item's name
        """
        self.name = name
