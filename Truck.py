class Truck:
    def __init__(self, mileage, depart_time, packages, current_location):
        self.mileage = mileage
        self.depart_time = depart_time
        self.packages = packages
        self.current_location = current_location
        self.speed = 18
        self.time = depart_time

    def __str__(self):
        return f"{self.mileage},{self.depart_time},{self.packages},{self.current_location}, {self.speed}"



