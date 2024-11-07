# Advanced Requirements:
# Have the user input their name, hometown, and age instead of hardcoding the
# values. Try giving both your first and second name when asked for your name.
# What happens? How can you handle multiple words in Python? Test the
# program by entering a string value for age (e.g., “twenty”). What happens?
# How can you prevent this issue?

# Advanced Requirement

bio = {"Name": "",
       "Hometown": "",
       "Age": ""} # dictionary with empty values for Name, Hometown, and Age

is_running = True # control variable to keep the program running until valid input is provided

print("---- BIOGRAPHY ----")

while is_running: # start a loop to prompt for user information until valid input is given
    print("Enter user information!") 
    first_name = input("Enter your first name: ") # Asks the user to input their first name
    if first_name.isalpha(): # checks if first name contains only alphabetic characters or not
        second_name = input("Enter your second name: ") # asks the user to input second name
        if second_name.isalpha(): # checks if second name contains only alphabetic characters or not
            hometown = input("Enter your hometown: ") # Asks the user to input their hometown
            if hometown.isalpha(): # checks if hometown name contains only alphabetic characters or not
                age = input("Enter your age: ") # asks the user to input age
                if age.isdigit(): # checks if age is a number 
                    bio.update({"Name": first_name + " " + second_name, "Hometown": hometown, "Age": age}) # update dictionary with our inputs
                    print(f"Name: {bio.get("Name")} \nHometown: {bio.get("Hometown")} \nAge: {bio.get("Age")}") # displays information from the dictionary
                    is_running = False # exit loop since all information is valid
                else:  
                    print("Age should be a number.") # error message if age is not a number
                    print("Please enter your information again")
            else:
                print("Hometown cannot be in digits.") # error message if hometown contains digits
                print("Please enter your information again!")
        else:
            print("Name cannot be in digits.") # error message if second name contains digits
            print("Please enter your information again!")
    else:
        print("Name cannot be in digits.") # error message if first name contains digits
        print("Please enter your information again!")
