#Ćwiczenie
#Napisz funkcję, która tworzy listę zawierającą 1000 wizytówek z losowymi danymi 
# (użyj biblioteki faker, którą opisywaliśmy w tym module).

#Następnie stwórz dekorator, który zmierzy czas wykonywania tej operacji. 
# Niech udekorowana funkcja wyświetla czas obliczeń (w sekundach) po ich zakończeniu.

#Wskazówka. W Pythonie do operacji na datach i czasie wykorzystuje się moduł datetime. 
# Zapoznaj się z jego dokumentacją.


from faker import Faker
fake = Faker()

import time

class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    def __str__ (self):
        return f'{self.first_name} {self.last_name} {self.phone_number} {self.email}'
    __repr__ = __str__

def czas_obliczen(func):    
    def obliczenie():
        t0 = time.time()      
        result = func()
        t1 = time.time() - t0
        print("Time elapsed: {:.2f}".format(t1))
        return result            
    return obliczenie    
    
            
@czas_obliczen
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