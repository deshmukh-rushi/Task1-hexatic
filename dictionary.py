# Task 2: Dictionary - Product Price Management
# Write a Python program that uses a dictionary to store product prices. 
# The program should allow adding new products and updating prices. 
# Use “if” statements to check if a product already exists.


class Product:
    def __init__(self):
        self.products = {}

    def add_product(self):
        Pname = input("Enter product name: ")
        while True:
            try:
                price = float(input("Enter product price: "))
                if price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                else:
                    break
            except ValueError:
                print("Wrong price. Please enter a number.")

        if Pname in self.products:
            print(f"Product '{Pname}' already exists.")
        else:
            self.products[Pname] = price
            print(f"Product '{Pname}' added with price {price}.")

    def update(self):
        Pname = input("Enter product name: ")
        if Pname in self.products:
            while True:
                try:
                    new_price = float(input("Enter new price: "))
                    if new_price < 0:
                        print("Price cannot be negative. Please enter a valid price.")
                    else:
                        break
                except ValueError:
                    print("Invalid price. Please enter a number.")
            self.products[Pname] = new_price
            print(f"Price of '{Pname}' updated to {new_price}.")
        else:
            print(f"Product '{Pname}' not found.")

    def display(self):
        print("Current Product:")
        for product, price in self.products.items():
            print(f"{product}: Rs{price:.2f}")
    def exec(self):
        while True:
            print("\n1. Add Product")
            print("2. Update Price")
            print("3. Display products")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                a.add_product()
            elif choice == '2':
                a.update()
            elif choice == '3':
                a.display()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
a = Product()
a.exec()
