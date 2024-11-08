# Exercise 8: Simple Search - 30 Marks
# Write a program that searches for a specific string within a list of strings. The list
# is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
# , and your task is to search for “Sam”.
# Optional Requirements:
# 1. Allow the user to input the search term instead of using a predefined value.
# 2. Implement the search functionality based on user input.

names_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # list of the names as mentioned in the question

search = input("Enter the name you want to search for: ") # asks the user to input the name they're searching for

if search in names_list: 
    print(f"{search} was found in the list.") # if name is found, displays on the screen that the name youre looking for is in the list
else:
    print(f"{search} was not found in the list.") # if name isnt, displays on the screen that the name youre looking for is NOT in the list
