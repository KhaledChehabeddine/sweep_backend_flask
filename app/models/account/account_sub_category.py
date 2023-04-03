"""
Summary: account Sub Category Model

An account sub category model used to convert an account sub category document into an account sub category object
"""

from typing import List
from app.models.account.account_category_item import AccountCategoryItem


class AccountSubCategory:
    """
    A class to represent an account sub category model


    Attributes
    ----------
    category : str
        account sub category's name
    account_main_category_items : List[AccountMainCategoryItem]
        account sub category's items

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
    """

    def __init__(self, category: str, account_main_category_document: dict) -> None:
        self.category = category
        self.account_main_category_items = account_main_category_document['account_main_category_items']

    def get_account_main_category_items(self) -> List[AccountCategoryItem]:
        """
        :return: account sub category's items
        """
        return self.account_main_category_items

    def set_account_main_category_items(self, account_main_category_items: List[AccountCategoryItem]) -> None:
        """
        :param account_main_category_items: account sub category's items
        """
        self.account_main_category_items = account_main_category_items

    def get_category(self) -> str:
        """
        :return: account sub category's items
        """
        return self.category

    def set_category(self, category: str) -> None:
        """
        :param category: account sub category's items
        """
        self.category = category
