# utils.py

import random
import datetime

def generate_id(prefix):
    """
    Generate ID like: SKU123, LOC456, TXN789
    """
    return f"{prefix}{random.randint(100,999)}"

def current_timestamp():
    """
    Return current datetime string.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")