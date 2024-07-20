# restaurant.py
from menu import Menu
from order import Order
from exceptions import InvalidMenuItemError, InsufficientQuantityError
from file_handling import read_menu_from_file, write_menu_to_file, read_orders_from_file, write_orders_to_file

def main():
    menu = Menu()
    order = Order()

    # Load initial menu and orders from files (use file_handling functions)

    while True:
        print("\nRestaurant Management System")
        print("1. Add item to menu")
        print("2. Update item in menu")
        print("3. Delete item from menu")
        print("4. Take order")
        print("5. View order")
        print("6. Generate receipt")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add item to menu
            pass
        elif choice == "2":
            # Update item in menu
            pass
        elif choice == "3":
            # Delete item from menu
            pass
        elif choice == "4":
            # Take order
            pass
        elif choice == "5":
            # View order
            pass
        elif choice == "6":
            # Generate receipt
            pass
        elif choice == "7":
            # Save menu and orders to files (use file_handling functions)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
