import json

BALANCE_FILE = "balance.txt"
INVENTORY_FILE = "inventory.txt"
HISTORY_FILE = "history.txt"

# def load_data():
#    with open(INVENTORY_FILE, "r") as inventory_file:
#    inventory_file.readline()

account_balance = 0
warehouse = {}

# Initialize recorded operations list
recorded_operations = []


def display_commands():
    print("Available commands:")
    print("1 - Balance")
    print("2 - Sale")
    print("3 - Purchase")
    print("4 - Account")
    print("5 - List")
    print("6 - Warehouse")
    print("7 - Review")
    print("8 - End")


# Add or subtract from account balance
def update_balance(amount):
    global account_balance

#    account_balance += amount

def record_sale(product_name, price, quantity):
    global warehouse, recorded_operations, account_balance
    if product_name in warehouse:
        if warehouse[product_name] >= quantity:
            revenue = price * quantity
            account_balance = account_balance + revenue
            update_balance(revenue)
            warehouse[product_name] -= quantity
            recorded_operations.append(f"Sale: {quantity} {product_name}(s) for {revenue}$")
            print("Sale recorded successfully.")
        else:
            print("Insufficient quantity in the warehouse.")
    else:
        print("Product not found in the warehouse.")

def restore_data():
    global account_balance
    with open('balance.txt', 'r') as BALANCE_FILE:
        account_balance=float(BALANCE_FILE.read()

    with open('history.txt', 'r') as HISTORY_FILE:
        global recorded_operations
        while True:
            operation=HISTORY_FILE.readline()
            if not operation:
                break
            operation=operation.strip()
            recorded_operations.append(operation)

def record_data():
    with open('balance.txt', 'w') as BALANCE_FILE:
#        for account_balance in BALANCE_FILE:
            BALANCE_FILE.write(str(account_balance))

    with open('history.txt', 'w') as HISTORY_FILE:
        global recorded_operations
        for operation in recorded_operations:
            HISTORY_FILE.write(operation)
            HISTORY_FILE.write("\n")

    with open('inventory.txt', 'w') as INVENTORY_FILE:
        global warehouse
        for product, quantity in warehouse.items():
            INVENTORY_FILE.write(f"{product}\n{quantity}\n")

def record_purchase(product_name, price, quantity):
    global account_balance, warehouse, recorded_operations
    cost = price * quantity
    if account_balance >= cost:
        account_balance = account_balance - cost
        if product_name in warehouse:
            warehouse[product_name] += quantity
        else:
            warehouse[product_name] = quantity
        recorded_operations.append(f"Purchase: {quantity} {product_name}(s) for {cost}$")
        print("Purchase recorded successfully.")
        record_data()
    else:
        print("Insufficient account balance.")


def record_warehouse(product_name, price, quantity):
    global account_balance, warehouse, recorded_operations
    if product_name in warehouse:
        warehouse[product_name] += quantity
    else:
        warehouse[product_name] = quantity
        recorded_operations.append(f"Purchase: {quantity} {product_name}(s) for {cost}$")
        print("Product recorded successfully.")


def display_account_balance():
    global account_balance
    print(f"Account balance: {account_balance}$")


def display_warehouse():
    global warehouse
    if len(warehouse) == 0:
        print("Warehouse is empty.")
    else:
        print("Warehouse inventory:")
        for product, quantity in warehouse.items():
            print(f"{product}: {quantity}")


def display_product_status(product_name):
    global warehouse
    if product_name in warehouse:
        print(f"{product_name} - Quantity: {warehouse[product_name]}")
    else:
        print("Product not found in the warehouse.")


def display_recorded_operations(from_index, to_index):
    global recorded_operations
    if not from_index and not to_index:
        print("Recorded operations:")
        for operation in recorded_operations:
            print(operation)
    else:
        from_index = from_index if from_index else 0
        to_index = to_index if to_index else len(recorded_operations)
        if from_index < 0 or from_index >= len(recorded_operations) or to_index < 0 or to_index > len(
                recorded_operations) or from_index > to_index:
            print("Invalid range.")
        else:
            print(f"Recorded operations (from index {from_index} to {to_index}):")
            for i in range(from_index, to_index):
                print(recorded_operations[i])

while True:
    display_commands()
    command = input("Enter a command: ").strip()

    if command == 'balance':
        option = input("(W)ithdraw or (D)eposit: ")
        amount = float(input("Enter amount: "))
        if option == "W":
            account_balance += - amount
        else:
            account_balance += + amount
        update_balance(amount)
        recorded_operations.append(f"Balance: {amount}$")
        print("Account balance updated.")
        print(account_balance)

    elif command == 'sale':
        product_name = input("Enter the name of the product: ")
        price = float(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity sold: "))
        record_sale(product_name, price, quantity)

    elif command == 'purchase':
        product_name = input("Enter the name of the product: ")
        price = float(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity purchased: "))
        record_purchase(product_name, price, quantity)
        recorded_operations.append(f"Product: {product_name}$")

    elif command == 'account':
        display_account_balance()

    elif command == 'list':
        display_warehouse()

    elif command == 'warehouse':
        product_name = input("Enter the name of the product: ")
        display_product_status(product_name)

    elif command == 'review':
        from_index = input("Enter the 'from' index (press Enter for the beginning): ")
        to_index = input("Enter the 'to' index (press Enter for the end): ")
        if from_index:
            from_index = int(from_index)
        if to_index:
            to_index = int(to_index)
        display_recorded_operations(from_index, to_index)

    elif command == 'end':
        break

    else:
        print("Invalid command.")

    print()

print("Program terminated.")