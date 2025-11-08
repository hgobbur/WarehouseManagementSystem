# exceptions.py

class ProductNotFoundError(Exception):
    pass

class LocationNotFoundError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass