"""Summary: Account Category Item Metadata Model

An account category item metadata model used to convert an account category item metadata document into an account
category item metadata object
"""


class AccountCategoryItemMetadata:
    """
    A class to represent an account category item metadata model

    Attributes
    ----------
    image_format : str
        Worker's image format
    image_height : int
        Worker's image height
    image_width : int
        Worker's banner image width
    """

    def __init__(self, account_category_item_metadata_document) -> None:
        self.image_format = account_category_item_metadata_document['image_format']
        self.image_height = account_category_item_metadata_document['image_height']
        self.image_width = account_category_item_metadata_document['image_width']
