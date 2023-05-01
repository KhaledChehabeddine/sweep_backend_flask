"""Summary: Worker Metadata Model

A worker metadata model used to convert a worker metadata document into a worker metadata object
"""


class WorkerMetadata:
    """
    A class to represent a worker metadata model


    Attributes
    ----------
    banner_image_format : str
        Worker's banner image format
    banner_image_height : int
        Worker's banner image height
    banner_image_width : int
        Worker's banner image width
    formatted_name : str
        Worker's formatted name
    profile_image_format : str
        Worker's profile image format
    profile_image_height : int
        Worker's profile image height
    profile_image_width : int
        Worker's profile image width
    """

    def __init__(self, worker_metadata_document: dict) -> None:
        self.banner_image_format = str(worker_metadata_document['banner_image_format'])
        self.banner_image_height = int(worker_metadata_document['banner_image_height'])
        self.banner_image_width = int(worker_metadata_document['banner_image_width'])
        self.formatted_name = str(worker_metadata_document['formatted_name'])
        self.profile_image_format = str(worker_metadata_document['profile_image_format'])
        self.profile_image_height = int(worker_metadata_document['profile_image_height'])
        self.profile_image_width = int(worker_metadata_document['profile_image_width'])
