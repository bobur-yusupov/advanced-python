# Define two different functions
def shout(text: str) -> str:
    return text.upper()

def whisper(text: str) -> str:
    return text.lower()

def greet(func: object): # Function passed as parameter. Function is the instance of Object type.
    greeting = func("Hi, I am created by function")

    print(greeting)

greet(shout) # Pass shout and whisper as arguments of func paramenter
greet(whisper)