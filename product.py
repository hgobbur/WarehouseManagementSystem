# product.py

class Product:
    def __init__(self, sku, name, category, unit, low_stock_threshold=10):
        self.sku = sku
        self.name = name
        self.category = category
        self.unit = unit
        self.low_stock_threshold = low_stock_threshold

    def __str__(self):
        return f"[{self.sku}] {self.name} ({self.category}) - Unit: {self.unit}, Low stock threshold: {self.low_stock_threshold}"
