import datetime
import csv
from HashTable import HashTable


def get_time_or_default():
    """
    Gets a time from user with default value set to end of business day.
    Returns: a datetime.timedelta object representing the time.
    """
    default_end_time = datetime.timedelta(hours=24, minutes=0)  # 11:58pm
    time_input = input("Enter a time (HH:MM) to view package status at that moment, or press ENTER to see status at "
                       "end of day:  ")

    if time_input:  # If the user entered a time.
        hours, minutes = map(int, time_input.split(':'))
        return datetime.timedelta(hours=hours, minutes=minutes)
    else:
        return default_end_time  # Default to end of day.


# Package outline
class Package:
    def __init__(self, ID, street, city, state, zip_code, deadline, weight, notes, truck_name=None):
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
        self.status = "At the Hub"  # default status will update when package is on move
        self.truck_name = truck_name

    def __str__(self):
        return (f"ID: {self.ID}, Address: {self.street}, {self.city}, {self.state} {self.zip_code}, "
                f"Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}, "
                f"Departure Time: {self.depart_time}, Delivery Time: {self.deliver_time}")

    pkg_holder = HashTable()

    def status_update(self, time_change):
        current_time = time_change if isinstance(time_change, datetime.timedelta) else datetime.timedelta(
            hours=time_change.hour, minutes=time_change.minute)
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
            if time_change >= datetime.timedelta(hours=10, minutes=20):
                self.street = "410 S. State St"
                self.zip_code = "84111"
                self.city = "UT"
                self.status = self.status + " Delayed"

            else:  # add elif for other time to change it back
                self.street = "300 State St"
                self.zip_code = "84103"
                self.state = "UT"
                self.city = "Salt Lake City"

    """
        Loads package details from a CSV file and saves them in a hash table.
        Args:
        - filename (str): Path to the CSV file containing package details.
        """

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
                pkg_note = package[7] if len(package) > 7 else ""  # in case the note field is blank

                # creates new package instance
                pkg = cls(pkg_id, pkg_street, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_weight, pkg_note)
                #  saves to hash table
                cls.pkg_holder.insert(pkg_id, pkg)





    @classmethod
    def get_by_id(cls, package_ID):
        return cls.pkg_holder.search(package_ID)

