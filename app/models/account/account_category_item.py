"""Summary: Account Category Item Model

An account category item model used to convert an account category item document into an account category item object
"""
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.models.account.metadata.account_category_item_metadata import AccountCategoryItemMetadata


class AccountCategoryItem:
    """
    A class to represent an account category item model


    Attributes
    ----------
    image_path : str
        Account category item's file path
    image_url : str
        Account category item's image url
    metadata : dict
        Account category item's metadata document
    name : str
        Account category item's name
    """

    def __init__(self, account_category_item_document: dict) -> None:
        self.image_path = account_category_item_document['image_path']
        self.image_url = create_cloudfront_url(file_path=self.image_path)
        self.metadata = AccountCategoryItemMetadata(account_category_item_document['metadata']).__dict__
        self.name = account_category_item_document['name']

    def database_dict(self) -> dict:
        """
        :return: Account category item's dictionary for creating a document (without _id and image_url)
        """
        return {
            'image_path': self.image_path,
            'image_url': self.image_url,
            'metadata': self.metadata,
            'name': self.name
        }
