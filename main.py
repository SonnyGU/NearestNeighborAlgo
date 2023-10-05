import datetime

from DataLoader import DataLoader
from DeliveryManager import DeliveryManager
from Package import Package
from Truck import Truck


def main():
    # loading packages from csv
    Package.pkg_holder.clear_table()
    # Package.pkg_holder.display()
    Package.load_from_csv("CSVFiles/packageCSV.csv")
    # print(Package.get_by_id(0))

    addresses = DataLoader.load_csv("CSVFiles/addressCSV.csv")
    distances = DataLoader.load_csv("CSVFiles/distanceCSV.csv")

    truck1 = Truck(0.0, datetime.timedelta(hours=8), [15, 14, 20, 16, 13, 1, 34, 29, 30, 31, 40, 33, 2, 21],
                   "4001 South 700 East")
    delivery_manager1 = DeliveryManager(truck1, distances, addresses)

    truck2 = Truck(0.0, datetime.timedelta(hours=8), [3, 6, 25, 26, 36, 38, 37, 18, 5, 7, 10, 24, 27, 35, 39],
                   "4001 South 700 East")
    delivery_manager2 = DeliveryManager(truck2, distances, addresses)

    truck3 = Truck(0.0, datetime.timedelta(hours=8), [9, 8, 32, 28, 17, 21, 4, 11, 12, 19, 22, 23],
                   "4001 South 700 East")
    delivery_manager3 = DeliveryManager(truck3, distances, addresses)

    delivery_manager1.delivering_packages()

    delivery_manager2.delivering_packages()

    delivery_manager3.delivering_packages()


if __name__ == "__main__":
    main()
