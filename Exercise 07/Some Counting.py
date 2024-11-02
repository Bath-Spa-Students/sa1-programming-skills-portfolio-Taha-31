# Exercise 7: Some Counting - 20 Marks
# Use your newly acquired knowledge of the for loop to complete the following
# tasks. Print all values to the console in each case. * Write a loop that counts
# up from 0 to 50 in increments of 1. * Write a loop that counts down from 50 to
# 0 in decrements of 1. * Write a loop that counts up from 30 to 50 in increments
# of 1. * Write a loop that counts down from 50 to 10 in decrements of 2. * Write
# a loop that counts up from 100 to 200 in increments of 5. You may include all
# loops in a single project

print("--------------------------")
print("Couting up from 0 till 50!")
print("--------------------------")
for count_up_to_50 in range(0,51): # counts up from 0 till 50, we use 51 because the stop value in range is exclusive, so this includes 50
    print(count_up_to_50) 

print("-----------------------------------------------")
print("Couting down from 50 till 0 in increments of 1!")
print("-----------------------------------------------")
for count_down_to_0 in range(50, -1, -1): # counts down in reverse from 50 till 0, we use -1 because the stop value is exclusive, so this includes 0.
    print(count_down_to_0)

print("---------------------------")
print("Couting up from 30 till 50!")
print("---------------------------")
for count_up_from_30 in range(30, 51): # counts up from 30 till 50, 51 written because 51 is exclusive, we use 51 to include 50, as the stop value is exclusive.
    print(count_up_from_30)

print("------------------------------------------------")
print("Couting down from 50 till 10 in increments of 2!")
print("------------------------------------------------")
for count_down_to_10 in range(50, 9, -2): # counts down from 50 till 10 in increments of 2, we use 9 because the stop value is exclusive, so this includes 10
    print(count_down_to_10)

print("------------------------------------------------")
print("Couting up from 100 till 200 in increments of 5!")
print("------------------------------------------------")
for count_up_from_100 in range(100, 201, 5): # counts up from 100 till 200 in increments of 5, we use 201 to include 200, as the stop value is exclusive.
    print(count_up_from_100)