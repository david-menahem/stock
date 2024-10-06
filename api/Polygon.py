import datetime
import os

import requests


class Polygon:
    API_KEY = os.getenv("API_KEY")

    def get_symbol_data(self, symbol, attr):
        url = (f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/{attr.gap}/{attr.time_unit}/'
               f'{attr.start_date}/{attr.end_date}?apiKey={self.API_KEY}')
        r = requests.get(url)
        data_from_api = r.json()
        print(data_from_api)
        if len(str(data_from_api)) > 1000:
            return data_from_api
        else:
            raise Exception("Error retrieving data")

    @staticmethod
    def get_results(data_from_api):
        data_for_app = []
        for result in data_from_api['results']:
            time = datetime.datetime.fromtimestamp(result['t'] / 1000, datetime.UTC)
            time_price = {'time': time.strftime("%m-%d \n %H:%M"),
                          'price': result['c']}
            data_for_app.append(time_price)
        return data_for_app