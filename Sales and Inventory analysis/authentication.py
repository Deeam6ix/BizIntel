import re

def main():
    user_info()

def user_info():
    user_choice=input("Would you like to\n" 
    "1.Sign in?\n" 
    "2.Create a account?\n")
    if user_choice=="1":
        ...
    elif user_choice=="2":
        try:
            name=input("Please insert your name: ")
            surname=input("Please insert your surname: ")
            user_name=input("Please insert your username: ")
            password=input("Please insert your password: ")
        except KeyboardInterrupt:
            print("Input was interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        except ValueError:
            print("Please enter a valid character or word.")
        except EOFError:
            print("Control commands are not allowed e.g(CRTL+D,CRTL+Z)")
    """
    -if there is a name 
    -check if name is already in the system
    -check if
    """

if __name__=="__main__":
    main()

