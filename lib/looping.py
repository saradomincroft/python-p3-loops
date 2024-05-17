#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter <= 10 and counter >0 :
        print(f"{counter}")
        counter -= 1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    print([x ** 2 for x in int_list])
    return [x ** 2 for x in int_list]
    
square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()

