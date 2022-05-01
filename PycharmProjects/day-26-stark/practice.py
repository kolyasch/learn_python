# name = ['Alex', 'Beth', 'Caroline']
# letter_list = [huj.upper() for huj in name if len(huj) > 4]
# print(letter_list)
##########2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# squared_numbers = [n**2 for n in numbers]
# #Write your code 👆 above:
#
# print(squared_numbers)
##############3
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
# result = [n for n in numbers if n % 2 == 0]
# #Write your code 👆 above:
#
# print(result)
############4
# with open('file1.txt') as file_1:
#     data_1 = file_1.readlines()
# with open('file1.txt') as file_2:
#     data_2 = file_2.readlines()
# b = [int(n) for n in data_2 if n in data_1]
# b.sort(reverse=True)
# # Write your code above 👆
#
# print(b)
########5
# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {n: random.randint(1, 100) for n in names}
# passed_students = {key: value for (key, value) in students_score.items() if value > 60}
# print(passed_students)

##########6
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word : len(word) for word in sentence.split()}
#
#
# print(result)

############7
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {a: ((b * 9/5)+32) for a, b in weather_c.items()}
#
#
# print(weather_f)

############7

import pandas
student_dict = {
    'students': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.students == 'Angela':
        print(f'Angela has {row.score} scores')

