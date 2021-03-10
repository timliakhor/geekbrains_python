class Person:
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.birthday_year}" \
               f" {self.city} {self.email} {self.phone_number}"

    first_name: str
    last_name: str
    birthday_year: int
    city: str
    email: str
    phone_number: str

    def __init__(self, first_name: str,
                 last_name: str,
                 birthday_year: int,
                 city: str,
                 email: str,
                 phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday_year = birthday_year
        self.city = city
        self.email = email
        self.phone_number = phone_number


def create_person(first_name: str,
                  last_name: str,
                  birthday_year: int,
                  city: str,
                  email: str,
                  phone_number: str) -> Person:
    return Person(first_name, last_name, birthday_year, city, email, phone_number)


person: Person = create_person(first_name=input('Please, enter first_name: '),
                               last_name=input('Please, enter last_name: '),
                               birthday_year=int(input('Please, enter birthday_year: ')),
                               city=input('Please, enter city: '),
                               email=input('Please, enter email: '),
                               phone_number=input('Please, enter phone_number: '))
print(person)
