"""Summary: Home Sub Feature Metadata Model

A home sub feature metadata model used to convert a home sub feature metadata document into a home sub feature
metadata object
"""


class HomeSubFeatureMetadata:
    """
    A class to represent a home sub feature metadata model


    Attributes
    ----------
    total_companies : int
        Home sub feature's total companies
    total_service_providers : int
        Home sub feature's total service providers (sum of companies and workers)
    total_workers : int
        Home sub feature's total workers
    """

    def __init__(self, home_sub_feature_metadata_document: dict) -> None:
        self.total_companies = int(home_sub_feature_metadata_document['total_companies'])
        self.total_service_providers = int(home_sub_feature_metadata_document['total_service_providers'])
        self.total_workers = int(home_sub_feature_metadata_document['total_workers'])
