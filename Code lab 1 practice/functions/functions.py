# void function 

def greetings(): # function header
    print("hello world")

# calling function

# greetings() 

# local variable
def variables():
    message = "Hello students" # local variable, it only exists in the function itself
    print(message)

# calling function

# variables()

# print(message) # error is given since the variable is on in the function itself not outside of it.

def bio(): # defines the bio() function
    name = "taha"
    age = 18                # variables with same name can be saved multiple times if theyre used in different functions
    location = "Ajman"
    print(f"Name: {name} \nAge: {age} \nLocation: {location}")

# calling function

# bio()

def greetings_2():
    name = "taha"           # same name variable used, since variables inside functions are local variables
    print(f"Hello {name}!")

# calling function

# greetings_2()

def greetings_3(name):
    print(f"Hello {name}!")

greetings_3("taha") 