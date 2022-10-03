import logging
from typing import Optional

import requests

logger = logging.getLogger(__file__)


class SWClient:
    def __init__(self):
        self.session = requests.Session()

    def fetch(self, url: str) -> requests.Response:
        logger.info("Fetching url: %s ")
        return self.session.get(url)


class SWRepository:

    PLANETS = "planets"
    PEOPLE = "people"

    def __init__(self):
        self.client = SWClient()
        self.base_url = "http://swapi:5000/api"

    def get_all_entities(self, module: str, format: Optional[callable] = None):
        next_page = f"{self.base_url}/{module}"
        entities = []
        while next_page:
            response = self.client.fetch(next_page).json()
            if format:
                res = format(results=response["results"])
                entities.extend(res)
            else:
                entities.extend(response["results"])
            next_page = response["next"]

        return entities
