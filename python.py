python
class products1:
    def __init__(self):
        self.products = {
            "Product Name": ["water", "soda", "chips", "bread", "eggs"],
            "Amount": [200000, 300000, 600000, 6000, 1000000],
            "Price": [80, 130, 75, 45, 56]
        }
        self.products2 = {
            "Product Name": ["pens", "notebooks", "erasers", "bread", "eggs"],
            "Amount": [200000, 300000, 600000, 6000, 1000000],
            "Price": [80, 130, 75, 45, 56]
        }

    def ProductTable1(self):
        print("\nMain Store Product Table:")
        print("{:<15} {:<10} {:<10}".format("Product Name", "Amount", "Price"))
        print("-" * 35)
        for i in range(len(self.products["Product Name"])):
            print(
                "{:<15} {:<10} {:<10}".format(
                    self.products["Product Name"][i],
                    self.products["Amount"][i],
                    self.products["Price"][i],
                )
            )

    def ProductTable(self):
        print("\nStationary Store Product Table:")
        print("{:<15} {:<10} {:<10}".format("Product Name", "Amount", "Price"))
        print("-" * 35)
        for i in range(len(self.products2["Product Name"])):
            print(
                "{:<15} {:<10} {:<10}".format(
                    self.products2["Product Name"][i],
                    self.products2["Amount"][i],
                    self.products2["Price"][i],
                )
            )

    def process_order(self, product_name, order_quantity, Delivery):
        if product_name in self.products["Product Name"]:
            index = self.products["Product Name"].index(product_name)
            if self.products["Amount"][index] >= order_quantity:
                self.products["Amount"][index] -= order_quantity
                print(f"\nOrder successful! {order_quantity} {product_name}(s) ordered.")
            else:
                print(f"\nNot enough stock for {product_name}. Only {self.products['Amount'][index]} left.")
        else:
            print(f"\nProduct {product_name} not found.")

    def totalcost(self, total, product_name, order_quantity, Delivery):
        if product_name in self.products["Product Name"]:
            index = self.products["Product Name"].index(product_name)
            if total == "USA":
                cost = self.products["Price"][index] * order_quantity
            elif total == "ERU":
                cost = self.products["Price"][index] * order_quantity / 1.05575
            else:
                cost = self.products["Price"][index] * order_quantity * 49.58300

            # Apply discounts
            if 250 <= order_quantity < 500:
                cost *= 0.95
            elif 500 <= order_quantity < 750:
                cost *= 0.90
            elif 750 <= order_quantity < 1000:
                cost *= 0.85
            elif order_quantity > 1250:
                cost *= 0.75

            # Add delivery cost
            if int(Delivery) == 1:
                cost += 200
            else:
                cost += 50

            return cost
        else:
            print("Product not defined.")
            return 0


def display(store_instance):
    while True:
        print("\nMenu:")
        print("1. Display Main Store")
        print("2. Order Product")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            store_instance.ProductTable1()
        elif choice == "2":
            product_name = input("Enter product name: ").lower()
            order_quantity = int(input("Enter quantity to order: "))
            total = input("In what currency do you want the amount? (USA, EGP, ERU): ").upper()
            Delivery = int(input("Enter 1 for Delivery or 2 for Pickup: "))
            cost = store_instance.totalcost(total, product_name, order_quantity, Delivery)
            if cost > 0:
                print(f"Total cost of your order is: {cost}")
                store_instance.process_order(product_name, order_quantity, Delivery)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


def display2(store_instance):
    while True:
        print("\nMenu:")
        print("1. Display Stationary Store")
        print("2. Order Product")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            store_instance.ProductTable()
        elif choice == "2":
            product_name = input("Enter product name: ").lower()
            order_quantity = int(input("Enter quantity to order: "))
            total = input("In what currency do you want the amount? (USA, EGP, ERU): ").upper()
            Delivery = int(input("Enter 1 for Delivery or 2 for Pickup: "))
            cost = store_instance.totalcost(total, product_name, order_quantity, Delivery)
            if cost > 0:
                print(f"Total cost of your order is: {cost}")
                store_instance.process_order(product_name, order_quantity, Delivery)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


usernames = ["mai", "amr", "hossam"]
passwords = ["pass1", "pass2", "pass3"]

while True:
    print("Welcome!")
    print("1: Log in")
    print("2: Sign up")
    print("3: Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        if name in usernames and password in passwords:
            index_name = usernames.index(name)
            index_password = passwords.index(password)
            if index_name == index_password:
                print(f"Welcome back, {name}!")
                store_instance = products1()
                while True:
                    print("Main Store: 1")
                    print("Stationary Store: 2")
                    store_choice = input("Enter your choice (1/2): ")
                    if store_choice == "1":
                        display(store_instance)
                    elif store_choice == "2":
                        display2(store_instance)
                    break
            else:
                print("Invalid login. Username and password do not match.")
        else:
            print("Username or password not found. Please try again.")

    elif choice == "2":
        new_name = input("Choose a username: ")
        if new_name in usernames:
            print("Username already taken. Please try another.")
        else:
            new_password = input("Choose a password: ")
            usernames.append(new_name)
            passwords.append(new_password)
            print("Sign up successful. You can now log in.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
