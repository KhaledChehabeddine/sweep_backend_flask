"""Summary: account Main Category Model

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
        account main category's items

    Methods
    -------
    get_account_category_items() : List[AccountCategoryItem]
        Returns the account main category's items
    set_account_category_items(account_category_items) : None
        Sets the account main category's items
    """
    def __init__(self, account_main_category_document: dict) -> None:
        self.account_category_items = account_main_category_document['account_category_items']

    def get_account_category_items(self) -> List[AccountCategoryItem]:
        """
        :return: account main category's items
        """
        return self.account_category_items

    def set_account_category_items(self, account_category_items: List[AccountCategoryItem]) -> None:
        """
        :param account_category_items: account main category's items
        """
        self.account_category_items = account_category_items
