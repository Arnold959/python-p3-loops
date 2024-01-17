#!/usr/bin/env python3
def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def fizzbuzz():
   for  num in range (1,101):
       if num % 3 == 0 and num % 5 == 0:
           print ("FizzBuzz")
       elif num % 3 == 0:
           print ("Fizz")
       elif num % 5 == 0:
           print ( "Buzz")
       else :
           print (num)

def square_integers (int_list):
    square_list = [num**2 for num in int_list]
    return square_list

def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str


