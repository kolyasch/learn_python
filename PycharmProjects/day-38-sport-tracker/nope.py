def add(sum=0, *args):
    for n in args:
        sum += n
    return sum


print(add(3, 4, 6, 1111))

