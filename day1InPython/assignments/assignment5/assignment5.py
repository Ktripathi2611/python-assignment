from datetime import datetime

class Product:
    def __init__(self, name, category, price, quantity, expiration_date):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

    def is_expired(self):
        expiration = datetime.strptime(self.expiration_date, '%Y-%m-%d').date()
        today = datetime.today().date()
        return expiration < today

inventory = []

def add_product_to_inventory():
    name = input("Enter product name: ").strip()
    category = input("Enter product category: ").strip()
    price = float(input("Enter product price: ").strip())
    quantity = int(input("Enter product quantity: ").strip())
    expiration_date = input("Enter expiration date (YYYY-MM-DD): ").strip()
    new_product = Product(name, category, price, quantity, expiration_date)
    inventory.append(new_product)
    print(f"Product '{name}' added to inventory.")

def remove_product_from_inventory():
    product_name = input("Enter product name to remove: ").strip()
    inventory[:] = [product for product in inventory if product.name != product_name]
    print(f"Product '{product_name}' removed from inventory.")

def search_products():
    search_term = input("Enter search term (name or category): ").strip().lower()
    matching_products = [product for product in inventory
                         if search_term in product.name.lower() or search_term in product.category.lower()]
    if not matching_products:
        print("No products found.")
    return matching_products

def list_all_products():
    if not inventory:
        print("Inventory is empty!")
        return
    print("-" * 50)
    print("Products in Inventory:")
    print("-" * 50)
    for product in inventory:
        print(f"Name: {product.name}")
        print(f"Category: {product.category}")
        print(f"Price: ${product.price:.2f}")
        print(f"Quantity: {product.quantity}")
        print(f"Expiration Date: {product.expiration_date}")
        print("-" * 20)

def categorize_products():
    categories = {}
    for product in inventory:
        if product.category not in categories:
            categories[product.category] = []
        categories[product.category].append(product)
    return categories

def load_inventory_from_file(filename):
    inventory.clear()  # Clear existing inventory before loading
    with open(filename, 'r') as f:
        next(f)  # Skip header line
        for line in f:
            data = line.strip().split(',')
            name = data[0].strip()
            category = data[1].strip()
            price = float(data[2].strip())
            quantity = int(data[3].strip())
            expiration_date = data[4].strip()
            new_product = Product(name, category, price, quantity, expiration_date)
            inventory.append(new_product)
    print(f"Inventory loaded successfully from '{filename}'.")

# Example of usage (you would integrate this as needed in your application):
while True:
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Search Products")
    print("4. List All Products")
    print("5. Categorize Products")
    print("6. Load Inventory from File")
    print("0. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        add_product_to_inventory()
    elif choice == '2':
        remove_product_from_inventory()
    elif choice == '3':
        search_products()
    elif choice == '4':
        list_all_products()
    elif choice == '5':
        categorize_products()
    elif choice == '6':
        filename = input("Enter filename to load inventory from: ").strip()
        load_inventory_from_file(filename)
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
