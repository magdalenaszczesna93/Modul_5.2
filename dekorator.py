from faker import Faker
fake = Faker()

from datetime import time
t=time()

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

class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


def card():
        list=[]
        for i in range(1000):
            list.append(Contact(
                first_name = fake.first_name(), 
                last_name = fake.last_name(), 
                phone_number = fake.phone_number(), 
                email = fake.email()))
        return list
print(card())