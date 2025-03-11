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
                print(f"\nBus Number: {bus_.number}\nRoute Key: "
                      f"{bus_.route_key}\nDriver Name: {bus_.driver_name}")


bus1 = Bus("2010", "Y", "Rafael")
bus2 = Bus("199", "PY", "Alex")
bus3 = Bus("876", "95", "Lebron")

for bus in range(len(Bus.bus_list)):
    Bus.print_details(Bus.bus_list[bus])
