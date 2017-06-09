
import requests
import json

class Kraken(object):
    api_endpoint = 'https://api.kraken.com/0/{platform}/{cls}'
    
    def _get(self, **kwargs):
        url = Kraken.api_endpoint.format(
            platform=self.platform(), cls=self.__class__.__name__)
        print("Requesting: {}".format(url))
        return self.request_method()(url, params=kwargs)

    def request(self, **kwargs):
        resp = self._get(**kwargs)
        j = resp.json()
        if j['error']:
            print('Error for request: {}'.format(resp.url))
        return j

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
    pass

def main():
    print(AssetPairs().request())

if __name__ == '__main__':
    main()

