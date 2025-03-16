class Bus:
    # This is a class attribute so there is only one of these and each object
    # created is appended here.
    bus_list = []

    # Initializes the object
    def __init__(self, number, route_key, driver_name):
        self.number = number
        self.route_key = route_key
        self.driver_name = driver_name
        # Appends the object to the list
        Bus.bus_list.append(self)

    # Method to print details of specific object
    def print_details(self):
        print(f"\nBus Number: {self.number}\nRoute Key: "
              f"{self.route_key}\nDriver Name: {self.driver_name}")

# Function to ask user for what bus, search for bus then print details if found
def find_bus(question):
    bus_to_find = input(question)
    # Iterates through the bus list
    for bus in Bus.bus_list:
        # Checks if the bus number matches the users search
        if bus_to_find == bus.number:
            # Runs print method if found
            bus.print_details()
            return
    print(f"Bus {bus_to_find} is not registered in the system yet")


# Main routine
# Creates bus objects without variables as they are added to bus list anyway
Bus("2010", "Y", "Rafael")
Bus("199", "PY", "Alex")
Bus("876", "95", "Lebron")

# Runs find bus function
find_bus("Which bus number would you like (e.g. '2010', '2011'): ")
