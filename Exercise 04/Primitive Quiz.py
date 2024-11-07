# Exercise 4: Primitive Quiz - 30 Marks
# In this exercise, you’ll create a simple program that asks the user a question,
# evaluates their answer, and provides feedback.
# Steps:
# 1. Write a program that asks the user “What is the capital of France?” and
# waits for their response.
# 2. If the user’s answer is correct (i.e., “Paris”), the program should print a
# message saying the answer is correct.
# 3. If the answer is incorrect, the program should print a message saying the
# answer is wrong.

Question_1 = input("What is the capital of france?: ")  # asks the user to input the capital of france

if Question_1 == "Paris":  # if condition using equals to condition, to check if our answer is equal to paris or not
    print("Your answer is correct!") # displays our answer is correct
else: # executes the code if our answer is wrong
    print("Your answer is wrong.") # displays our answer is wrong
