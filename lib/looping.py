#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    if i == 0:
        print("Happy New Year!")

def square_integers(int_list):
    squares = [num * num for num in int_list]
    return squares

def fizzbuzz():
    def fb(num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return str(num)

    for num in range(1, 101):
        print(fb(num))
