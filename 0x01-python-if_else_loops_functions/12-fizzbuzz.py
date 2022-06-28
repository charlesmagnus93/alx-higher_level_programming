#!/usr/bin/python3
def fizzbuzz():
    a = ''
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 != 0):
            a += f'Fizz '
        elif (i % 5 == 0 and i % 3 != 0):
            a += f'Buzz '
        elif (i % 3 == 0 and i % 5 == 0):
            a += f'FizzBuzz '
        else:
            a += f'{str(i)} '
    print(a)
