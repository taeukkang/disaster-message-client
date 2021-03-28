import urllib.parse
import urllib.request
import json


class DisasterMessageClient(object):
    def __init__(self, **options):
        self.service_key = options.get('service_key')
        self.baseUrl = 'http://apis.data.go.kr/1741000/DisasterMsg2/'

    def _get(self, url):
        if not url:
            raise ValueError('A URL is required')

        with urllib.request.urlopen(url) as response:
            raw_data = response.read()

        json_data = json.loads(raw_data.decode('utf-8'))

        return json_data

    def get_disaster_message_list(self, page, rows):
        data = {'pageNo': page, 'numOfRows': rows, 'type': 'json',
                'flag': 'Y', 'ServiceKey': self.service_key}
        url_values = urllib.parse.urlencode(data)

        url = urllib.parse.urljoin(
            self.baseUrl, 'getDisasterMsgList' + '?' + url_values)
        print(url)

        return self._get(url)
