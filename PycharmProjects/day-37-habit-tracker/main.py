import requests
from datetime import date

today = date.today()
today = today.strftime('%Y%m%d')

TOKEN = 'feitk1nlet13h1iont1'
USERNAME = 'kolyasha'
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Reading Graph',
    'unit': 'Pages',
    'type': 'int',
    'color': 'shibafu'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

input_function = input('How many pages did you read today? ')

smth_config = {
    'date': today,
    'quantity': input_function
}
pixel_creation_endpoint = f'{graph_endpoint}/{GRAPH_ID}/{today}'
response1 = requests.put(url=pixel_creation_endpoint, json=smth_config, headers=headers)
print(response1.text)

