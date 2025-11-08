# Warehouse Management System (WMS)

A lightweight, educational **Warehouse Management System (WMS)** built in Python.  
This project simulates basic warehouse operations such as product management, inventory tracking, inbound/outbound processing, stock transfers, and reporting.

---

## Project Structure
wms_project/
│
├── manager.py # Core logic – manages products, locations, inventory, and transactions
├── product.py # Product model definition
├── location.py # Location model definition
├── inventory.py # Inventory transaction model
├── report.py # Reporting utilities (inventory snapshots, low stock, movement logs)
├── exceptions.py # Custom exception classes for error handling
├── utils.py # Helper functions (ID generation, timestamps, etc.)
└── main.py # Entry point / test script

---

## 🚀 Features

Add and manage products and warehouse locations  
Receive inbound and process outbound stock  
Perform stock transfers and quantity adjustments  
Record and view transaction history  
Generate inventory and low-stock reports  

