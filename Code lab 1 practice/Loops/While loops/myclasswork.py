# while loop = execute some code WHILE some condition remains true

name = input("Enter ur name: ")

while name == "":
   print("You did not enter your name")
   name = input("Enter your name: ")
print(f"Hello {name}")


age = int(input("Enter ur age: "))

while age < 0:
    print("Age cant be negative")
    age = int(input("Enter ur age: "))

print(f"Your are {age} years old!")

food = input("Enter a food you like boss (q to quit): ")

while not food == "q":
    print(f"You like {food}!")
    food = input("Enter another food you like boss (q to quit): ")

print("Bye!")

num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))

print(f"Your number is {num}!")