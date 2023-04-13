"""Summary: Account Category Item Model

An account category item model used to convert an account category item document into an account category item object
"""


class AccountCategoryItem:
    """
    A class to represent an account category item model


    Attributes
    ----------
    account_category_name : str
        Account category item's account category name
    file_name : str
        Account category item's file name
    _id : str
        Account category item's id
    image_url : str
        Account category item's image url
    name : str
        Account category item's name
    """

    def __init__(self, account_category_item_document: dict) -> None:
        self.account_category_name = account_category_item_document['account_category_name']
        self.file_name = account_category_item_document['file_name']
        self._id = account_category_item_document['_id']
        self.image_url = ""
        self.name = account_category_item_document['name']

    def create_dict(self) -> dict:
        """
        :return: Account category item's dict (without _id)
        """
        return {
            'account_category_id': self.account_category_name,
            'file_name': self.file_name,
            'image_url': self.image_url,
            'name': self.name
        }
