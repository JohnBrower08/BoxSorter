import time
import random

# Constants
VALID_WEIGHT = (0.5, 1.0)  # Min, Max in lbs
VALID_DIMENSIONS = (6.0, 9.0)  # Min, Max in inches
SORT_LOCATIONS = {1: "Bin 1", 2: "Bin 2", 3: "Bin 3"}
REJECT_BIN = "Reject Bin"



# Mock functions
def read_sensor():
    """Simulates detecting a box."""
    return True

def generate_random_package():
    return {
        "id": f"PKG{random.randint(10000, 99999)}",  # Random 5-digit alphanumeric ID
        "weight": round(random.uniform(0.3, 1.1), 2),  # Random weight between 0.3 and 1.1 lbs
        "length": round(random.uniform(6.0, 9.5), 1),  # Random length between 6.0 and 9.5 inches
        "width": round(random.uniform(6.0, 9.0), 1),   # Random width between 6.0 and 9.0 inches
        "height": round(random.uniform(6.0, 9.0), 1),  # Random height between 6.0 and 9.0 inches
        "sort_code": random.choice([1, 2, 3, "Reject"])  # Random sort code or Reject
    }

def move_conveyor(state):
    """Simulates conveyor movement."""
    print(f"Conveyor {'started' if state else 'stopped'}.")

def divert_to_bin(bin_name):
    """Simulates diverting a package to a bin."""
    print(f"Package diverted to {bin_name}.")

def log_package(package_id, destination):
    """Logs the package ID and destination."""
    print(f"Logged: Package {package_id} -> {destination}")

# Main process
def sort_boxes():
    while True:
        # Step 1: Detect box
        if read_sensor():
            move_conveyor(False)  # Stop conveyor
            package = generate_random_package()  # Read barcode
            
            # Step 2: Validate package
            if not (VALID_WEIGHT[0] <= package["weight"] <= VALID_WEIGHT[1]) or \
               not (VALID_DIMENSIONS[0] <= package["length"] <= VALID_DIMENSIONS[1]) or \
               not (VALID_DIMENSIONS[0] <= package["width"] <= VALID_DIMENSIONS[1]) or \
               not (VALID_DIMENSIONS[0] <= package["height"] <= VALID_DIMENSIONS[1]):
                destination = REJECT_BIN
            else:
                destination = SORT_LOCATIONS.get(package["sort_code"], REJECT_BIN)
            
            # Step 3: Sort package
            divert_to_bin(destination)
            log_package(package["id"], destination)
            move_conveyor(True)  # Restart conveyor
            
            # Simulate delay
            time.sleep(1)

# Run the system
sort_boxes()
