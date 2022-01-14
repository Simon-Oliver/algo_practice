from faker import Faker
import sqlite3
import uuid
import math


con = sqlite3.connect("./testDB.db")
cur = con.cursor()


# def execute_query(connection, query):
#     cur = connection.cursor()
#     try:
#         print("I'm working")

#     except Error as err:
#         print(f"Error: {err}")


def create_table():
    cur.execute(
        """
    CREATE TABLE CLIENT(
        client_id BLOB(32) PRIMARY KEY,
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


def add_client(client_id, f_name, l_name, dob, phone):
    cur.execute(
        """
        INSERT INTO client VALUES (?,?,?,?,?)
    """,
        (client_id, f_name, l_name, dob, phone),
    )
    con.commit()


# create_table()


def create_clients(amount):
    for n in range(0, amount):
        add_client(
            uuid.uuid4().hex,
            faker.first_name(),
            faker.last_name(),
            faker.date_of_birth(minimum_age=18),
            faker.phone_number(),
        )
        per = math.floor((100 / amount) * n)
        print(per, end="\r")


create_clients(10000)

# Shrinks the DB after making space e.g dropping a table
def vacuum():
    cur.execute("VACUUM")
    con.close()


vacuum()
