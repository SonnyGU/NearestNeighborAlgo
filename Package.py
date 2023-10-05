import datetime
import csv
from HashTable import HashTable


def get_package_status():
    """
    Prompts user for a specific time and package ID.
    Displays the status of the specified package (or all packages) at the given time.
    """
    time_input = input("Enter the time (HH:MM) to check status: ")
    hours, minutes = map(int, time_input.split(':'))
    time_to_check = datetime.timedelta(hours=hours, minutes=minutes)

    package_id_input = input("Enter the Package ID or press Enter to see all packages: ")

    # If user provides an ID, we just take that ID.
    # If user just presses Enter, we take all IDs.
    single_entry = [int(package_id_input)] if package_id_input else range(1, 41)

    for packageID in single_entry:
        package = Package.get_by_id(packageID)
        if package:
            package.status_update(time_to_check)
            print(f"Package ID: {package.ID}, Status: {package.status}, Delivery Time: {package.deliver_time}")
        else:
            print(f"Package with ID {packageID} not found.")


def get_time_range():
    """
    Gets start and end time from user with default values set to business hours.
    Returns: tuple containing start and end times as datetime.timedelta objects.
    """
    default_start_time = datetime.timedelta(hours=8)  # 8:00am
    default_end_time = datetime.timedelta(hours=17)  # 5:00pm
    start_time_input = input("Enter the start time (HH:MM) of leave blank: ")
    start_time = default_start_time
    if start_time_input:
        # if input is given, update the start_time
        start_hours, start_minutes = map(int, start_time_input.split(':'))
        start_time = datetime.timedelta(hours=start_hours, minutes=start_minutes)

    end_time_input = input("Enter the end time (HH:MM) or leave blank if none: ")
    end_time = default_end_time
    if end_time_input:  # updates if input is given
        end_hours, end_minutes = map(int, end_time_input.split(':'))
        end_time = datetime.timedelta(hours=end_hours, minutes=end_minutes)

    return start_time, end_time


# Package outline
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
        self.status = "At the Hub"  # default status will update when package is on move

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
            if time_change > datetime.timedelta(hours=10, minutes=20):
                self.street = "410 S. State St"
                self.zip_code = "84111"
                self.city = "UT"
            else:
                self.street = self.street
                self.zip_code = self.zip_code

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
    def print_status_for_time_range(cls, start_time, end_time):
        print(f"Package Status between {start_time} and {end_time}:\n")

        for pkg_id in sorted(cls.pkg_holder.keys()):
            package = cls.get_by_id(pkg_id)

            package.status_update(start_time)  # update the status for the given start time
            start_status = package.status

            package.status_update(end_time)  # update the status for the given end time
            end_status = package.status

            # Check if delivery time is within the user-specified range
            if package.deliver_time and start_time <= package.deliver_time <= end_time:
                print(
                    f"Package ID: {package.ID}, Address: {package.street}, {package.city}, {package.state} {package.zip_code}, "
                    f"Status at {start_time}: {start_status}, Status at {end_time}: {end_status}, "
                    f"Delivery Time: {package.deliver_time}")
            else:
                print(
                    f"Package ID: {package.ID}, Address: {package.street}, {package.city}, {package.state} {package.zip_code}, "
                    f"Status at {start_time}: {start_status}, Status at {end_time}: {end_status}")

    def print_details(self):
        print(
            f"Package ID: {self.ID}, Address: {self.street}, {self.city}, {self.state} {self.zip_code}, Status: {self.status}")

    @classmethod
    def get_by_id(cls, package_ID):
        return cls.pkg_holder.search(package_ID)
