# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_all_info(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    # Update stock method. Used in re-stock function
    def update_quantity(self, new_quantity):
        convert_quantity = int(self.quantity)
        convert_quantity += new_quantity
        self.quantity = str(convert_quantity)

    def __str__(self):
        msg = (f"Country: {self.country}. "
               f"Code: {self.code}. "
               f"Product: {self.product}. "
               f"Cost: {self.cost}. "
               f"Quantity: {self.quantity}"
               )
        return msg


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
inventory_file_header = ""


# ==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as inventory_file:  # Open the text file and store as "inventory_file"
            next(inventory_file)  # Skip header
            all_shoes = inventory_file.readlines()  # Store the shoes

            # Clear the shoe_list
            shoe_list.clear()
            # Add each line to shoe_list as a new object.
            for line in all_shoes:
                line = line.strip("\n")
                line = line.split(",")
                shoe = Shoe(line[0], line[1], line[2], line[3], line[4])
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("'inventory.txt' was not found.")


def capture_shoes():
    # Get all info from the user and store into individual variables
    capture_country = input("Country: ")
    capture_code = input("Code: ")
    capture_product = input("Product: ")
    # Only get numerical input for 'capture_cost'
    capture_cost = 0
    while capture_cost == 0:
        try:
            capture_cost = float(input("Cost: £"))
        except ValueError:
            input("Invalid input. Please try again.")
    # Only get numerical input for 'capture_quantity'
    capture_quantity = 0
    while capture_quantity == 0:
        try:
            capture_quantity = int(input("Quantity: "))
        except ValueError:
            input("Invalid input. Please try again.")

    # Create new shoe entry. Add it to shoe_list
    shoe = Shoe(capture_country, capture_code, capture_product, capture_cost, capture_quantity)
    shoe_list.append(shoe)

    # Update text file
    with open("inventory.txt", "w") as inventory_file:
        inventory_file.write(f"Country,Code,Product,Cost,Quantity\n")  # Add header
        for entry in shoe_list:
            inventory_file.write(
                f"{entry.get_all_info()}\n")  # Write all files in a format that can be read by the program


def view_all():
    print("=== ALL SHOE ENTRIES ===\n")
    for shoe_entry in shoe_list:
        print(shoe_entry)
        print()


def re_stock():
    lowest_stock_count = 9999999  # There won't be that many shoes, right?
    lowest_stock_shoe = ""
    for shoe_entry in shoe_list:  # Get the lowest stock number and store the object.
        shoe_quantity = int(shoe_entry.get_quantity())
        if shoe_quantity < lowest_stock_count:
            lowest_stock_count = shoe_quantity
            lowest_stock_shoe = shoe_entry
    lowest_shoe_index = shoe_list.index(lowest_stock_shoe)
    print(f"=== The item with the least stock is ===\n{lowest_stock_shoe}")

    # Would you like to add stock?
    re_stock_choice = input("Would you like to add stock (y/n)? ")
    while re_stock_choice != "y" and re_stock_choice != "n":
        re_stock_choice = input("Invalid choice!\nWould you like to add stock (y/n)? ")
    if re_stock_choice == "y":
        # Get additional stock number
        while True:
            try:
                re_stock_amount = int(input("How much stock would you like to add? "))
            except ValueError:
                print("Invalid entry!")
                continue
            else:
                break
        # Update entry:
        shoe_list[lowest_shoe_index].update_quantity(re_stock_amount)

        # Update text file
        with open("inventory.txt", "w") as inventory_file:
            inventory_file.write(f"Country,Code,Product,Cost,Quantity\n")  # Add header
            for entry in shoe_list:
                inventory_file.write(
                    f"{entry.get_all_info()}\n")  # Write all files in a format that can be read by the program

        # Print updated object
        print(shoe_list[lowest_shoe_index])

    elif re_stock_choice == "n":
        pass


def search_shoe():
    searched_shoe = input("Enter the shoe code you are looking for: ").upper()

    for shoe in shoe_list:
        if shoe.get_code() == searched_shoe:
            input(shoe)


def value_per_item():
    for shoe in shoe_list:
        shoe_value = round(float(shoe.get_cost()) * float(shoe.get_quantity()), 2)
        print(shoe)
        print(f"Value: £{shoe_value}")
        print()


def highest_qty():
    highest_qty_shoe = 0
    for shoe in shoe_list:
        if float(shoe.get_quantity()) > float(highest_qty_shoe):
            highest_qty_shoe = shoe.get_quantity()
            selected_shoe = shoe
    print(f"{selected_shoe}\nThis shoe has the highest quantity at {highest_qty_shoe} units and should go on sale.")


# ==========Main Menu=============
menu_choice = ""
while menu_choice != "quit":
    menu_choice = input("""Please choose one of the following options:
Update - Force update the program's product list
Add - Create a new entry
View - View all products
Stock - Show the lowest stock - update stock?
Search - Search for a product using the product code
Value - Get the total value for each item
Qty - Get the product with the greatest quantity
Quit - Exit the program

Enter Choice: """).lower()

    if menu_choice == "update":
        read_shoes_data()
    elif menu_choice == "add":
        read_shoes_data()
        capture_shoes()
    elif menu_choice == "view":
        read_shoes_data()
        view_all()
    elif menu_choice == "stock":
        read_shoes_data()
        re_stock()
    elif menu_choice == "search":
        read_shoes_data()
        search_shoe()
    elif menu_choice == "value":
        read_shoes_data()
        value_per_item()
    elif menu_choice == "qty":
        read_shoes_data()
        highest_qty()
    elif menu_choice == "quit":
        print("Goodbye!")
        exit()
    else:
        input("Invalid input. Please try again!")
