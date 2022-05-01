print ('Welcome to the rollercoaster!')
height = int(input('What is ypor hieght in cm? '))
if height >= 120:
    print ('You can ride the rollercoaster!')
    age=int(input('What is ypur age? '))
    if age <12:
        bill = 5
        print ('Child tickets are 5$.')
    elif age <= 18:
        bill = 7
        print ('Youth tickets are 7$.')
    else:
        bill = 12
        print('Adult tickets are 12$.')
    photo = input('Do you want a photo taken? Y or N. ')
    if photo == 'Y':
        #add 3$ to their bill
        bill += 3
    print(f'Your final bill is {bill}$.')
else:
    print ('Sorry, you have to grow taller before you can ride.')