import re
import os
import json
import csv

def main():
    user_info()

def user_info():
    while True:
        user_choice=input("Would you like to\n" 
        "1.Sign in?\n" 
        "2.Create a account?\n"
        "3.Exit\n")
        if user_choice=="1":
            ...
        elif user_choice=="2":
            user_choice_two()
        else:
            False break

def user_choice_two():
    try:    #Gets user input
            name=input("Please insert your name: ")
            surname=input("Please insert your surname: ")
            user_name=input("Please insert your username: ")
            password=input("Please insert your password: ")
            
            users_info_file()
    
        except KeyboardInterrupt:
            print("Input was interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        except ValueError:
            print("Please enter a valid character or word.")
        except EOFError:
            print("Control commands are not allowed e.g(CRTL+D,CRTL+Z)")
    
def user_info_file():
    # Organize user data
            user_data = {
                "name": name,
                "surname": surname,
                "username": user_name,
                "password": password,
            }
            #Save to jason
            json_file= "users_login.json" #creates name
            all_users=[] #creates a list to store everything
            
            #if the file exists open and load data
            if os.path.exists(json_file):
                with open(json_file,"r")as file:
                    try: #Try to read existing user data from the json file
                        all_users=json.load(file)
                    except json.JSONDecodeError:
                        #If we have a empty or invalid file, then start with a empty list
                        all_users=[]
            #Adds new users data to the list
            all_users.append(user_data)
            #Re write the updated list on json file
            with open(json_file,"w") as file:
                #nicely saves all users w a indentation 
                json.dump(all_users, file, indent=4)
            return "Thank you, User information has been saved successfully."       
            
            #Save to Csv
            csv_file="users_login.csv"
            file_exists=os.path.isfile(csv_file)
            with open(csv_file, "a",newline="")as file:
                #Creates a csv writer from the dictionary
                writter=csv.Dictwriter(file, filenames=user_data.keys())
                if not file_exists: #If the file is new write the header first
            #Otherwise write ghe data on a new row
            writer.writerow(user_data)
            
            
if __name__=="__main__":
    main()

