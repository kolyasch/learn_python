import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = '2a3RrsKmPg3-Jl-oO5apHf7zY4BX0hrg'


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
        print(results)
        code = results[0]['code']
        return code
