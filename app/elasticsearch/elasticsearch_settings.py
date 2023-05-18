"""Summary: Elasticsearch Settings

A module that contains the Elasticsearch settings
"""
from app.models.user.metadata.company_metadata import CompanyMetadata
from app.models.user.service_provider import ServiceProvider


WORKER_INDEX_NAME = 'workers'
COMPANY_INDEX_NAME = 'companies'

WORKER_MAPPING = {
    'properties': {
        'first_name': {'type': 'keyword'},
        'last_name': {'type': 'keyword'},
        'metadata': {'type': 'nested'},
        'service_provider': {'type': 'nested'}
    }
}

COMPANY_MAPPING = {
    'properties': {
        'name': {'type': 'keyword'},
        'metadata': {'type': 'nested', 'properties': CompanyMetadata.__dict__},
        'service_provider': {'type': 'nested', 'properties': ServiceProvider.__dict__}
    }
}
