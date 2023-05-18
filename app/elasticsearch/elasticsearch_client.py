"""Summary: Elasticsearch Client

Description: A client class for connecting to Elasticsearch and performing operations such as creating an index,
deleting an index, and performing search operations.
"""
import logging
import os
from base64 import b64encode

from elasticsearch import Elasticsearch, ConnectionError, NotFoundError

es_logger = logging.getLogger('elasticsearch')
es_logger.setLevel(logging.ERROR)


def get_elasticsearch_client():
    """
    :return: an Elasticsearch client
    """
    es_url = os.environ.get("ES_URL")
    es_username = os.environ.get("ES_USERNAME")
    es_password = os.environ.get("ES_PASSWORD")
    es_client = ElasticsearchClient(es_url, es_username, es_password)
    return es_client


def _create_basic_auth_header(username, password):
    """
    :param username: the username to be used for basic authentication
    :param password: the password to be used for basic authentication
    :return: a base64 encoded string of the username and password
    """
    credentials = "%s:%s" % (username, password)
    credentials_bytes = credentials.encode("utf-8")
    credentials_base64 = b64encode(credentials_bytes).decode("utf-8")
    return credentials_base64


class ElasticsearchClient:
    """
    Elasticsearch client class for connecting to Elasticsearch
    """

    def __init__(self, url, username, password, api_key=None, timeout=30):
        """
        :param url: the url of the Elasticsearch instance
        :param username: the username to be used for basic authentication
        :param password: the password to be used for basic authentication
        :param api_key: the api key to be used for api key authentication
        :param timeout: the timeout to be used for the Elasticsearch client
        :return: an Elasticsearch client instance
        """
        self.url = url
        self.username = username
        self.password = password
        self.api_key = api_key
        self.timeout = timeout

        try:
            headers = {}
            if api_key:
                headers["Authorization"] = "ApiKey %s" % api_key
            else:
                headers["Authorization"] = "Basic %s" % _create_basic_auth_header(username, password)

            self.client = Elasticsearch(
                [url],
                headers=headers,
                timeout=timeout
            )

            if not self.client.ping():
                raise ConnectionError("Failed to ping Elasticsearch at %s" % url)
        except Exception:
            logging.error("Failed to connect to Elasticsearch at %s: %s", url, Exception)
            raise

    def create_index(self, index_name, body):
        """
        :param index_name: the name of the index to be created
        :param body: the body of the index to be created
        :return: logs the result of the create operation
        """
        try:
            self.client.indices.create(index=index_name, body=body)  # Update the method call
            logging.info("Elasticsearch index %s created", index_name)
        except Exception as e:
            logging.error("Failed to create Elasticsearch index %s: %s", index_name, e)

    def delete_index(self, index_name):
        """
        :param index_name: the name of the index to be deleted
        :return: logs the result of the delete operation
        """
        try:
            self.client.indices.delete(index=index_name)
            logging.info("Elasticsearch index %s deleted", index_name)
        except NotFoundError:
            logging.info("Elasticsearch index %s not found", index_name)
        except Exception as e:
            logging.error("Failed to delete Elasticsearch index %s: %s", index_name, e)

    def search(self, index_name, body):
        """
        :param index_name: the name of the index to be searched
        :param body: the body of the search query
        :return: the result of the search operation
        """
        try:
            res = self.client.search(index=index_name, body=body)
            return res
        except Exception as e:
            logging.error("Failed to perform search in Elasticsearch index %s: %s", index_name, e)
            return None

    def delete(self, index_name, id_):
        """
        Delete a document from the Elasticsearch index.

        :param index_name: The name of the index
        :param id_: The id of the document to be deleted
        :return: True if the document was successfully deleted, False otherwise
        """
        try:
            self.client.delete(index=index_name, id=id_)
            return True
        except NotFoundError:
            logging.info("Document with id %s not found in Elasticsearch index %s", id_, index_name)
            return False
        except Exception as e:
            logging.error("Failed to delete document from Elasticsearch index %s: %s", index_name, e)
            return False
