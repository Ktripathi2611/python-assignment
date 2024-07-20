# order.py

class Order:
    def __init__(self):
        self.order_items = []  # Initialize an empty list to store ordered items

    def take_order(self):
        # Take input from the user to place an order
        pass

    def calculate_total(self):
        # Calculate the total bill including taxes and discounts
        pass

    def generate_receipt(self):
        # Print a receipt for the order
        pass

# Example usage:
if __name__ == "__main__":
    order = Order()
    order.take_order()
    order.generate_receipt()
