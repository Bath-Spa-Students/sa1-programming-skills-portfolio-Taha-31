#  string concatenation in print statement itself

print("hello " + "world") # string concat in print statement with space in the string itself that contains "hello "

print("i " + "love " + "gaming")

a = "minecraft"

print("i love", a, "so much" ) # print statement concatenating a variable and another string with commas which dont automatically put spaces

b = "roblox"

print("i play " + b + " everyday") #print statement concatenating using "+" but we have to manually add spaces either in a seperate string like " " or in 
#                                         the string itself like "i love playing " + a + "minecraft"

age = 17
print(f"My age is {age} years old!") #print statement with an f string that allows putting the variable in the string without seperating it with a comma or a "+" 