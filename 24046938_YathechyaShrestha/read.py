# Loads product data from products.txt into a list of dictionaries for inventory management
def load_products(filename="products.txt"):
    product_list = []

    # Helper function to remove leading and trailing spaces from text
    def space(i):
        while i and i[0] == ' ':
            i = i[1:]
        while i and i[-1] == ' ':
            i = i[:-1]
        return i

    file = open(filename, 'r')
    for line in file:
        parts = line.split(',')  # Split CSV line into parts

        if len(parts) < 5:
            continue  # Skip invalid or incomplete lines

        # Clean and extract product details
        product_id = space(parts[0])
        name = space(parts[1])
        brand = space(parts[2])
        quantity = space(parts[3])
        cost = space(parts[4])
        origin = space(parts[5].replace('\n', ''))

        # Add product as a dictionary to the list
        product_list.append({
            'id': product_id,
            'name': name,
            'brand': brand,
            'quantity': int(quantity),
            'cost': int(cost),
            'origin': origin
        })

    file.close()
    return product_list