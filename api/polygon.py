import datetime
import requests


class polygon:
    def get_symbol_data(self,symbol,attr):
        api_key = "mS4aLtwtpr_hgp7cDGBjZmpfBCBHq6Wi"
        url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/{attr['gap']}/{attr['time_unit']}/{attr['start_date']}/{attr['end_date']}?apiKey={api_key}'

        data_for_app = []
        r = requests.get(url)
        data_from_api = r.json()
        print(data_from_api)
        if len(str(data_from_api)) > 1000:
            for result in data_from_api['results']:
                time = datetime.datetime.fromtimestamp(result['t'] / 1000, datetime.UTC)
                time_price = {'time': time.strftime("%m-%d \n %H:%M"),
                              'price': result['c']}
                data_for_app.append(time_price)
            return data_for_app
        else:
            raise Exception("Error retrieving data")