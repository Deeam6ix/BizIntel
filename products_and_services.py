import random     # For barcode digit generation
import os         # To check if file exists
import json       # For reading/writing JSON data

def main():
    # Run both registration and search
    register_product_or_service()
    search_product_or_service()

def register_product_or_service():
    # Ask user to enter product/service details
    name = input("Product or Service Name: ").strip().lower()

    try:
        price = float(input("Product or Service Price (e.g. 19.99): "))
    except ValueError:
        print("❌ Invalid price. Please enter a number.")
        return

    existing_products = load_from_json()

    # Check if the product name already exists
    if any(product["name"].lower() == name for product in existing_products):
        print("❌ This product or service is already registered on the system.")
        return

    # Generate a unique barcode
    barcode = generate_barcode()

    # Create the product dictionary
    product = {
        "name": name,
        "price": price,
        "barcode": barcode,
    }

    # Add the product and save to file
    existing_products.append(product)
    save_to_json(existing_products)

    # Confirmation
    print(f"✅ Registered successfully! Barcode: {barcode}")

def generate_barcode():
    # Keep generating until we get a unique barcode
    while True:
        # Generate 12 random digits
        base_digits = [random.randint(0, 9) for _ in range(12)]

        # Calculate EAN-13 check digit
        checksum = sum(
            base_digits[i] if i % 2 == 0 else base_digits[i] * 3
            for i in range(12)
        )
        check_digit = (10 - (checksum % 10)) % 10

        # Create full 13-digit barcode
        full_barcode = ''.join(map(str, base_digits)) + str(check_digit)

        # Ensure it's unique
        existing = load_from_json()
        if not any(p["barcode"] == full_barcode for p in existing):
            return full_barcode

def load_from_json():
    filename = "products.json"

    # If file exists, load and return data
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    # If file doesn't exist, return empty list
    return []

def save_to_json(data):
    # Save product list to products.json with nice formatting
    with open("products.json", "w") as file:
        json.dump(data, file, indent=4)

def search_product_or_service():
    # Ask for search term
    name = input("Enter the product or service name to search: ").strip().lower()
    
    # Load data
    products = load_from_json()

    # Search for product by name (case-insensitive)
    for product in products:
        if product["name"].lower() == name:
            print("\n🔍 Product or Service Found:")
            print(f"📦 Name   : {product['name'].title()}")
            print(f"💰 Price  : R{product['price']:.2f}")
            print(f"🔢 Barcode: {product['barcode']}")
            return

    # If not found
    print("❌ Product or service not found in the system.")

# Entry point of the program
if __name__ == "__main__":
    main()