import logging
from elasticsearch.helpers import bulk
import elasticsearch.exceptions
from app.elasticsearch.elasticsearch_client import get_elasticsearch_client
from app.elasticsearch.elasticsearch_settings import WORKER_INDEX_NAME, COMPANY_INDEX_NAME

es = get_elasticsearch_client()


def create_indices():
    if not es.indices.exists(index=WORKER_INDEX_NAME):
        try:
            es.indices.create(index=WORKER_INDEX_NAME, ignore=400)
            logging.info("Elasticsearch index %s created", WORKER_INDEX_NAME)
        except elasticsearch.exceptions.BadRequestError as e:
            logging.error("Failed to create Elasticsearch index %s: %s", WORKER_INDEX_NAME, e)
    else:
        print(f"Elasticsearch index {WORKER_INDEX_NAME} already exists")

    if not es.indices.exists(index=COMPANY_INDEX_NAME):
        try:
            es.indices.create(index=COMPANY_INDEX_NAME, ignore=400)
            logging.info("Elasticsearch index %s created", COMPANY_INDEX_NAME)
        except elasticsearch.exceptions.BadRequestError as e:
            logging.error("Failed to create Elasticsearch index %s: %s", COMPANY_INDEX_NAME, e)
    else:
        print(f"Elasticsearch index {COMPANY_INDEX_NAME} already exists")


def index_workers(workers):
    """
    Indexes the given list of workers in Elasticsearch.

    :param workers: A list of Worker objects to be indexed.
    :return: None
    """
    actions = [
        {
            "_index": WORKER_INDEX_NAME,
            "_id": worker['_id'],
            "_source": {
                "first_name": worker.first_name,
                "last_name": worker.last_name,
                "company_id": worker.company_id
            }
        }
        for worker in workers
    ]

    bulk(es, actions)


def index_companies(companies):
    """
    Indexes the given list of companies in Elasticsearch.

    :param companies: A list of Company objects to be indexed.
    :return: None
    """
    actions = [
        {
            "_index": COMPANY_INDEX_NAME,
            "_id": company['_id'],
            "_source": {
                "name": company.name,
                "service_category_ids": company.service_category_ids
            }
        }
        for company in companies
    ]

    bulk(es, actions)

