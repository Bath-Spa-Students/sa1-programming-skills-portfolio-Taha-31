# simple if condition being used to ask the user to input values and then itll determine and tell you which one is greater. (uses elif)

print("Enter your 2 numbers and it will tell which one is greater!") # shows a print statement thatll tell you what the program is about
num_1 = int(input("Enter your first number: ")) # tells the user to inout first value
num_2 = int(input("Enter your second number: ")) # tells the user to input second value

if num_1 > num_2: # if condition using greater than condition to determine if your first value is greater than your second value or not
    print(f"Your first number {num_1} is greater than your second number {num_2}!") # prints to show that first value is more than the second value 
elif num_1 == num_2: # if condition using equals to condition incase the user enters 2 numbers of the same value
    print(f"Your two numbers entered are of the same value!")
elif num_2 > num_1: # if condition using greater than condition to determine if your second value is greater than your first value
    print(f"Your second number {num_2} is greater than your first number {num_1}!") # prints to show that the your second value is larger than first value

