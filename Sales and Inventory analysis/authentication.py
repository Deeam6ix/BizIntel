import re          # For future use: can be used for validating inputs like strong passwords
import os          # Used to check if files exist (e.g., JSON or CSV)
import json        # Used to read/write structured data to/from JSON files
import csv         # Used to read/write user info in CSV (spreadsheet-like) format
import sales

# Entry point of the program
def main():
    user_info()  # Start the user interaction menu

# Menu to either sign in, create an account, or exit
def user_info():
    while True:
        user_choice = input("Would you like to:\n" 
                            "1. Sign in\n" 
                            "2. Create an account\n"
                            "3. Exit\n"
                            "Enter your choice (1/2/3): ")

        # Placeholder for sign-in (not yet implemented)
        if user_choice == "1":
            if not user_choice_one():  # Call the new function and check result
                print("Redirecting to account creation...")
                user_choice_two()

        # If user chooses to create an account
        elif user_choice == "2":
            user_choice_two()
            user_choice_one()

        # If user chooses to exit the program
        elif user_choice == "3":
            print("Goodbye!")
            break

        # Any other input is considered invalid
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# This function allows the user to log in by checking their credentials
# against the existing JSON and CSV databases.
def user_choice_one():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # ----------- Check JSON file first -----------
    json_file = "users_login.json"
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            try:
                users = json.load(file)  # Load all users from JSON
                for user in users:
                    # If both username and password match, grant access
                    if user["username"] == username and user["password"] == password:
                        print(f"✅ Welcome back, {user['name']} {user['surname']}!")
                        return True
            except json.JSONDecodeError:
                pass  # If JSON is empty or corrupt, skip to next check

    # If no match found in either file
    print("❌ No matching user found. Please create an account.")
    return False
    
# Function to collect user information for account creation
def user_choice_two():
    try:
        # Prompt the user for basic account details
        name = input("Please insert your name: ")
        surname = input("Please insert your surname: ")
        user_name = input("Please insert your username: ")

        while True:
            password = input("Please insert your password: ")

            # Validate all conditions in a single if statement using re.search()
            if (
                len(password) >= 8 and                                   # ✅ Minimum 8 characters
                re.search(r"[a-z]", password) and                        # ✅ At least one lowercase letter
                re.search(r"[A-Z]", password) and                        # ✅ At least one uppercase letter
                re.search(r"[0-9]", password) and                        # ✅ At least one digit
                re.search(r"[!@#$%^&*(),.?\":{}|<>_\-\[\]\\\/;'+=~`]", password)  # ✅ At least one special character
            ):
                print("✅ Password is valid and secure.")
                break  # Exit the loop once a valid password is entered

            else:
                # If any condition fails, print general message 
                print("❌ Password must be at least 8 characters long, and include:\n"
                      "- at least one uppercase letter\n"
                      "- at least one lowercase letter\n"
                      "- at least one number\n"
                      "- at least one special character (e.g. @, #, $, %)")

        # Send all data to the saving function
        user_info_file(name, surname, user_name, password)

    # Catch when the user manually interrupts input (Ctrl+C)
    except KeyboardInterrupt:
        print("\nInput was interrupted by user.")

    # Catch when the user enters an EOF command (Ctrl+D or Ctrl+Z)
    except EOFError:
        print("\nControl commands are not allowed (e.g., CTRL+D, CTRL+Z).")

    # Catch general value issues, although input() returns strings
    except ValueError:
        print("\nPlease enter valid characters.")

    # Catch any other unexpected error
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Function to save user information to both JSON and CSV formats
def user_info_file(name, surname, user_name, password):
    # Combine all user input into a dictionary
    user_data = {
        "name": name,
        "surname": surname,
        "username": user_name,
        "password": password
    }

    # ---------- JSON Section ----------
    json_file = "users_login.json"  # File name to store JSON data
    all_users = []  # Will store all user entries as a list of dictionaries

    # Check if the JSON file already exists
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            try:
                # Load all existing users from the file
                all_users = json.load(file)
            except json.JSONDecodeError:
                # If the file is empty or broken, reset to empty list
                all_users = []

    # Add the current user's data to the list
    all_users.append(user_data)

    # Overwrite the JSON file with the updated user list
    with open(json_file, "w") as file:
        json.dump(all_users, file, indent=4)  # Write with indentation for readability

    print("✅ User information saved successfully to JSON.")

    # ---------- CSV Section ----------
    csv_file = "users_login.csv"  # File name to store CSV data
    file_exists = os.path.isfile(csv_file)  # Check if it already exists (for headers)

    # Open the CSV file in append mode
    with open(csv_file, "a", newline="") as file:
        # Use the dictionary keys as CSV headers
        writer = csv.DictWriter(file, fieldnames=user_data.keys())

        # If file is new, write headers first
        if not file_exists:
            writer.writeheader()

        # Write the actual user data as a new row
        writer.writerow(user_data)

    print("✅ User information saved successfully to CSV.")

# Makes sure the program only runs if this script is executed directly
if __name__ == "__main__":
    main()

