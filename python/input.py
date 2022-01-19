import sqlite3
from os import system

# con = sqlite3.connect("../chinook.db")
# cur = con.cursor()

# menu = {1: "Search by CustomerId", 2: "Search by LastName", 3: "Search by Email"}


# def create_menu():
#     for key in menu.keys():
#         print(f"{key} - {menu[key]}")


# while True:
#     create_menu()
#     option = int(input("Select search: "))
#     match option:
#         case 1:
#             search = input("Enter CustomerId: ")
#             cur.execute(f"SELECT LastName from customers WHERE CustomerId = {search}")
#             res = cur.fetchall()
#             print(res[0][0])





def settings():
    system('clear')
    print(f'''
    1 - Some Setting
    2 - Back
    ''',end="\r")
    select = int(input('Select Option: '))
    match select:
        case 1:
            print("Some setting has been toggled")
        case 2:
             menu()

def menu():
    system('clear')
    print(
        f"""
    1 - Settings
    2 - Exit
    """
    ,end="\r")
    select = int(input('Select Option: '))
    match select:
        case 1:
             settings()
        case 2:
            exit()

menu()
