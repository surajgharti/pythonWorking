class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True


    def open_seats(self):
        return self.capacity - len(self.passengers)


fligh = Flight(3)
people = ["suraj", "Sarmila", "Sukripa", "Savit"]

for person in people:
    print(f"Avialiable steates {fligh.open_seats()}")
    if fligh.addPassenger(person):
        print(f"Added {person} Successfully added")
    else:
        print("Couldn't add")

