"""Summary: Company Metadata Model

A company metadata model used to convert a company metadata document into a company metadata object
"""


class CompanyMetadata:
    """
    A class to represent a company metadata model


    Attributes
    ----------
    number_of_employees : int
        Company's number of employees
    """

    def __init__(self, company_metadata_document: dict) -> None:
        self.number_of_employees = company_metadata_document['number_of_employees']
