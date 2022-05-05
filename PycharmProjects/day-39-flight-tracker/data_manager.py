import requests

sheet_url = 'https://api.sheety.co/96b85a69d38d890adf468ad958709c2e/flightDeals/prices'


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(sheet_url)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def testing(self):
        for n in self.destination_data:
            if self.destination_data[n]['iataCode'] == '':
                self.destination_data[n]['iataCode'] = 'TESTING'
        return self.destination_data
