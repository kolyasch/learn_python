import requests

sheet_url = 'https://api.sheety.co/2042acd42e8d3c73c73f38b9d9cca344/flightDeals/prices'


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_url)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{sheet_url}/{city['id']}",
                json=new_data
            )
            print(response.text)
