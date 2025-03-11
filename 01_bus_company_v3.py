class Bus:
    bus_list = []

    def __init__(self, number, route_key, driver_name):
        self.number = number
        self.route_key = route_key
        self.driver_name = driver_name
        Bus.bus_list.append(self)

    def print_details(self):
        for bus_ in Bus.bus_list:
            if bus_ == self:
                print(f"\nBus Number: {self.number}\nRoute Key: "
                      f"{self.route_key}\nDriver Name: {self.driver_name}")


def find_bus(question):
    bus_to_find = input(question)
    for bus in Bus.bus_list:
        if bus_to_find == bus.number:
            return Bus.print_details(bus)
    print(f"Bus {bus_to_find} is not registered in the system yet")


# Main routine
Bus("2010", "Y", "Rafael")
Bus("199", "PY", "Alex")
Bus("876", "95", "Lebron")

find_bus("Which bus number would you like (e.g. '2010', '2011'): ")
