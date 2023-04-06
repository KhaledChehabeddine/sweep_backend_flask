"""Summary: Account Sub Category Model

An account sub category model used to convert an account sub category document into an account sub category object
"""

from typing import List
from app.models.account.account_category_item import AccountCategoryItem


class AccountSubCategory:
    """
    A class to represent an account sub category model


    Attributes
    ----------
    account_category_items : List[AccountMainCategoryItem]
        Account sub category's items
    category : str
        Account sub category's name
    _id : str
        Account sub category's id

    Methods
    -------
    get_account_sub_category_items() : List[AccountMainCategoryItem]
        Returns the account sub category's items
    set_account_sub_category_items(account_main_category_items) : None
        Sets the account sub category's items
    get_category() : str
        Returns the account sub category's name
    set_category(category) : None
        Sets the account sub category's name
    get_id() : str
        Returns the account sub category's id
    set_id(_id) : None
        Sets the account sub category's id
    """

    def __init__(self, account_main_category_document: dict) -> None:
        self.account_category_items = account_main_category_document['account_category_items']
        self.category = account_main_category_document['category']
        self._id = account_main_category_document['_id']

    def get_account_main_category_items(self) -> List[AccountCategoryItem]:
        """
        :return: Account sub category's items
        """
        return self.account_category_items

    def set_account_main_category_items(self, account_category_items: List[AccountCategoryItem]) -> None:
        """
        :param account_category_items: Account sub category's items
        """
        self.account_category_items = account_category_items

    def get_category(self) -> str:
        """
        :return: Account sub category's items
        """
        return self.category

    def set_category(self, category: str) -> None:
        """
        :param category: Account sub category's items
        """
        self.category = category

    def get_id(self) -> str:
        """
        :return: Account sub category's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Account sub category's id
        """
        self._id = _id
