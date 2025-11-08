# inventory.py

from datetime import datetime

class InventoryRecord:
    def __init__(self, sku, location_id, quantity):
        self.sku = sku
        self.location_id = location_id
        self.quantity = quantity

    def __str__(self):
        return f"SKU: {self.sku}, Location: {self.location_id}, Quantity: {self.quantity}"


class InventoryTransaction:
    def __init__(self, txn_id, txn_type, sku, qty, source_location=None, dest_location=None, timestamp=None, note=""):
        self.txn_id = txn_id
        self.txn_type = txn_type
        self.sku = sku
        self.qty = qty
        self.source_location = source_location
        self.dest_location = dest_location
        self.timestamp = timestamp if timestamp else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.note = note

    def __str__(self):
        return (f"[{self.txn_id}] {self.txn_type} - SKU:{self.sku} Qty:{self.qty} "
                f"From:{self.source_location or '-'} To:{self.dest_location or '-'} "
                f"At:{self.timestamp} Note:{self.note}")
