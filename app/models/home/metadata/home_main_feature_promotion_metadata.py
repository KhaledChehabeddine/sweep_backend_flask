"""Summary: Home Main Feature Promotion Metadata Model

A home main feature promotion metadata model used to convert a home main feature promotion metadata document into a home
main feature promotion metadata object
"""


class HomeMainFeaturePromotionMetadata:
    """
    A class to represent a home main feature promotion metadata model


    Attributes
    ----------
    total_companies : int
        Home main feature promotion's total companies
    total_service_providers : int
        Home main feature promotion's total service providers (sum of companies and workers)
    total_workers : int
        Home main feature promotion's total workers
    """

    def __init__(self, home_main_feature_promotion_metadata_document: dict) -> None:
        self.total_companies = home_main_feature_promotion_metadata_document['total_companies']
        self.total_service_providers = home_main_feature_promotion_metadata_document['total_service_providers']
        self.total_workers = home_main_feature_promotion_metadata_document['total_workers']
