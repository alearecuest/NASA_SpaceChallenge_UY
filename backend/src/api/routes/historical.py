from fastapi import APIRouter, Depends, HTTPException, Query
from services import get_historical_service, HistoricalDataService
from models import HistoricalEventsResponse, HistoricalEvent

router = APIRouter()

@router.get("/events/search", response_model=HistoricalEventsResponse)
async def search_historical_events(
    query: str = Query(..., description="Search term (e.g., 'dinosaurs', 'Tunguska', 'Russia')"),
    historical_service: HistoricalDataService = Depends(get_historical_service)
):
    """
    Search historical events by keywords.
    
    Examples:
    - 'dinosaurs': Finds the K-Pg extinction event
    - 'russia': Finds Tunguska and Chelyabinsk events  
    - 'crater': Finds events with impact craters
    """
    return await historical_service.search_events(query)

@router.get("/events/{event_id}", response_model=HistoricalEvent)
async def get_historical_event(
    event_id: int,
    historical_service: HistoricalDataService = Depends(get_historical_service)
):
    """
    Get specific historical event by ID.
    
    Available IDs:
    - 1: Dinosaur Extinction (Chicxulub)
    - 2: Tunguska Event (1908)
    - 3: Chelyabinsk Event (2013) 
    - 4: Barringer Crater (50,000 years ago)
    - 5: Eastern Mediterranean Event (12,800 years ago)
    - 6: Vredefort Impact (2 billion years ago)
    - 7: Sikhote-Alin Impact (1947)
    """
    event = await historical_service.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Historical event not found")
    return event

@router.get("/events", response_model=HistoricalEventsResponse)
async def get_historical_events(
    historical_service: HistoricalDataService = Depends(get_historical_service)
):
    """
    Get all important historical events related to asteroids.
    
    Includes significant impacts that have shaped Earth's history.
    """
    return await historical_service.get_all_events()
