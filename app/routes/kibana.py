# routes/kibana.py

import requests
from app.config import settings
from fastapi import APIRouter, HTTPException
from app.services.kibana_service import fetch_data_from_kibana, search_data
import httpx


router = APIRouter()

@router.post('/fetch')
def get_kibana_data(query:dict):
    try:
        print(query)
        data = fetch_data_from_kibana(query)
        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/health")
async def kibana_health():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{settings.KIBANA_BASE_URL}/api/status",
                                        auth = (settings.KIBANA_USERNAME, settings.KIBANA_PASSWORD))
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"Kibana API error: {e.response.text}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))





@router.post("/search")
async def search(query: dict):
    index = 1
    query_data = search_data(query)
    print(query_data)

    async with httpx.AsyncClient() as client:

        if not query_data["query"]["bool"]["should"]:
            raise HTTPException(status_code=400, detail="At least one of 'userid', 'trackingid', or 'correlationid' must be provided")

        try:
            response = await client.post(
                f"{settings.KIBANA_BASE_URL}/{index}/_search",
                json=query_data,
                auth=(settings.KIBANA_USERNAME, settings.KIBANA_PASSWORD)  # Include authentication if required
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"Elasticsearch API error: {e.response.text}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

        