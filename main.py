# main.py

from manager import WarehouseManager
import report

def main():
    manager = WarehouseManager()

    while True:
        print("\n--- Warehouse Management Menu ---")
        print("1. Add Product")
        print("2. Add Location")
        print("3. Receive Inbound Shipment")
        print("4. Process Outbound Shipment")
        print("5. Transfer Stock")
        print("6. Adjust Inventory")
        print("7. View Reports")
        print("8. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter product name: ")
            category = input("Enter category: ")
            unit = input("Enter unit (e.g., pcs, kg): ")
            threshold = int(input("Enter low stock threshold: ") or 10)
            sku = manager.add_product(name, category, unit, threshold)
            print(f"Product added successfully. SKU: {sku}")

        elif choice == "2":
            warehouse = input("Enter warehouse name: ")
            aisle = input("Enter aisle: ")
            bin_code = input("Enter bin code: ")
            loc_id = manager.add_location(warehouse, aisle, bin_code)
            print(f"Location added successfully. ID: {loc_id}")

        elif choice == "3":
            sku = input("Enter SKU: ")
            loc = input("Enter location ID: ")
            qty = int(input("Enter quantity: "))
            manager.receive_inbound(sku, loc, qty)
            print("Inbound shipment processed.")

        elif choice == "4":
            sku = input("Enter SKU: ")
            loc = input("Enter location ID: ")
            qty = int(input("Enter quantity: "))
            manager.process_outbound(sku, loc, qty)
            print("Outbound shipment processed.")

        elif choice == "5":
            sku = input("Enter SKU: ")
            src = input("Enter source location ID: ")
            dest = input("Enter destination location ID: ")
            qty = int(input("Enter quantity: "))
            manager.transfer_stock(sku, src, dest, qty)
            print("Stock transferred.")

        elif choice == "6":
            sku = input("Enter SKU: ")
            loc = input("Enter location ID: ")
            qty = int(input("Enter new quantity: "))
            reason = input("Enter adjustment reason: ")
            manager.adjust_inventory(sku, loc, qty, reason)
            print("Inventory adjusted.")

        elif choice == "7":
            print("\n--- Reports Menu ---")
            print("1. Inventory Snapshot")
            print("2. Low Stock Report")
            print("3. Movement History")
            print("4. Location Report")

            r_choice = input("Enter choice: ").strip()
            if r_choice == "1":
                report.inventory_snapshot(manager)
            elif r_choice == "2":
                report.low_stock_report(manager)
            elif r_choice == "3":
                sku = input("Enter SKU to filter (or press Enter for all): ").strip() or None
                report.movement_history(manager, sku)
            elif r_choice == "4":
                loc = input("Enter location ID: ")
                report.location_report(manager, loc)
            else:
                print("Invalid report choice.")

        elif choice == "8":
            print("Exiting WMS. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
