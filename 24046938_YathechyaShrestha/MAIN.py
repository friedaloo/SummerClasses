from read import load_products
from write import display_products
from operations import process_sale, save_products, restock_products

# Main program: loads product data and provides a menu to manage inventory (display, sell, restock, or exit)
if __name__ == "__main__":
    products = load_products()  # Load products from products.txt into a list
    while True:
        # Display menu options for inventory management
        print("\n1. Display Products")
        print("2. Process Sale")
        print("3. Restock Products")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                display_products(products)  # Show current product inventory
            elif choice == '2':
                process_sale(products)  # Process a customer sale and update inventory
            elif choice == '3':
                restock_products(products)  # Restock products from a supplier
            elif choice == '4':
                save_products(products)  # Save changes to products.txt
                print("Exiting program. Changes saved.")
                break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")