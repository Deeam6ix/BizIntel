import json
import os
import re
import products_and_services

def main():
    record_sale()
    
def record_sale():
    record_sale.man()
    try:
        print("\n=== 🧾 New Sale Record ===")
        # Step 1: Get customer details
        customer_name = input("Customer name: ").strip()
        customer_surname = input("Customer surname: ").strip()
        # Step 2: Validate phone number
        while True:
            customer_phone_number = input("Customer phone number (+27...): ").strip()
            if re.fullmatch(r'\+27[6-8]\d{8}', customer_phone_number):
                break
            else:
                print("❌ Invalid phone number. Try again (e.g. +27821234567)")
        # Step 3: Validate postal code
        while True:
            customer_postal_code = input("Customer Postal Code: ").strip()
            if re.fullmatch(r'[1-9]\d{3}', customer_postal_code):
                break
            else:
                print("❌ Invalid postal code. Must be 4 digits and not start with 0.")

        # Step 4: Search for product/service to sell
        print("\n🔍 Now searching for a product or service to sell: ")
        product = products_and_services.search_product_or_service(return_result=True)
        if not product:
            print("❌ No product selected. Sale cancelled.")
            return

        # Step 5: Prepare sale record
        sale_record = {
            "customer_name": f"{customer_name} {customer_surname}",
            "phone": customer_phone_number,
            "postal_code": customer_postal_code,
            "product": product
        }
        # Step 6: Log to sales.json
        save_sale_to_file(sale_record)
        # Step 7: Print receipt
        print("\n🧾 === RECEIPT ===")
        print(f"👤 Customer: {sale_record['customer_name']}")
        print(f"📞 Phone   : {sale_record['phone']}")
        print(f"🏠 Postal  : {sale_record['postal_code']}")
        print("💼 Product/Service Sold:")
        print(f"   📦 Name    : {product['name'].title()}")
        print(f"   💰 Price   : R{product['price']:.2f}")
        print(f"   🔢 Barcode : {product['barcode']}")
        print("✅ Sale successfully recorded.\n")

    except ValueError:
        print("⚠️ Invalid input. Please enter correct values.")
    except FileNotFoundError:
        print("⚠️ Required file not found.")
    except json.JSONDecodeError:
        print("⚠️ File format error. Could not read data.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

def save_sale_to_file(sale):
    filename = "sales.json"
    # Load existing sales
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                sales = json.load(f)
            except json.JSONDecodeError:
                sales = []
    else:
        sales = []
    # Append the new sale
    sales.append(sale)
    # Save back to file
    with open(filename, "w") as f:
        json.dump(sales, f, indent=4)
        
if __name__=="__main__":
    main()