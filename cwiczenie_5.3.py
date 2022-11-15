from faker import Faker
person = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    def __str__ (self):
        return f'{self.first_name} {self.last_name} {self.phone_number} {self.email}'
    __repr__ = __str__
  
    def contact(self):
        return f'Wybiaram numer {self.phone_number} i dzownię do {self.first_name} {self.last_name}'

    @property
    def label_lenght(self):
        return len(f"{self.first_name} {self.last_name}")

Katherine = BaseContact(first_name='Katherine', last_name='Wade', phone_number= '+1 707-645-2247', email='daniel38@example.net')
Susan = BaseContact(first_name='Susan', last_name='Frank', phone_number= '+1 803-370-5903', email='kellygreen@example.net')
Benjamin = BaseContact(first_name='Benjamin', last_name='Peters', phone_number= '+1 503-435-8432', email='leejacob@example.org')
April = BaseContact(first_name='April', last_name='Johnson', phone_number= '+1 906-563-8043', email='aallen@example.net')
Derrick = BaseContact(first_name='Derrick', last_name='Miller', phone_number= '+1 313-831-2818', email='christopher65@example.net')

class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone = business_phone
    def __str__ (self):
        return f'{self.first_name} {self.last_name} {self.phone_number} {self.email} {self.job} {self.company} {self.business_phone}'
    __repr__ = __str__
  
    def contact(self):
        return f'Wybiaram numer slozbowy {self.business_phone} i dzownię do {self.first_name} {self.last_name}'
    
    @property
    def label_lenght(self):
        return len(f"{self.first_name} {self.last_name}")
    

Katherine = BusinessContact(first_name='Katherine', last_name='Wade', phone_number= '+1 707-645-2247', email='daniel38@example.net', job='Personal assistant', company = 'Mikro Designs', business_phone= '+34 783 832 801')
Susan = BusinessContact(first_name='Susan', last_name='Frank', phone_number= '+1 803-370-5903', email='kellygreen@example.net', job='Information systems manager', company = 'Practi-Plan', business_phone= '+34 622 795 400')
Benjamin = BusinessContact(first_name='Benjamin', last_name='Peters', phone_number= '+1 503-435-8432', email='leejacob@example.org', job='Journalist, broadcasting', company = 'Consumers and Consumers Express', business_phone= '+34 640 183 391')
April = BusinessContact(first_name='April', last_name='Johnson', phone_number= '+1 906-563-8043', email='aallen@example.net', job='Engineer, electrical', company = 'Castle Realty', business_phone= '+34 655 468 394')
Derrick = BusinessContact(first_name='Derrick', last_name='Miller', phone_number= '+1 313-831-2818', email='christopher65@example.net', job='Market researcher', company = 'Quality Merchant Services', business_phone= '+34 649 554 164')


print(BaseContact.contact(Katherine))
print(BusinessContact.contact(Katherine))

print(Susan.label_lenght)
print(April.label_lenght)

#czemu to nie działa??
def create_contacts(class_name, i):
    cards=[]
    for i in range(i):  
        if class_name == BaseContact:
            cards.append(
                BaseContact(
                    first_name = person.first_name(),
                    last_name = person.last_name(),
                    phone_number = person.phone_number(),
                    email = person.email()))    
            return f'{cards}'         
        elif class_name == BusinessContact:
            cards.append(
                BusinessContact(
                    first_name = person.first_name(),
                    last_name = person.last_name(),
                    phone_number = person.phone_number(),
                    email = person.email(),
                    job = person.job(),
                    company = person.company(),
                    business_phone = person.phone_number()))
            return cards

print(create_contacts(BaseContact, 3))
print(create_contacts(BusinessContact, 2))

