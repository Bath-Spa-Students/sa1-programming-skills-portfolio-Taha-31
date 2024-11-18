# string concatenation through variables

message_1 = "hello " + "world"
print(message_1)

message_2 = "hello" + " " + "world"
print(message_2) # this message uses a seperate string for space and message 1 uses the space in the string itself

message_3 = "i" + " " + "love" + " " + "pizzas!"
print(message_3)

message_4 = "i " + "love " + "pizzas!!"
print(message_4) # this message has spaces in the strings whereas message_3 had seperate strings just for the space like " "