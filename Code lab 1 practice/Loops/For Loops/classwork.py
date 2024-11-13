# Lets suppose i want to Print 10 numbers - as per previous practices -
# Through print functions ,  line by line Is it a Good practice ?
# Lets suppose i need to print hundred values ?
# If condition True then Loop Sarts 
# What happens if the condition not false - infinite loop 
# 80 % For Loop Use in loops , also named as counter control loop 
 
#For loop 
#  A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


  # Using the range Function with the for Loop

  for x in range(0,15):
      print (x)

for x in range(10):
     print (x)

# To improve readibility 

for x in range(0,15):
      print (x, end=",")
  
 # Normaly step count (1 increment ) 

for x in range (0,15,2):    # Count +2 
   print(x ,end=",")

# Count +5
for x in range (0,20,5):
      print(x,end=",")

# Activity  : Calculate square root of each number  in a range 

# Getting input from user - User Controlled Loop 

N= int (input("Enter max number for range :"))
for x in range (0,20,5):
      print(x,end=",")


# Running time Total 

sum =0 
for i in range(5):
    x=float(input("Enter Number :  "))
    sum +=x   # sum =sum +1 
print(sum)

# Augmented assigment operator 
# Slide 18 


# Loop control through sentinels value 

sum =0 
while True:
    x=float(input("Enter Number :  "))
    sum +=x   # sum =sum +1
    if x ==-1 :
        break 
print(sum)


#Nested Loops  -- A loop withon a loop

x= [1,2,3]
y=[4,5,6]
for i in x:
    for j in y:
        print (i,j)
# Another Example 

for i in range (2):   # 0,1,
    
      for j in range(3) :  #0,1,2
             print("outer loop" ,i , "Inner Loop" , j )
          