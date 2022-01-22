import sqlite3
from os import system

con = sqlite3.connect("../chinook.db")
cur = con.cursor()

menu = {1: "Search by CustomerId", 2: "Search by LastName", 3: "Search by Email", 4: "Exit"}


def search_CustomerId():
    system('clear')
    search = input("Enter CustomerId: ")
    cur.execute(f"SELECT LastName from customers WHERE CustomerId = {search}")
    res = cur.fetchall()
    print(f'''
    ----------------------------
    Customer Found:
    Last Name: {res[0][0]}
    ----------------------------
    ''')
    show_invoices(search)

# refactor the above and the below function to follow DRY
def search_CustomerEmail():
    system("clear")
    search = str(input("Enter customer email address: "))
    cur.execute(f"SELECT LastName from customers WHERE Email = '{search}'")
    res = cur.fetchall()
    print(f'''
       ----------------------------
       Customer Found:
       Last Name: {res[0][0]}
       ----------------------------
       ''')

def show_invoices(CustomerId):
    cur.execute(f"""
    SELECT Total, InvoiceId, InvoiceDate from invoices WHERE CustomerId = {CustomerId}
    """)
    res = cur.fetchall()
    print(f"{len(res)} invoices found:")
    for invoice in res:
        print(f"""
        InvoiceId: {invoice[1]}
        Invoice date: {invoice[2]}
        Total: {invoice[0]}
        """)


def create_menu():
    system('clear')
    for key in menu.keys():
        print(f"{key} - {menu[key]}")
    option = int(input("Select search: "))
    match option:
        case 1:
            search_CustomerId()
            create_back(search_CustomerId)
        case 3:
            search_CustomerEmail()
            create_back(search_CustomerEmail)
        case 4:
            exit()

def create_back(searchFunction):
    print(f'''
    1 - Back to Menu
    2 - Search again
    ''')
    select = int(input('Select Option: '))
    match select:
        case 1:
            create_menu()
        case 2:
            searchFunction()
            create_back(searchFunction)

def run():
    create_menu()
    


run()

# def settings():
#     system('clear')
#     print(f'''
#     1 - Some Setting
#     2 - Back
#     ''',end="\r")
#     select = int(input('Select Option: '))
#     match select:
#         case 1:
#             print("Some setting has been toggled")
#         case 2:
#              menu()

# def menu():
#     system('clear')
#     print(
#         f"""
#     1 - Settings
#     2 - Exit
#     """
#     ,end="\r")
#     select = int(input('Select Option: '))
#     match select:
#         case 1:
#              settings()
#         case 2:
#             exit()

# menu()
