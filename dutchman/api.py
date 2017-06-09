
import logging
import requests
import json

logger = logging.getLogger(__name__)


class Kraken(object):
    api_endpoint = 'https://api.kraken.com/0/{platform}/{cls}'

    def __init__(self):
        self._request_params = {}
        self.data = None

    def _get(self, **kwargs):
        url = Kraken.api_endpoint.format(
            platform=self.platform(), cls=self.__class__.__name__)
        logger.info("Requesting: {}", url)
        return self.request_method()(url, params=kwargs)

    def request(self, pretty_string=False):
        resp = self._get(**self._request_params)
        j = resp.json()
        if j['error']:
            logger.error("Error when requesting {}:\n\t{}", resp.url, '\n\t'.join(j['error']))
        result = j.get('result', None)
        if pretty_string and result:
            return json.dumps(result, indent=2, sort_keys=True)
        elif result:
            return result
        return None

    def load(self):
        self.data = self.request()
        return self


class Public(Kraken):
    @staticmethod
    def platform():
        return 'public'

    @staticmethod
    def request_method():
        return requests.get


class Ticker(Public):
    pass


class AssetPairs(Public):
    def __init__(self, pair_name=None):
        super(AssetPairs, self).__init__()
        if pair_name is not None:
            self._request_params['pair'] = pair_name


