class flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): #if self.open_seats == 0
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = flight(3) #that is tha capcity of the flight

people = ["Harry", "Ghassan" ,"Ali", "Ron"]
for person in people:
    
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")

    else:
        print("No available seats for this person")
