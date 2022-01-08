from faker import Faker

faker = Faker(["en_AU"])


def create_person():
    person = {}
    person["first"] = faker.first_name()
    person["last"] = faker.last_name()
    person["dob"] = faker.date_of_birth(minimum_age=18)
    person["address"] = faker.address()
    print(person)


def create_property():
    property = {}
    property["address"] = faker.address()
    property["value"] = faker


for p in range(0, 20):
    create_person()
