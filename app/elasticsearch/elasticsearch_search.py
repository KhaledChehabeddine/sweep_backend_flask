"""
Summary: Elasticsearch Search Criteria

A set of functions to search for workers and companies based on a given query.
"""
import functools
import time
from app.elasticsearch.elasticsearch_index import es
from app.elasticsearch.elasticsearch_settings import WORKER_INDEX_NAME, COMPANY_INDEX_NAME
from app.models.user.company import Company
from app.models.user.worker import Worker


def cache(expiration_time):
    """
    Cache decorator to cache function results for a specified expiration time.

    :param expiration_time: The expiration time in seconds for the cache.
    :return: A decorator function.
    """
    cache_dict = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if args in cache_dict and time.time() - cache_dict[args][0] < expiration_time:
                return cache_dict[args][1]
            result = func(*args)
            cache_dict[args] = (time.time(), result)
            return result

        return wrapper

    return decorator


@cache(expiration_time=3600)  # Set the expiration time to 1 hour (3600 seconds)
def search_workers(query) -> list:
    """
    :param query: a query to be used to search for workers
    :return: A list of workers that match the given query
    """
    body = {
        "query": {
            "bool": {
                "should": [
                    {
                        "multi_match": {
                            "query": query,
                            "fields": ["first_name^2", "last_name^2"],
                            "fuzziness": "2",
                            "prefix_length": 2
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "first_name": {
                                "query": query,
                                "boost": 1
                            }
                        }
                    }
                ]
            }
        }
    }

    res = es.search(index_name=WORKER_INDEX_NAME, body=body)

    workers = res.get("hits", {}).get("hits", [])
    worker_documents = [hit.get("_source", {}) for hit in workers]
    workers = [Worker(worker_document) for worker_document in worker_documents]

    return workers


@cache(expiration_time=3600)
def search_companies(query: str) -> list:
    """
    Search for companies that match the given query based on the name attribute.

    :param query: The search query.
    :return: A list of companies that match the query.
    """
    body = {
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "name": {
                                "query": query,
                                "boost": 2,
                                "fuzziness": "AUTO"
                            }
                        }
                    },
                    {
                        "prefix": {
                            "name": {
                                "value": query,
                                "boost": 1
                            }
                        }
                    },
                    {
                        "wildcard": {
                            "name": {
                                "value": f"*{query.lower()}*",
                                "boost": 0.5
                            }
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "name": {
                                "query": query,
                                "boost": 0.1
                            }
                        }
                    }
                ]
            }
        }
    }

    res = es.search(index_name=COMPANY_INDEX_NAME, body=body)

    companies = res.get("hits", {}).get("hits", [])
    company_documents = [hit.get("_source", {}) for hit in companies]

    filtered_companies = []
    for company_document in company_documents:
        name = company_document.get("name", "")
        if query.lower() in name.lower():
            filtered_companies.append(Company(company_document))

    return filtered_companies


@cache(expiration_time=3600)  # Set the expiration time to 1 hour (3600 seconds)
def search(query) -> tuple[list[Company], list[Worker]]:
    """
    :param query: a query to be used to search for companies and workers
    :return: A tuple containing a list of companies and a list of workers that match the given query
    """
    return search_companies(query), search_workers(query)
