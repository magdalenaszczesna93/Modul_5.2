from faker import Faker
fake = Faker()

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

def card():
    list=[]
    for i in range(1000):
        list.append(name = fake.name(
            first_name = fake.first_name, 
            last_name = fake.last_name, 
            phone_number = fake.phone_number, 
            email = fake.email))
    return list

print(card())