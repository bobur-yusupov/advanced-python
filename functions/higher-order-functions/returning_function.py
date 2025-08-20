def create_adder(x: int) -> object: # this function returns object instance
    def adder(y: int): # a function created inside create_adder
        return x + y

    return adder # returned the created function

add_15 = create_adder(15)
print(add_15(10)) # 15
