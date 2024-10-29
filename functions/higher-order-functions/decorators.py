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