"""Summary: Account Main Category Model

An account main category model used to convert an account main category document into an account main category object
"""

from typing import List
from app.models.account.account_category_item import AccountCategoryItem


class AccountMainCategory:
    """
    A class to represent an account main category model


    Attributes
    ----------
    account_category_items : List[AccountMainCategoryItem]
        Account main category's items
    _id : str
        Account main category's id

    Methods
    -------
    get_account_category_items() : List[AccountCategoryItem]
        Returns the account main category's items
    set_account_category_items(account_category_items) : None
        Sets the account main category's items
    get_id() : str
        Returns the account main category's id
    set_id(_id) : None
        Sets the account main category's id
    """
    def __init__(self, account_main_category_document: dict) -> None:
        self.account_category_items = account_main_category_document['account_category_items']
        self._id = account_main_category_document['_id']

    def get_account_category_items(self) -> List[AccountCategoryItem]:
        """
        :return: Account main category's items
        """
        return self.account_category_items

    def set_account_category_items(self, account_category_items: List[AccountCategoryItem]) -> None:
        """
        :param account_category_items: Account main category's items
        """
        self.account_category_items = account_category_items

    def get_id(self) -> str:
        """
        :return: Account main category's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Account main category's id
        """
        self._id = _id
