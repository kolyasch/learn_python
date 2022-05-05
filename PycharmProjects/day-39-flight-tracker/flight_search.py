import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = '2a3RrsKmPg3-Jl-oO5apHf7zY4BX0hrg'
smth = 'https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021'


class FlightSearch:
    def get_destination_code(self, city_name):
        headers = {'apikey': TEQUILA_API_KEY}
        query = {
            'term': city_name,
            'location_types': 'city'
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            headers=headers,
            params=query
        )
        results = response.json()['locations']
        code = results[0]['code']
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {'apikey': TEQUILA_API_KEY}
        query = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_From': from_time,
            'dateTo': to_time,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'CZK'
        }
        response = requests.get(
            url=f'{TEQUILA_ENDPOINT}/v2/search',
            params=query,
            headers=headers
        )
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights found for {destination_city_code}.')
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date=data['route'][1]['local_departure'].split('T')[0]
        )
        print(f'{flight_data.destination_city}: {flight_data.price}Kč')
        return flight_data
