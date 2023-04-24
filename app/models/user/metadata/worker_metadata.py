"""Summary: Worker Metadata Model

A worker metadata model used to convert a worker metadata document into a worker metadata object
"""


class WorkerMetadata:
    """
    A class to represent a worker metadata model


    Attributes
    ----------
    formatted_name : str
        Worker's formatted name
    """

    def __init__(self, worker_metadata_document: dict) -> None:
        self.formatted_name = worker_metadata_document['formatted_name']
