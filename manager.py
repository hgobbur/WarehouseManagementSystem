# manager.py

from product import Product
from location import Location
from inventory import InventoryTransaction
from exceptions import *
import utils


class WarehouseManager:
    def __init__(self):
        self.products = {}
        self.locations = {}
        self.inventory = {}      
        self.transactions = {}   

    def add_product(self, name, category, unit, low_stock_threshold=10):
        sku = utils.generate_id("SKU")
        product = Product(sku, name, category, unit, low_stock_threshold)
        self.products[sku] = product
        print(f"✅ Product added: {product}")
        return sku

    def add_location(self, warehouse, aisle, bin_code):
        location_id = utils.generate_id("LOC")
        location = Location(location_id, warehouse, aisle, bin_code)
        self.locations[location_id] = location
        print(f"✅ Location added: {location}")
        return location_id

    def receive_inbound(self, sku, location_id, qty, note=""):
        if sku not in self.products:
            raise ProductNotFoundError(f"Product {sku} not found.")
        if location_id not in self.locations:
            raise LocationNotFoundError(f"Location {location_id} not found.")
        if qty <= 0:
            raise InvalidQuantityError("Quantity must be positive.")

        key = (sku, location_id)
        self.inventory[key] = self.inventory.get(key, 0) + qty

        txn_id = utils.generate_id("TXN")
        txn = InventoryTransaction(txn_id, "INBOUND", sku, qty, dest_location=location_id, note=note)
        self.transactions[txn_id] = txn
        print(f"✅ Inbound received: {txn}")

    def process_outbound(self, sku, location_id, qty, note=""):
        if sku not in self.products:
            raise ProductNotFoundError(f"Product {sku} not found.")
        if location_id not in self.locations:
            raise LocationNotFoundError(f"Location {location_id} not found.")
        if qty <= 0:
            raise InvalidQuantityError("Quantity must be positive.")

        key = (sku, location_id)
        current_qty = self.inventory.get(key, 0)
        if current_qty < qty:
            raise InsufficientStockError(f"Not enough stock for {sku} at {location_id}.")

        self.inventory[key] = current_qty - qty

        txn_id = utils.generate_id("TXN")
        txn = InventoryTransaction(txn_id, "OUTBOUND", sku, qty, source_location=location_id, note=note)
        self.transactions[txn_id] = txn
        print(f"✅ Outbound processed: {txn}")

    def transfer_stock(self, sku, from_loc, to_loc, qty, note=""):
        if from_loc == to_loc:
            raise InvalidQuantityError("Source and destination locations cannot be the same.")

        self.process_outbound(sku, from_loc, qty, note=f"Transfer to {to_loc}. {note}")
        self.receive_inbound(sku, to_loc, qty, note=f"Transfer from {from_loc}. {note}")

        txn_id = utils.generate_id("TXN")
        txn = InventoryTransaction(txn_id, "TRANSFER", sku, qty, from_loc, to_loc, note=note)
        self.transactions[txn_id] = txn
        print(f"✅ Transfer complete: {txn}")

    def adjust_inventory(self, sku, location_id, new_qty, reason):
        if sku not in self.products:
            raise ProductNotFoundError(f"Product {sku} not found.")
        if location_id not in self.locations:
            raise LocationNotFoundError(f"Location {location_id} not found.")
        if new_qty < 0:
            raise InvalidQuantityError("New quantity cannot be negative.")

        key = (sku, location_id)
        old_qty = self.inventory.get(key, 0)
        self.inventory[key] = new_qty

        diff = new_qty - old_qty
        txn_id = utils.generate_id("TXN")
        txn = InventoryTransaction(txn_id, "ADJUSTMENT", sku, diff, source_location=location_id, note=reason)
        self.transactions[txn_id] = txn
        print(f"✅ Inventory adjusted: {txn}")

    def get_stock_level(self, sku, location_id=None):
        if sku not in self.products:
            raise ProductNotFoundError(f"Product {sku} not found.")

        if location_id:
            key = (sku, location_id)
            return self.inventory.get(key, 0)
        else:
            total = sum(qty for (s, _), qty in self.inventory.items() if s == sku)
            return total

    def list_transactions(self, filter_options=None):
        if not self.transactions:
            print("No transactions recorded yet.")
            return

        for txn in self.transactions.values():
            print(txn)
