# Exercise 6: Brute Force Attack - 30 Marks
# Write a program that simulates a password entry system. The correct password
# is defined as 12345. The program should keep asking the user to enter the

# 3

# password until they provide the correct one.
# Basic Requirements:
# 1. Define the correct password.
# 2. Use a while loop to repeatedly ask the user for the password until the
# correct one is entered.
# 3. Output an appropriate message when the correct password is entered.
# Optional Requirements:
# Modify the program to include a maximum of 5 password attempts. If the
# user enters the wrong password, inform them of the remaining attempts. If the
# maximum number of attempts is reached, inform the user that the authorities
# have been alerted.

correct_password = "12345" # correct password is defined as a string since there is no comparison operators in the program


max_attempts = 5 # maximum number of allowed attempts
attempts = 0 # counter for tracking the number of attempts

print("-----------------------")
print("-- PASSWORD ENTRY --")
print("-----------------------")

while attempts < max_attempts: # start a while loop to repeatedly ask for the password
    print("Enter a 5 digit password to gain access.") # displays to tell us what the user should do
    password = input("Enter the password: ") # User input for the correct password
    
    if password == correct_password: # check if the entered password is correct 
        print("Access granted, Welcome!")
        print("-----------------------")
        print("-- ACCESS GRANTED --")
        print("-----------------------")
        break # exit the loop if the correct password is entered
    else:
        attempts += 1 # adds 1 to the counter

        remaining_attempts = max_attempts - attempts # calculates and informs the user of how many attempts remaining
        if remaining_attempts > 0:
            print(f"Incorrect password, You have {remaining_attempts} attempts remaining.")
        else:
            print(f"Maximum amount of attempts reached, The authorities have been alerted")
            print("-----------------------")
            print("-- ACCESS DENIED --")
            print("-----------------------")
        