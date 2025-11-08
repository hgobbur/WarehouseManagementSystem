# location.py

class Location:
    def __init__(self, location_id, warehouse, aisle, bin_code):
        self.location_id = location_id
        self.warehouse = warehouse
        self.aisle = aisle
        self.bin_code = bin_code

    def __str__(self):
        return f"Location {self.location_id} - {self.warehouse} (Aisle: {self.aisle}, Bin: {self.bin_code})"
