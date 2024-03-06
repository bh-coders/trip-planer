import logging
from urllib.parse import urlencode

from requests import Session
from requests.exceptions import HTTPError, RequestException

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
        try:
            return self._make_request(url)
        finally:
            self.close()

    def geocode(self, number: str, city: str, county: str, state: str):
        query = f"{number}, {city}, {county}, {state}"
        url = self._get_url("search", q=query.lower())
        try:
            return self._make_request(url)
        finally:
            self.close()

    def _make_request(self, url: str):
        try:
            result = self.session.get(url)
            result.raise_for_status()
            return result.json()
        except HTTPError as e:
            logger.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
            raise
        except RequestException as e:
            logger.error(f"Request error: {e}")
            raise

    def close(self):
        self.session.close()
