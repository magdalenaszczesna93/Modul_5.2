

def say_louder(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@say_louder
def say_hello():
    greeting = "Hello stranger !"
    return greeting
    
print(say_hello())

