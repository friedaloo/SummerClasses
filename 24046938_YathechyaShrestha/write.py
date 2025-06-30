from utils import pad_right

# Displays the current product inventory in a formatted table with aligned columns
def display_products(products):
    print("\nCurrent Inventory:")
    print("-" * 70)
    print("ID    Name                Brand           Qty       Price     ")  # Table header
    print("-" * 70)
    for product in products:
        pid = product['id']
        name = product['name']
        brand = product['brand']
        qty = str(product['quantity'])
        price = str(product['cost'] * 2)  # Selling price is double the cost price

        # Align columns using padding
        pad_id = pad_right(pid, 6)
        pad_name = pad_right(name, 20)
        pad_brand = pad_right(brand, 15)
        pad_qty = pad_right(qty, 10)

        print(pad_id + pad_name + pad_brand + pad_qty + price)