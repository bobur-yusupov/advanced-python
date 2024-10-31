import time
"""
This module demonstrates the use of higher-order functions and decorators in Python.
Functions:
    hello_function(func: Callable[[], None]) -> Callable[[], None]:
        A decorator that prints messages before and after the execution of a function.
    function_to_be_used() -> None:
        A simple function to demonstrate the use of the hello_function decorator.
    calculate_time(func: Callable[..., Any]) -> Callable[..., Any]:
        A decorator that calculates and prints the time taken by a function to execute.
    factorial(num: int) -> None:
        A function to calculate the factorial of a number, decorated with calculate_time.
    add(a: int, b: int) -> int:
        A function that takes two integers as arguments and returns their sum.
"""
import math
from typing import Callable, Any

# A decorator that prints messages before and after the execution of a function
def hello_function(func: Callable[[], None]) -> Callable[[], None]:
    def inner1() -> None:
        print("Hello, this is before func execution\n")
        func()
        print("Hello, this is after execution")
    return inner1

# A simple function to demonstrate the use of the hello_function decorator
def function_to_be_used() -> None:
    print("This function is going to be used!\n")

# Applying the hello_function decorator to function_to_be_used
used = hello_function(function_to_be_used)
used()

# A decorator that calculates and prints the time taken by a function to execute
def calculate_time(func: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args: Any, **kwargs: Any) -> None:
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in:", func.__name__, end - begin)
    return inner

# A function to calculate the factorial of a number, decorated with calculate_time
@calculate_time
def factorial(num: int) -> None:
    print(math.factorial(num))

factorial(10)

# Function with 2 int arguments which returns their sum
def add(a: int, b: int) -> int:
    return a + b
    