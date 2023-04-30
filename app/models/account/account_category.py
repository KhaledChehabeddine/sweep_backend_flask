"""Summary: Account Category Model

An account category model used to convert an account category document into an account category object
"""
from app.models.account.account_category_item import AccountCategoryItem
from app.models.account.metadata.account_category_metadata import AccountCategoryMetadata


class AccountCategory:
    """
    A class to represent an account category model


    Attributes
    ----------
    account_category_items : list[dict]
        Account category's account category items
    _id : str
        Account category's id
    metadata : dict
        Account category's metadata document
    name : str
        Account category's name
    """

    def __init__(self, account_category_document: dict) -> None:
        self.account_category_items = [
            AccountCategoryItem(account_category_item_document=account_category_item_document).__dict__
            for account_category_item_document in account_category_document['account_category_items']
        ]
        self._id = str(account_category_document['_id'])
        self.metadata = AccountCategoryMetadata(account_category_document['metadata']).__dict__
        self.name = account_category_document['name']

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the account category object (without _id)
        """
        return {
            'account_category_items': self.account_category_items,
            'metadata': self.metadata,
            'name': self.name
        }
