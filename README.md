# NearestNeighborAlgo
1. Project Title
WGUPS Package Delivery System
2. Description
Designed for a package delivery system for the Western Governors University Parcel Service (WGUPS).

3. Features

**Efficient Package Delivery:**
-The system is designed for the efficient delivery of packages. It calculates optimized routes for the trucks to ensure that all packages are delivered as quickly and efficiently as possible.

**Custom Hash Table Implementation:**
  -A custom hash table is used for storing and managing package information, ensuring quick access times for retrieval, insertion, and deletion operations.

**Data Loading from CSV:**
The system has the ability to load package and location data from CSV files, making the import process seamless and straightforward.

**Truck Simulation:**
Trucks are simulated with various attributes such as mileage, departure time, speed, and current location. This contributes to the overall simulation of the package delivery process.

**Dynamic Package Status Tracking:**
Packages have statuses that change dynamically based on the truck's delivery progress. It allows real-time tracking of each package's delivery status.

**Handling Special Delivery Constraints:**
The system is capable of managing packages with special delivery constraints, such as specific delivery times or delayed availability, ensuring that all packages are delivered within their respective constraints.

**Route Optimization:**
The system calculates optimized delivery routes based on package destinations and special constraints to ensure that all packages are delivered efficiently.

**Comprehensive Package Information:**
The hash table stores comprehensive details about each package, including destination, delivery status, and any special delivery instructions or constraints.

**Robust Error Handling and Validation:**
The system includes error handling and validation features to ensure that operations such as package insertion, retrieval, and deletion are performed accurately and reliably.

**Flexible Capacity and Customizability:**
The system offers flexibility with adjustable hash table capacities, allowing it to handle various numbers of packages with ease.
For example, efficient delivery route calculation, hash table implementation for quick package access, etc.

5. Class Descriptions

1. **HashTable Class**
Purpose: Manages the storage, retrieval, and deletion of package information.
Key Methods:
_hash: Creates a hash value for a given key.
_probe: Finds an index in the hash table for a given key.
insert: Inserts a package into the hash table.
search: Searches for a package in the hash table using a key.
remove: Removes a package from the hash table using a key.
Attributes:
table: Stores packages and their details.
deleted: A marker to denote deleted entries.

3. **DataLoader Class**
Purpose: Handles the loading of data from external CSV files.
Key Methods:
load_csv: Loads data from a CSV file and returns it as a list.

4.** Truck Class**
Purpose: Represents a truck and its attributes necessary for delivering packages.
Key Methods:
__str__: Returns a string representation of the truck's status.
Attributes:
mileage: Keeps track of the total miles traveled.
depart_time: Stores the time when the truck departs.
packages: Holds the packages currently on the truck.
current_location: Represents the truck’s current location.
speed: Represents the speed at which the truck moves.
time: Stores the current time relative to the truck’s operations.
name: A name identifier for the truck****

5. **Package Class**
Description: Represents a package with various attributes necessary for delivery, and handles package status updates and data loading from a CSV file.
Attributes:
ID, street, city, state, zip_code, deadline, weight, notes, etc.
Methods:
__init__: Initializes package attributes.
__str__: Returns a string representation of the package.
status_update: Updates the status of a package based on time.
load_from_csv: Class method to load packages from a CSV file and store them in a hash table.
get_by_id: Class method to retrieve a package using its ID.

6. **DeliveryManager Class**
Description: Manages the delivery of packages, calculating distances, and updating the status and location of trucks and packages.
Attributes:
truck, distances, addresses, and a static attribute returned_to_hub.
Methods:
__init__: Initializes the delivery manager with a truck, distances, and addresses.
get_distance_between_addresses: Calculates the distance between two address IDs.
get_address_id_from_literal: Retrieves the ID for a given address.
delivering_packages: Manages the delivery process, finding the closest package, updating truck and package details, and handling the return of trucks to the hub.

