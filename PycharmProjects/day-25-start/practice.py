# import csv
# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(type(data)
# print(data['temp'])
# data_dict = data.to_dict()
#
# print(data_dict)

# temp_list = data['temp'].to_list()
# a = data['temp'].max()
# print(a)

# print(data[data.temp == data.temp.max()])
# print(data.condition)

# monday = data[data.day == 'Monday']
# print(monday.condition)
# farengate = (data.temp * (9/5)) + 32
# print(farengate)

# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# ddata = pandas.DataFrame(data_dict)
# ddata.to_csv('new_file.csv')
# print(ddata)


#next challenge
data = pandas.read_csv('Central_Park.csv')
# colors = data['Primary Fur Color']

gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

ddata = pandas.DataFrame(data_dict)
ddata.to_csv('count.csv')

