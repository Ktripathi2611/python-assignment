class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.__vehicle_id = vehicle_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__category = category

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_category(self):
        return self.__category

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model


def add_vehicle(vehicles, vehicle):
    vehicle_set = set([v.get_vehicle_id() for v in vehicles])
    if vehicle.get_vehicle_id() not in vehicle_set:
        vehicles.append(vehicle)
    else:
        print("Error: Vehicle with ID", vehicle.get_vehicle_id(), "already exists.")


def remove_vehicle(vehicles, vehicle_id):
    for vehicle in vehicles:
        if vehicle.get_vehicle_id() == vehicle_id:
            vehicles.remove(vehicle)
            return
    print("Error: Vehicle with ID", vehicle_id, "not found.")


def search_vehicles(vehicles, search_term):
    results = []
    for vehicle in vehicles:
        if search_term.lower() in vehicle.get_make().lower() or search_term.lower() in vehicle.get_model().lower():
            results.append(vehicle)
    return results


def list_vehicles(vehicles):
    print("-" * 50)
    print(" | ".join(["Vehicle ID", "Make", "Model", "Year", "Category"]))
    print("-" * 50)
    for vehicle in vehicles:
        print(" | ".join([str(vehicle.get_vehicle_id()), vehicle.get_make(), vehicle.get_model(), str(vehicle.get_year()), vehicle.get_category()]))
    print("-" * 50)


def categorize_vehicles(vehicles):
    categories = {}
    for vehicle in vehicles:
        category = vehicle.get_category()
        if category not in categories:
            categories[category] = []
        categories[category].append(vehicle)
    return categories


# Main program loop
vehicles = []

while True:
    print("\nVehicle Rental System")
    print("1. Add Vehicle")
    print("2. Remove Vehicle")
    print("3. Search Vehicles")
    print("4. List All Vehicles")
    print("5. Categorize Vehicles")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            vehicle_id = int(input("Enter vehicle ID: "))
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            category = input("Enter category: ")
            new_vehicle = Vehicle(vehicle_id, make, model, year, category)
            add_vehicle(vehicles, new_vehicle)
        except ValueError:
            print("Invalid input. Please enter integers for ID and year.")

    elif choice == '2':
        try:
            vehicle_id = int(input("Enter vehicle ID to remove: "))
            remove_vehicle(vehicles, vehicle_id)
        except ValueError:
            print("Invalid input. Please enter an integer for ID.")

    elif choice == '3':
        search_term = input("Enter search term (make or model): ")
        search_results = search_vehicles(vehicles, search_term)
        print("Search results for", search_term)
        list_vehicles(search_results)

    elif choice == '4':
        print("All vehicles in the system:")
        list_vehicles(vehicles)

    elif choice == '5':
        vehicle_categories = categorize_vehicles(vehicles)
        print("Vehicles categorized by type:")
        for category, vehicle_list in vehicle_categories.items():
            print(category)
            list_vehicles(vehicle_list)

    elif choice == '6':
        print("Exiting Vehicle Rental System")
        break
