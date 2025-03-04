class Bus:
    def __init__(self, number, route_key, driver_name):
        self.number = number
        self.route_key = route_key
        self.driver_name = driver_name

    def print_details(self):
        return (f"Bus Number: {self.number}\nRoute Key: {self.route_key}\n"
                f"Driver Name: {self.driver_name}")


bus1 = Bus(2010, "Y", "Rafael")
bus2 = Bus(199, "PY", "Alex")
bus3 = Bus(876, 95, "Lebron")
print(Bus.print_details(bus1))
print(Bus.print_details(bus2))
print(Bus.print_details(bus3))
