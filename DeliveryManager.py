import datetime

from Package import Package


class DeliveryManager:
    def __init__(self, truck, distances, addresses):
        self.truck = truck
        self.distances = distances
        self.addresses = addresses

    def get_distance_between_addresses(self, x, y):
        distance = self.distances[x][y]
        if distance == '':
            distance = self.distances[y][x]
        return float(distance)

    @staticmethod
    def get_address_id_from_literal(address, addresses):
        for row in addresses:
            if address in row[2]:
                return int(row[0])

    @staticmethod
    def find_nearest_package_address(current_address, addresses, distances):
        current_address_id = DeliveryManager.get_address_id_from_literal(current_address, addresses)
        closest_distance = float('inf')
        closest_package = None

        for package in addresses:
            package_address = package[1]
            package_address_id = DeliveryManager.get_address_id_from_literal(package_address, addresses)
            if package_address == current_address:
                continue  # skip comparing the same addresses
            distance = distances[current_address_id][package_address_id]

            if distance < closest_distance:
                closest_distance = distance
                closest_package = package

                return closest_package[1]

    def delivering_packages(self):
        not_delivered = [Package.get_by_id(packageID) for packageID in self.truck.packages]
        delivered = []

        while not_delivered:
            current_address = self.truck.current_location

            # Calculate distances for all undelivered packages
            distances = [
                (package, self.get_distance_between_addresses(
                    self.get_address_id_from_literal(current_address, self.addresses),
                    self.get_address_id_from_literal(package.street, self.addresses)
                )) for package in not_delivered
            ]

            # Sort packages based on distance
            distances.sort(key=lambda x: x[1])

            # Pick the closest package
            next_package, distance = distances[0]

            self.truck.mileage += distance
            self.truck.current_location = next_package.street
            time_to_add = datetime.timedelta(hours=distance / self.truck.speed)
            self.truck.time += time_to_add

            delivered.append(next_package)
            not_delivered.remove(next_package)
