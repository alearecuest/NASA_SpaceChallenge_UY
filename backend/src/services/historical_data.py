from models import HistoricalEvent, HistoricalEventsResponse
from typing import List, Optional

class HistoricalDataService:
    def __init__(self):
        self.events = self._load_historical_events()
    
    def _load_historical_events(self) -> List[HistoricalEvent]:
        """Load important historical asteroid impact events"""
        return [
            HistoricalEvent(
                id=1,
                title="Dinosaur Extinction - K-Pg Event",
                description="The impact of an asteroid approximately 10-15 km in diameter caused the Cretaceous-Paleogene mass extinction, eliminating 75% of species, including non-avian dinosaurs.",
                year="66 million years BC",
                impact_location="Yucatán Peninsula, Mexico",
                asteroid_size="10-15 km in diameter",
                scientific_evidence="Chicxulub crater (180 km diameter), global iridium layer, global tsunamis",
                consequences=[
                    "Extinction of 75% of terrestrial and marine species",
                    "End of the dinosaur era", 
                    "Opening of ecological niches for mammals",
                    "Global nuclear winter for decades"
                ],
                references=[
                    "Alvarez, L. W. (1980). Extraterrestrial cause for the Cretaceous–Tertiary extinction",
                    "NASA Earth Observatory - Chicxulub Impact Event",
                    "Science Magazine - The Chicxulub Asteroid Impact and Mass Extinction"
                ]
            ),
            HistoricalEvent(
                id=2,
                title="Tunguska Event",
                description="A massive aerial explosion caused by a meteoroid that exploded in the atmosphere, flattening 2,150 km² of forest in Siberia.",
                year="1908",
                impact_location="Podkamennaya Tunguska River, Siberia, Russia",
                asteroid_size="50-80 meters (estimated)",
                scientific_evidence="Trees flattened in radial pattern, globally recorded shock wave, bright nights in Europe",
                consequences=[
                    "2,150 km² of forest devastated",
                    "Shock wave equivalent to 10-15 megatons of TNT",
                    "Charred trees at the epicenter",
                    "Witnesses reported 'sky split in two'"
                ],
                references=[
                    "NASA - The Tunguska Impact",
                    "Russian Academy of Sciences reports", 
                    "Royal Astronomical Society papers"
                ]
            ),
            HistoricalEvent(
                id=3,
                title="Chelyabinsk Event",
                description="The most significant meteor impact in modern times, causing extensive damage and over 1,500 injuries from the shock wave.",
                year="2013", 
                impact_location="Chelyabinsk, Russia",
                asteroid_size="17-20 meters",
                scientific_evidence="Extensive video material, recovered fragments (Chelyabinsk meteorite), infrasound data",
                consequences=[
                    "1,500+ people injured (mainly from broken glass)",
                    "Damage to 7,200 buildings", 
                    "Shock wave equivalent to 500 kilotons of TNT",
                    "Recovered meteorite fragments"
                ],
                references=[
                    "NASA - Chelyabinsk Meteor",
                    "Science Magazine - Chelyabinsk Airburst",
                    "Russian Geophysical Committee reports"
                ]
            ),
            HistoricalEvent(
                id=4,
                title="Barringer Crater (Meteor Crater)",
                description="One of the best-preserved impact craters on Earth, formed by a metallic meteorite.",
                year="50,000 years ago",
                impact_location="Arizona, United States",
                asteroid_size="50 meters (iron-nickel)",
                scientific_evidence="1.2 km diameter crater, iron-nickel meteorite fragments, coesite and stishovite",
                consequences=[
                    "1.2 km diameter crater, 170 m deep",
                    "Instant destruction of everything within 10 km radius",
                    "Shock wave equivalent to 10 megatons",
                    "Exceptional preservation due to arid climate"
                ],
                references=[
                    "Barringer Crater Company",
                    "US Geological Survey studies",
                    "Meteoritical Society papers"
                ]
            ),
            HistoricalEvent(
                id=5,
                title="Eastern Mediterranean Event", 
                description="Possible cosmic impact that may have contributed to abrupt climate changes during the Younger Dryas.",
                year="12,800 years ago",
                impact_location="Eastern Mediterranean / Greenland",
                asteroid_size="4-5 km (estimated)",
                scientific_evidence="Nanodiamonds, impact spherules, charcoal layer, abrupt climate changes",
                consequences=[
                    "Possible contribution to Younger Dryas (global cooling)",
                    "Extinction of North American megafauna",
                    "Changes in early human civilizations", 
                    "Anomalous platinum deposits"
                ],
                references=[
                    "Scientific Reports - Evidence for Cosmic Impact",
                    "PNAS - Younger Dryas Impact Hypothesis",
                    "Geology Journal papers"
                ]
            ),
            HistoricalEvent(
                id=6,
                title="Vredefort Impact",
                description="The largest verified impact crater on Earth, formed by an enormous asteroid during the Paleoproterozoic Era.",
                year="2.023 billion years ago",
                impact_location="Free State Province, South Africa",
                asteroid_size="10-15 km (estimated)",
                scientific_evidence="300 km diameter crater structure, shatter cones, impact breccias, shocked quartz",
                consequences=[
                    "Formation of 300 km diameter crater",
                    "Global environmental changes",
                    "Release of massive energy (>100 million megatons)",
                    "Significant geological and biological impacts"
                ],
                references=[
                    "Geological Society of South Africa",
                    "Nature - Vredefort Impact Structure",
                    "Earth and Planetary Science Letters"
                ]
            ),
            HistoricalEvent(
                id=7,
                title="Sikhote-Alin Impact",
                description="One of the largest observed meteorite falls in history, with an iron meteorite that created numerous craters.",
                year="1947",
                impact_location="Sikhote-Alin Mountains, Russia", 
                asteroid_size="1-2 meters (iron meteorite)",
                scientific_evidence="Over 100 impact craters, 23 tons of recovered fragments, eyewitness accounts",
                consequences=[
                    "Creation of 106 impact craters",
                    "23 tons of meteorite fragments recovered",
                    "Bright fireball observed in daylight",
                    "Extensive scientific study opportunity"
                ],
                references=[
                    "Russian Academy of Sciences",
                    "Meteoritical Bulletin",
                    "Smithsonian Institution collections"
                ]
            )
        ]
    
    async def get_all_events(self) -> HistoricalEventsResponse:
        """Get all historical events"""
        return HistoricalEventsResponse(
            events=self.events,
            total_events=len(self.events)
        )
    
    async def get_event_by_id(self, event_id: int) -> Optional[HistoricalEvent]:
        """Get specific historical event by ID"""
        for event in self.events:
            if event.id == event_id:
                return event
        return None
    
    async def search_events(self, query: str) -> HistoricalEventsResponse:
        """Search events by keywords"""
        query_lower = query.lower()
        filtered_events = [
            event for event in self.events
            if (query_lower in event.title.lower() or 
                query_lower in event.description.lower() or
                query_lower in event.impact_location.lower())
        ]
        return HistoricalEventsResponse(
            events=filtered_events,
            total_events=len(filtered_events)
        )

async def get_historical_service():
    return HistoricalDataService()
