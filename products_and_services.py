import random
import os
import json

def main():
    register_product_or_service()
    search_product_or_service()
    
def register_product_or_service():
    name=input("Product or Service Name: ")
    price=int(input("Product or Service Proce: ")
    
    existing_products=load_from_json()
    
    #Check if the product name already exits
    if any(product(["name"].lower() == name for product in existing_products):
        print("This product or service is already registered on the system.")
        break
    
    barcode=generated_barcode()
    product={
        "name":name,
        "price":price,
        "barcode":barcode,
        }
    # Add the new product to the list of existing ones
    existing_products.append(product)
    # Save the updated list back to the JSON file
    save_to_json(existing_products)
    # Notify the user that registration was successful
    print(f"✅ Registered successfully! Barcode: {barcode}")
    
    
def generate_barcode():
    while True:
        # Generate a list of 12 random digits for the EAN-13 base
        base_digits = [random.randint(0, 9) for _ in range(12)]
        # Calculate the EAN-13 check digit using the weighted sum formula
        checksum = sum(
            base_digits[i] if i % 2 == 0 else base_digits[i] * 3 for i in range(12)
        )
        # Get the check digit that makes the total divisible by 10
        check_digit = (10 - (checksum % 10)) % 10
        # Combine the 12 base digits and the check digit into one full barcode
        full_barcode = ''.join(map(str, base_digits)) + str(check_digit)
        # Load existing barcodes to ensure uniqueness
        existing = load_from_json()
        
        # If the generated barcode doesn't already exist, return it
        if not any(p["barcode"] == full_barcode for p in existing):
            return full_barcode

def load_from_json():
    filename="products.json"
    #check if the file alreayd exists 
    if os.path.exists(filenams):
        with open(filename,"r") as file:
            try: #Try to load and return the json data
                return json.load(file)
            except json.JSONDecodeError:
                #If the file is empty or invalid return empty list
                return []
    #If file doesn't exit, return empty list
    return []

def save_to_json(data):
    #Save the given product list into products.json with indentation for readability 
    with open("products.json","w")as file:
    json.dump(data,file,indent=4)
      
def search_product_or_service():
    name = input("Enter the product or service name to search: ").strip().lower()
    # Load all registered products
    products = load_from_json()
    # Try to find the product with a case-insensitive match
    for product in products:
        if product["name"].lower() == name:
            print("\n🔍 Product or Service Found:")
            print(f"📦 Name   : {product['name'].title()}")
            print(f"💰 Price  : R{product['price']:.2f}")
            print(f"🔢 Barcode: {product['barcode']}")
            return

    # If not found, display message
    print("❌ Product or service not found in the system.")
   
            
if __name__=="__main__":
    main()