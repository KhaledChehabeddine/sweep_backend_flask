"""Summary: Account Category Metadata Model

An account category metadata model used to convert an account category metadata document into an account category
metadata object
"""


class AccountCategoryMetadata:
    """
    A class to represent an account category metadata model

    Attributes
    ----------
    created_date : datetime
        Account Category's created date
    total_account_category_items : int
        Account Category's total account category items
    updated_date : datetime
        Account Category's updated date
    """

    def __init__(self, account_category_metadata_document) -> None:
        self.created_date = account_category_metadata_document['created_date']
        self.total_account_category_items = account_category_metadata_document['total_account_category_items']
        self.updated_date = account_category_metadata_document['updated_date']
