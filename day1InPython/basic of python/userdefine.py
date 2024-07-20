class PackageNotFoundError(Exception):
    def __init__(self, package_name):
        super().__init__(f"Package '{package_name}' not found")

def check_package_exists(package_name):
    try:
        __import__(package_name)
    except ImportError:
        raise PackageNotFoundError(package_name)

# Example usage:
try:
    user_input_package = input("Enter a package name: ")
    check_package_exists(user_input_package)
    print(f"Package '{user_input_package}' exists!")
except PackageNotFoundError as e:
    print(f"Error: {e}")
      