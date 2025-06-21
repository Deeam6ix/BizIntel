import sales
import authentication

def main():
    login()
    sales.welcome_message()
    sales.inventory_dashboard()

def login():
    account=input("Do you already have an account with us?\n"
    "1.Yes\n"
    "2.No\n\n"
    ":")
    if account=="1":
        authentication.user_choice_one()
    else:
        authentication.user_choice_two()
        print("\n\nPlease go ahead and login now.")
        authentication.user_choice_one()

if __name__=="__main__":
    main()