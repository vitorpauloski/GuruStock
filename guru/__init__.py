import requests
import json

class Session:
    def __init__(self, token):
        self.token = token

    def getMarketData(self, tickers):
        url = 'https://guruapi.com/v1/marketdata'
        params = {'tickers': ','.join(tickers)}
        headers = {'Authorization': f'Bearer {self.token}'}
        request = requests.get(url, params = params, headers = headers)
        if request.status_code == 200:
            request_response = json.loads(request.text)['symbols']
        else:
            request_response = {}
        market_data = {}
        for i in request_response:
            market_data[i['ticker']] = i
        output_list = []
        for i in tickers:
            try:
                a = {
                    'ticker': i,
                    'name': market_data[i]['company'],
                    'close': market_data[i]['close'],
                    'price': market_data[i]['price'],
                    'variation_percent': market_data[i]['variation_percent']
                }
            except:
                a = {
                    'ticker': i,
                    'name': 'ERROR',
                    'close': 'ERROR',
                    'price': 'ERROR',
                    'variation_percent': 'ERROR'
                }
            output_list.append(a)
        return output_list
