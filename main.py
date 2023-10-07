"""
Guson Ulysse
Student ID: 010821257
"""
import datetime

from DataLoader import DataLoader
from DeliveryManager import DeliveryManager
from Package import Package, get_time_or_default
from Truck import Truck


def main():
    # loading packages from csv
    Package.pkg_holder.clear_table()
    # Package.pkg_holder.display()
    Package.load_from_csv("CSVFiles/packageCSV.csv")
    # print(Package.get_by_id(0))

    addresses = DataLoader.load_csv("CSVFiles/addressCSV.csv")
    distances = DataLoader.load_csv("CSVFiles/distanceCSV.csv")

    # initializing trucks and loading info into deliveryManager instances
    truck1 = Truck(0.0, datetime.timedelta(hours=8), [15, 14, 20, 16, 13, 1, 34, 29, 30, 31, 40, 33, 2, 21],
                   "4001 South 700 East")
    delivery_manager1 = DeliveryManager(truck1, distances, addresses)

    truck2 = Truck(0.0, datetime.timedelta(hours=9, minutes=5),
                   [3, 6, 25, 26, 36, 38, 37, 18, 5, 7, 10, 24, 27, 35, 39],
                   "4001 South 700 East")
    delivery_manager2 = DeliveryManager(truck2, distances, addresses)

    truck3 = Truck(0.0, datetime.timedelta(hours=10, minutes=30), [9, 8, 32, 28, 17, 21, 4, 11, 12, 19, 22, 23],
                   "4001 South 700 East")
    delivery_manager3 = DeliveryManager(truck3, distances, addresses)

    # calling class to start delivery
    delivery_manager1.delivering_packages()

    delivery_manager2.delivering_packages()

    delivery_manager3.delivering_packages()

    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage

    # Simple cmdline loop
    while True:
        print("\n***************************************")
        print("1. Begin Package Printing Process")
        print("2. Includes total mileage")
        print("3. Exit the Program")
        print("***************************************")

        choice = input("Enter your choice: ")

        if choice == '1' or '2':
            time_to_check = get_time_or_default()
            package_id_input = input("Enter the Package ID or press Enter to see all packages: ")

            # if a specific package ID is given
            if package_id_input:
                package_id = int(package_id_input)
                pkg = Package.get_by_id(package_id)
                if pkg:
                    pkg.status_update(time_to_check)
                    # base output
                    output = (f"Package ID: {pkg.ID}, Address: {pkg.street}, {pkg.city}, {pkg.state} {pkg.zip_code}, "
                              f"Status at {time_to_check}: {pkg.status}")

                    # If package is delivered, append delivery time to output
                    if pkg.status == "Delivered" or pkg.status == "Delivered Delayed":
                        output += f", Delivery Time: {pkg.deliver_time}"
                    print(output)
                    print(f"\nTotal Mileage Travelled by All Trucks: {total_mileage:.2f} miles")
                else:
                    print(f"Package with ID {package_id} not found.")

            # if no specific package ID is given
            else:
                for pkg_id in Package.pkg_holder.keys():
                    pkg = Package.get_by_id(pkg_id)
                    pkg.status_update(time_to_check)

                    if time_to_check > datetime.timedelta(hours=23, minutes=58):
                        status_time = "end of day"
                    else:
                        status_time = str(time_to_check)
                    # Base output
                    output = (f"Package ID: {pkg.ID}, Address: {pkg.street}, {pkg.city}, {pkg.state} {pkg.zip_code}, "
                              f"Status at {status_time}: {pkg.status}")

                    # If package is delivered, append delivery time to output
                    if pkg.status == "Delivered" or pkg.status == "Delivered Delayed":
                        output += f", Delivery Time: {pkg.deliver_time}"

                    print(output)
                if choice == '2':
                    print(f"\nTotal Mileage Travelled by All Trucks: {total_mileage:.2f} miles")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")


# assures that main is not called by another class by mistake
if __name__ == "__main__":
    main()

# Guson Ulysse
