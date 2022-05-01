def add(sum=0, *args):
    for n in args:
        sum += n
    return sum
add(3, 4, 6, 1111)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
calculate(2, add=3,  multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')
my_car = Car(make='Nissan', model='GT')
print(my_car.make, my_car.model)
