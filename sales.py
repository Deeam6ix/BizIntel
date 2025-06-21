def main():
    welcome_message()
    inventory_dashboard()

def welcome_message():
    box = """
╔══════════════════════════════════════════════╗
║                                              ║
║           Welcome to BizIntel Pro!           ║
║                                              ║
║  Empowering Smart Business Decisions with    ║
║      Data-Driven Intelligence and Insight    ║
║                                              ║
║      💼 Optimize. 📊 Analyze. 🚀 Grow.      ║
║                                              ║
║   Thank you for choosing us as your partner  ║
║       in business innovation and success.    ║
║                                              ║
╚══════════════════════════════════════════════╝
"""

    # Width of your desired print area (e.g., 100 characters)
    for line in box.splitlines():
        print(f"{line:^100}")

    
def inventory_dashboard():
    menu = """
╔════════════════════════════════════════════════════╗
║                                                    ║
║             📦 INVENTORY DASHBOARD MENU            ║
║                                                    ║
║         Choose from the options below:             ║
║                                                    ║
║     1. 📈 KPI Tracking                             ║
║     2. 📊 Inventory Analysis                       ║
║     3. 📉 Sale Trend Visualizations                ║
║     4. ❌ Exit                                     ║
║                                                    ║
║     [Coming Soon]                                  ║
║     7. Forecasting                                 ║
║     8. Stock Replenishment Automation              ║
║     9. Low Stock Alerts                            ║
║    10. Supplier Performance                        ║
║    11. Inventory Turnover Ratio                    ║
║    12. Product Heatmap                             ║
║                                                    ║
╚════════════════════════════════════════════════════╝
"""

    # Desired total width
    width = 100

    # Print centered menu and capture user choice
    for line in menu.strip().splitlines():
        print(f"{line:^{width}}")

    inventory_dashboard_choice = input(f"\n{'Please select an option: '
    :^{width}}")

    while True:
        if inventory_dashboard_choice == "1":
            inventory_choice_one()
        elif inventory_dashboard_choice == "2":
            inventory_choice_two()
        elif inventory_dashboard_choice == "3":
            inventory_choice_three()
        else: 
            return "Exiting..." ,False
    
def inventory_choice_one():
    ...

def inventory_choice_two():
    ...    

def inventory_choice_three():
    ...   
    

if __name__=="__main__":
    main()