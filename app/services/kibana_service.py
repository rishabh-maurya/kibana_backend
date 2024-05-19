# app/services/kibana_services

import requests
from app.config import settings
import httpx

def fetch_data_from_kibana(query: dict):
    # url = f"{settings.KIBANA_BASE_URL}/elasticsearch/{settings.KIBANA_INDEX}/_search"
    # response = requests.post(url, json=query)
    # response.raise_for_status()
    # return response.json()
    dummy_response =  {"status": 200, "data": [1, 2, 3, 4, 5]}
    return dummy_response

def search_data(query_data:dict):
    query = {
        "query": {
            "bool": {
                "should": [],
                "minimum_should_match": 1
            }
        }
    }
    
    if query_data['userid']:
        query["query"]["bool"]["should"].append({"match": {"userid": query_data['userid']}})
    if query_data['trackingid']:
        query["query"]["bool"]["should"].append({"match": {"trackingid": query_data['trackingid']}})
    if query_data['correlationid']:
        query["query"]["bool"]["should"].append({"match": {"correlationid": query_data['correlationid']}})

    return query