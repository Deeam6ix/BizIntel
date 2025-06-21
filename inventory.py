import re
import products_and_services

def main():
    inventory_choice_one()
    inventory_choice_two()
    inventory_choice_three()
    
def inventory_choice_one(): #KPI tracking
    record_sale()
    total_sales_revenue()
    sales_growth()
    quota_attainment()
    sales_region()

def inventory_choice_two():
    ...
def inventory_choice_three():
    ...
def total_sales_revenue():
    ...
def sales_growth():
    ...
def quota_attainment():
    ...
def sales_region():
    ...
    
def record_sale():
    try:
        customer_name=input("Customer name: ")
        customer_surname=input("Customer surname: ")
        while True:
            customer_phone_number=input("Customer phone number: ")
            if re.fullmatch(r'\+27[6-8]\d{8},customer_phone_number)):
                break
            else:
                print("Invalid phone number, try starting with (+27...)")
        while True:
            customer_postal_code=input("Customer Postal Code: ")
            if re.fullmatch(r'[1-9]\d{3}', customer_postal_code)):
                break
            else:
                print("Invalid postal code, please try again")
        #Product or service will be assigned price and barcode number
        while True:
            products_and_services.search_product_or_service()
    except:
        ...
        
if __name__=="__main__":
    main()