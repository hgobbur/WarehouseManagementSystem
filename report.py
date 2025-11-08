# report.py

def inventory_snapshot(manager):
    if not manager.inventory:
        print("📦 No inventory records yet.")
        return

    print("\n=== INVENTORY SNAPSHOT ===")
    for (sku, location_id), qty in manager.inventory.items():
        product = manager.products.get(sku)
        location = manager.locations.get(location_id)
        print(f"SKU: {sku} | {product.name if product else '?'} | "
              f"Location: {location_id} ({location if location else '?'}) | Qty: {qty}")


def low_stock_report(manager):
    print("\n=== LOW STOCK REPORT ===")
    found = False
    for sku, product in manager.products.items():
        total = manager.get_stock_level(sku)
        if total < product.low_stock_threshold:
            print(f"⚠️ {sku} | {product.name} | Stock: {total} | Threshold: {product.low_stock_threshold}")
            found = True
    if not found:
        print("✅ No low stock items.")


def movement_history(manager, sku=None):
    print("\n=== MOVEMENT HISTORY ===")
    if not manager.transactions:
        print("No transactions recorded yet.")
        return

    for txn in manager.transactions.values():
        if sku and txn.sku != sku:
            continue
        print(txn)


def location_report(manager, location_id):
    print(f"\n=== LOCATION REPORT: {location_id} ===")
    if location_id not in manager.locations:
        print("❌ Location not found.")
        return

    found = False
    for (sku, loc), qty in manager.inventory.items():
        if loc == location_id:
            product = manager.products.get(sku)
            print(f"SKU: {sku} | {product.name if product else '?'} | Qty: {qty}")
            found = True

    if not found:
        print("📦 No stock found at this location.")
