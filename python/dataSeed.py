from faker import Faker
import sqlite3

con = sqlite3.connect("./testDB.db")
cur = con.cursor()


def create_table():
    cur.execute(
        """
    CREATE TABLE CLIENT(
        client_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        dob DATE NOT NULL,
        phone TEXT NOT NULL
    )
    """
    )
    con.commit()


faker = Faker(["en_AU"])


def create_person():
    person = {}
    person["first"] = faker.first_name()
    person["last"] = faker.last_name()
    person["dob"] = faker.date_of_birth(minimum_age=18)
    person["phone"] = faker.phone_number()
    print(person)


def create_property():
    property = {}
    property["address"] = faker.address()
    property["value"] = faker


for p in range(0, 20):
    create_person()

create_table()
