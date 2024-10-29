import time
import math

def hello_function(func: object) -> object:
    def inner1():
        print("Hello, this is befor func execution\n")

        func()

        print("Hello, this is after execution")

    return inner1

def function_to_be_used():
    print("This function is going to be used!\n")

used = hello_function(function_to_be_used)

used()

def calculate_time(func: object):
    def inner(*args, **kwargs):

        begin = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("Total time taken in: ", func.__name__, end - begin)

    return inner

@calculate_time
def factorial(num):
    print(math.factorial(num))

factorial(10)