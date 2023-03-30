"""Summary: Account Category Item Model

An account category item model used to convert an account category item document into an account category
item object
"""


class AccountCategoryItem:
    """
    A class to represent an account category item model


    Attributes
    ----------
    icon : str
        Account category item's icon
    name : str
        Account category item's name

    Methods
    -------
    get_icon() : str
        Returns the account category item's icon
    set_icon(icon) : None
        Sets the account category item's icon
    get_name() : str
        Returns the account category item's name
    set_name(name) : None
        Sets the account category item's name
    """

    def __init__(self, account_category_item_document: dict) -> None:
        self.icon = account_category_item_document['icon']
        self.name = account_category_item_document['name']

    def get_icon(self) -> str:
        """
        :return: Account category item's icon
        """
        return self.icon

    def set_icon(self, icon: str) -> None:
        """
        :param icon: Account category item's icon
        """
        self.icon = icon

    def get_name(self) -> str:
        """
        :return: Account category item's name
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        :param name: Account category item's name
        """
        self.name = name
