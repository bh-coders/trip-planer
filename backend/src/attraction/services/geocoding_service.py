import logging
from urllib.parse import urlencode

from requests import Session

from src.core.configs import GEOCODES_CO_API_KEY

logger = logging.getLogger(__name__)


class MapsCoService:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key if api_key else GEOCODES_CO_API_KEY
        self.base_url = "https://geocode.maps.co/"
        self.session = Session()

    def _get_url(self, endpoint: str, **params):
        params["api_key"] = self.api_key
        return self.base_url + endpoint + "?" + urlencode(params)

    def reverse_geocode(self, lat: float, lng: float):
        url = self._get_url("reverse", lat=lat, lon=lng)
        return self._make_request(url)

    def geocode(self, number: str, city: str, county: str, state: str):
        query = f"{number}, {city}, {county}, {state}"
        url = self._get_url("search", q=query.lower())
        return self._make_request(url)

    def _make_request(self, url: str):
        result = self.session.get(url)
        if result.status_code == 200:
            return result.json()
        else:
            error_msg = f"Error {result.status_code}: {result.text}"
            logger.error(error_msg)
            raise Exception(error_msg)
        self.close()

    def close(self):
        self.session.close()
