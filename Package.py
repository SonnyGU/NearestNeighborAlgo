import datetime
import csv
from HashTable import HashTable


class Package:
    def __init__(self, ID, street, city, state, zip_code, deadline, weight, notes):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.depart_time = None
        self.deliver_time = None
        self.status = "At the Hub"

    def __str__(self):
        return (f"ID: {self.ID}, Address: {self.street}, {self.city}, {self.state} {self.zip_code}, "
                f"Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}, "
                f"Departure Time: {self.depart_time}, Delivery Time: {self.deliver_time}")

    pkg_holder = HashTable()

    def status_update(self, time_change):
        if not self.deliver_time:
            self.status = "At the hub"
        elif time_change < self.depart_time:
            self.status = "At the hub"
        elif time_change < self.deliver_time:
            self.status = "En route"
        else:
            self.status = "Delivered"
        #  catches the error of address and fixes it at the appropriate time
        if self.ID == 9:
            if time_change > datetime.timedelta(hours=10, minutes=20):
                self.street = "410 S. State St"
                self.zip_code = "84111"
                self.city = "UT"
            else:
                self.street = self.street
                self.zip_code = self.zip_code

    @classmethod
    def load_from_csv(cls, filename):
        with open(filename) as packages_file:
            package_info = csv.reader(packages_file, delimiter=',')
            for package in package_info:
                pkg_id = int(package[0])
                pkg_street = package[1]
                pkg_city = package[2]
                pkg_state = package[3]
                pkg_zip = package[4]
                pkg_deadline = package[5]
                pkg_weight = package[6]
                pkg_note = package[7] if len(package) > 7 else ""

                # creates new package instance
                pkg = cls(pkg_id, pkg_street, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_weight, pkg_note)
                #  saves to hash table
                cls.pkg_holder.insert(pkg_id, pkg)
                print(f"Inserted package with ID: {pkg_id}")

    @classmethod
    def get_by_id(cls, package_ID):
        return cls.pkg_holder.search(package_ID)
