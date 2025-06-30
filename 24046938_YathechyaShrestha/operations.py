from write import display_products

# Processes a customer sale: displays products, collects customer input, manages cart, updates inventory, and generates a sale invoice
def process_sale(products):
    display_products(products)  # Show available products
    customer_name = input("Enter customer name: ")

    cart = []  # Stores items purchased by the customer
    total_amount = 0  # Tracks total cost of items

    while True:
        product_id = input("Enter product ID: ")

        found = False
        for product in products:
            if product['id'] == product_id:
                found = True
                try:
                    quantity = int(input("Enter quantity: "))  # Get quantity to purchase
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
                    break

                if product['quantity'] < quantity:
                    print("Error: Not enough stock available!")
                    break

                free_items = quantity // 3  # Buy 3, get 1 free promotion
                total_items = quantity + free_items  # Total items including free ones
                price_per_item = product['cost'] * 2  # Selling price is twice the cost
                item_total = quantity * price_per_item  # Total cost for this item

                # Add item details to the cart
                cart.append({
                    'name': product['name'],
                    'brand': product['brand'],
                    'quantity': quantity,
                    'price': price_per_item,
                    'total': item_total,
                    'free': free_items
                })

                total_amount += item_total  # Update overall total

                # Deduct purchased and free items from inventory
                product['quantity'] -= total_items

                print("Item added to cart.")
                break

        if not found:
            print("Error: Product ID not found.")

        more_items = input("More items? Type 1 for yes, 2 for no: ")
        if more_items == '2':
            break

    if not cart:
        print("No items purchased. Sale cancelled.")
        return
    generate_invoice_sale(customer_name, cart, total_amount)  # Create sale invoice
    save_products(products)  # Save updated inventory

# Aligns text by adding spaces to the right until it reaches the specified length
def pad_right(text, length):
    text = str(text)
    while len(text) < length:
        text = text + ' '
    return text

# Aligns text by adding spaces to the left until it reaches the specified length
def pad_left(text, length):
    text = str(text)
    while len(text) < length:
        text = ' ' + text
    return text

# Generates a sale invoice with customer and item details, saves it to a text file, and displays it
def generate_invoice_sale(customer_name, cart, total_amount):
    timestamp = input("Enter invoice number or timestamp: ")
    filename = "invoice_" + timestamp + "_sale.txt"
    file = open(filename, 'w')

    # Invoice header: store details, invoice type, and customer name
    header = "===============================================\n"
    header += "        WeCare RETAIL STORE\n"
    header += "         Kathmandu, Nepal\n"
    header += "        Phone: +977-1-1234567\n"
    header += "===============================================\n"
    header += "Invoice Type: SALE\n"
    header += "Customer Name: " + customer_name + "\n"
    header += "-----------------------------------------------\n"
    header += "Product Name         Brand           Qty   Price    Total\n"
    header += "-----------------------------------------------\n"

    print(header)
    file.write(header)

    for item in cart:
        name = pad_right(item['name'], 20)  # Align product name
        brand = pad_right(item['brand'], 15)  # Align brand name
        qty = pad_left(item['quantity'], 5)  # Align quantity
        price = pad_left(item['price'], 8)  # Align price
        total = pad_left(item['total'], 8)  # Align total cost

        line = name + brand + qty + price + total
        print(line)
        file.write(line + "\n")

        if item['free'] > 0:
            free_line = "    (Free: " + str(item['free']) + " units)"  # Note free items
            print(free_line)
            file.write(free_line + "\n")

    # Invoice footer: total amount and thank you message
    footer = "-----------------------------------------------\n"
    footer += "Total Amount Due: Rs. " + str(total_amount) + "\n"
    footer += "===============================================\n"
    footer += "        THANK YOU FOR YOUR PURCHASE!\n"
    footer += "===============================================\n"

    print(footer)
    file.write(footer)
    file.close()
    print("Invoice generated: " + filename)

# Generates a restock invoice with supplier and item details, saves it to a text file, and displays it
def generate_invoice_restock(supplier, cart, total_amount):
    timestamp = input("Enter invoice number or timestamp: ")
    filename = "invoice_" + timestamp + "_restock.txt"
    file = open(filename, 'w')

    # Invoice header: store details, invoice type, and supplier name
    header = "===============================================\n"
    header += "         WeCare RETAIL STORE\n"
    header += "         Kathmandu, Nepal\n"
    header += "        Phone: +977-1-1234567\n"
    header += "===============================================\n"
    header += "Invoice Type: RESTOCK\n"
    header += "Supplier Name: " + supplier + "\n"
    header += "-----------------------------------------------\n"
    header += "Product Name         Brand           Qty   Cost     Total\n"
    header += "-----------------------------------------------\n"
    print(header)
    file.write(header)

    for item in cart:
        name = pad_right(item['name'], 20)  # Align product name
        brand = pad_right(item['brand'], 15)  # Align brand name
        qty = pad_left(item['quantity'], 5)  # Align quantity
        cost = pad_left(item['cost'], 8)  # Align cost
        total = pad_left(item['total'], 8)  # Align total cost
        line = name + brand + qty + cost + total
        print(line)
        file.write(line + "\n")

    # Invoice footer: total amount and thank you message
    footer = "-----------------------------------------------\n"
    footer += "Total Amount: Rs. " + str(total_amount) + "\n"
    footer += "===============================================\n"
    footer += "        THANK YOU FOR YOUR SUPPLY!\n"
    footer += "===============================================\n"
    print(footer)
    file.write(footer)
    file.close()
    print("Invoice generated: " + filename)

# Saves the updated product list to products.txt, overwriting the previous file
def save_products(products, filename="products.txt"):
    try:
        with open(filename, 'w') as file:
            for product in products:
                # Write product details in CSV format
                line = product['id'] + "," + product['name'] + "," + product['brand'] + "," + str(product['quantity']) + "," + str(product['cost']) + "," + product['origin'] + "\n"
                file.write(line)
    except Exception as e:
        print("Error saving products:", e)

# Manages restocking: displays products, collects supplier input, updates inventory, and generates a restock invoice
def restock_products(products):
    display_products(products)  # Show current inventory
    supplier = input("Enter supplier name: ")
    cart = []  # Stores restocked items
    total_amount = 0  # Tracks total cost of restocking

    while True:
        product_id = input("Enter product ID to restock: ")
        found = False
        for product in products:
            if product['id'] == product_id:
                found = True
                try:
                    quantity = int(input("Enter quantity to add: "))  # Get quantity to restock
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
                    break
                product['quantity'] += quantity  # Update inventory
                total_cost = quantity * product['cost']  # Calculate cost
                cart.append({
                    'name': product['name'],
                    'brand': product['brand'],
                    'quantity': quantity,
                    'cost': product['cost'],
                    'total': total_cost
                })
                total_amount += total_cost  # Update total cost
                print("Product restocked successfully.")
                break
        if not found:
            print("Error: Product ID not found.")
        more_items = input("More items to restock? Type 1 for yes, 2 for no: ")
        if more_items == '2':
            break

    if cart:
        generate_invoice_restock(supplier, cart, total_amount)  # Create restock invoice
        save_products(products)  # Save updated inventory
    else:
        print("No products restocked.")