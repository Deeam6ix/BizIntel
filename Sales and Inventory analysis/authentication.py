import re
import os
import json
import csv

# Entry point of the program
def main():
    user_info()

# Presents the user with sign-in, account creation, or exit options
def user_info():
    while True:
        user_choice = input("Would you like to\n" 
                            "1. Sign in?\n" 
                            "2. Create an account?\n"
                            "3. Exit\n")
        if user_choice == "1":
            pass  # Placeholder for sign-in logic
        elif user_choice == "2":
            user_choice_two()
        elif user_choice == "3":
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Handles user account creation
def user_choice_two():
    try:
        # Get user input
        name = input("Please insert your name: ")
        surname = input("Please insert your surname: ")
        user_name = input("Please insert your username: ")
        password = input("Please insert your password: ")

        # Save the user information
        user_info_file(name, surname, user_name, password)

    except KeyboardInterrupt:
        print("\nInput was interrupted by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    except ValueError:
        print("\nPlease enter a valid character or word.")
    except EOFError:
        print("\nControl commands are not allowed (e.g., CTRL+D, CTRL+Z).")

# Saves user information to both JSON and CSV files
def user_info_file(name, surname, user_name, password):
    # Organize user data into a dictionary
    user_data = {
        "name": name,
        "surname": surname,
        "username": user_name,
        "password": password
    }

    # ----- Save to JSON -----
    json_file = "users_login.json"
    all_users = []

    # Load existing JSON data if the file exists
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            try:
                all_users = json.load(file)
            except json.JSONDecodeError:
                all_users = []  # If JSON is empty or corrupt, start with an empty list

    # Add the new user data to the list
    all_users.append(user_data)

    # Write updated user list back to the JSON file
    with open(json_file, "w") as file:
        json.dump(all_users, file, indent=4)  # Nicely formatted with indentation

    print("Thank you, user information has been saved successfully (JSON).")

    # ----- Save to CSV -----
    csv_file = "users_login.csv"
    file_exists = os.path.isfile(csv_file)

    # Open the CSV file in append mode
    with open(csv_file, "a", newline="") as file:
        # Create a CSV writer using dictionary keys as fieldnames
        writer = csv.DictWriter(file, fieldnames=user_data.keys())

        # If file is new, write headers first
        if not file_exists:
            writer.writeheader()

        # Write the user's data to a new row
        writer.writerow(user_data)

    print("Thank you, user information has been saved successfully (CSV).")

# Ensures main() only runs when this script is executed directly
if __name__ == "__main__":
    main()

