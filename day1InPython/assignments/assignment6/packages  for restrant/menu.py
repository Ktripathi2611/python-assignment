# menu.py

class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.menu_items = []  # Initialize an empty list to store menu items

    def add_item(self, name, price, quantity):
        # Add a new item to the menu
        pass

    def update_item(self, name, price, quantity):
        # Update an existing item in the menu
        pass

    def delete_item(self, name):
        # Delete an item from the menu
        pass

    def display_menu(self):
        # Display the current menu items
        pass

# Example usage:
if __name__ == "__main__":
    menu = Menu()
    menu.add_item("Burger", 5.99, 10)
    menu.display_menu()
