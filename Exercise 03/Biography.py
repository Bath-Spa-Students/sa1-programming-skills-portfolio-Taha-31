# In this exercise, you’ll create a program that stores and prints your name, home-
# town, and age to the console using a Python dictionary.

# Steps:
# 1. Store the information (name, hometown, and age) as key-value pairs in a
# dictionary.
# 2. Print the values on separate lines using a single print() statement.
# 3. Use variables with appropriate data types for each piece of information.
# Advanced Requirements:
# Have the user input their name, hometown, and age instead of hardcoding the
# values. Try giving both your first and second name when asked for your name.
# What happens? How can you handle multiple words in Python? Test the
# program by entering a string value for age (e.g., “twenty”). What happens?
# How can you prevent this issue?

bio = {"Name": "Taha Bilal",
       "Hometown": "Pakistan",
       "Age": 17}

print(f"Name: {bio["Name"]} \nHometown: {bio["Hometown"]} \nAge: {bio["Age"]}")

# Advanced Requirement

bio = {"Name": "",
       "Hometown": "",
       "Age": ""} # dictionary with empty values for Name, Hometown, and Age

is_running = True # Control variable to keep the program running until valid input is provided

while is_running: # Start a loop to prompt for user information until valid input is given
    print("Enter user information!")  
    first_name = input("Enter your first name: ") #  User input for first name
    if first_name.isdigit(): # Check if first name contains digits or not
        print("Name cannot be in digits.")
        print("Please enter your information again!")
    else:
        second_name = input("Enter your second name: ") # User input for second name
        if second_name.isdigit(): # Check if second name contains digits or not
            print("Name cannot be in digits.")
            print("Please enter your information again!")
        else:
            hometown = input("Enter your hometown: ") # User input for hometown
            if hometown.isdigit(): # Check if hometown contains digits or not 
                print("Hometown cannot be in digits.")
                print("Please enter your information again!")
            else:
                age = input("Enter your age: ") # User input for age 
                if age.isdigit(): # check if age is a number 
                    bio.update({"Name": first_name + " " + second_name, "Hometown": hometown, "Age": age}) #  Update dictionary with our inputs
                    print("---- YOUR BIOGRAPHY ----")
                    print(f"Name: {bio["Name"]} \nHometown: {bio["Hometown"]} \nAge: {bio["Age"]}") # Display information from dictionary
                    is_running = False # Exit loop since all information is valid
                else:
                    print("Age should be a number.")
                    print("Please enter your information again")
    



