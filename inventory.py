import re
import json
import os
import record_sale
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
    record_sale.main()


        
if __name__=="__main__":
    main()