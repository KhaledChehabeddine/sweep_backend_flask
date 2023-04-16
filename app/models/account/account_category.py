"""Summary: Account Main Category Model

An account category model used to convert an account category document into an account category object
"""


class AccountCategory:
    """
    A class to represent an account category model


    Attributes
    ----------
    _id : str
        Account category's id
    name : str
        Account category's name
    """
    def __init__(self, account_category_document: dict) -> None:
        self._id = str(account_category_document['_id'])
        self.name = account_category_document['name']

    def database_dict(self) -> dict:
        """
        :return: Account category's dict (without _id)
        """
        return {
            'name': self.name
        }
