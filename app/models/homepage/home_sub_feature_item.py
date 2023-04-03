"""Summary: Home sub feature item model

A home sub feature item model used to convert a home sub feature item document into a home sub feature item object

"""


class HomeSubFeatureItem:

    def __init__(self, service_category_item_document: dict) -> None:
        self.title = service_category_item_document['title']
        self.description = service_category_item_document['description']
        self.image = service_category_item_document['image']

    def get_title(self) -> str:
        """
        :return: service category item's active
        """
        return self.title

    def set_title(self, title: str) -> None:
        """
        :param title: service category item's active
        """
        self.title = title

    def get_description(self) -> str:
        """
        :return: service category item's icon
        """
        return self.description

    def set_description(self, description: str) -> None:
        """
        :param description: service category item's icon
        """
        self.description = description

    def get_image(self) -> str:
        """
        :return: service category item's name
        """
        return self.image

    def set_image(self, image: str) -> None:
        """
        :param image: service category item's name
        """
        self.image = image
