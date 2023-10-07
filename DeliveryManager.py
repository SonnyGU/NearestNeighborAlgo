import datetime

from Package import Package


# Manages the delivery of packages based on their proximity to the truck's current location.
class DeliveryManager:
    returned_to_hub = False  # initialize the flag

    def __init__(self, truck, distances, addresses):
        # truck: The truck instance that will deliver packages.
        # - distances: A 2D list representing distances between addresses.
        # - addresses: A list of addresses where each address has a unique ID.
        self.truck = truck
        self.distances = distances
        self.addresses = addresses

    # Calculate the distance between two address IDs.
    def get_distance_between_addresses(self, x, y):
        distance = self.distances[x][y]
        if distance == '':
            distance = self.distances[y][x]
        return float(distance)

    # Retrieve the ID for a given address
    @staticmethod
    def get_address_id_from_literal(address, addresses):
        for row in addresses:
            if address in row[2]:
                return int(row[0])

    def delivering_packages(self):
        #  Initialize an 'on_truck' list
        on_truck = [Package.get_by_id(pkg_id) for pkg_id in self.truck.packages]

        #  Empty the truck's package list
        self.truck.packages = []

        #  Delivery loop
        while on_truck:
            #  Find the closest package
            closest_package = None
            closest_distance = float('inf')
            for package in on_truck:
                distance = self.get_distance_between_addresses(
                    self.get_address_id_from_literal(self.truck.current_location, self.addresses),
                    self.get_address_id_from_literal(package.street, self.addresses)
                )
                if distance < closest_distance:
                    closest_distance = distance
                    closest_package = package

            # If no closest package was found (though unlikely), break the loop
            if not closest_package:
                break

            #  Update truck details
            self.truck.mileage += closest_distance
            time_to_add = datetime.timedelta(hours=closest_distance / self.truck.speed)
            self.truck.time += time_to_add
            self.truck.current_location = closest_package.street

            # 6. Update package details
            closest_package.deliver_time = self.truck.time
            if closest_package.depart_time is None:
                closest_package.depart_time = self.truck.depart_time

            closest_package.truck_name = self.truck.name
            # 7. Remove delivered package from 'on_truck' list
            on_truck.remove(closest_package)

        if not DeliveryManager.returned_to_hub:  # Check the flag here
            hub_address_id = self.get_address_id_from_literal("4001 South 700 East", self.addresses)
            distance_to_hub = self.get_distance_between_addresses(
                self.get_address_id_from_literal(self.truck.current_location, self.addresses),
                hub_address_id
            )

            # Update truck details for return to hub
            self.truck.mileage += distance_to_hub
            time_to_add = datetime.timedelta(hours=distance_to_hub / self.truck.speed)
            self.truck.time += time_to_add
            self.truck.current_location = "4001 South 700 East"

            self.returned_to_hub = True  # Set the flag to True after the truck returns
