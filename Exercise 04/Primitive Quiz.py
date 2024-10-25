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

Question_1 = input("What is the capital of france?: ")  

if Question_1 == "Paris":  
    print("Your answer is correct!")
else:
    print("Your answer is wrong.")

# Advanced Requirements:

# Ignore Capitalization: Modify your program to accept answers regardless of
# the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
# correct). Multiple Questions: Extend the program into a quiz that asks for the
# capitals of 10 European countries. Provide feedback for each question.

questions = ("What is the capital of Germany?: ",
             "What is the capital of Denmark?: ",
             "What is the capital of Italy?: ",
             "What is the capital of France?: ",
             "What is the capital of Iceland?: ",
             "What is the capital of Ireland?: ",
             "What is the capital of Czech Republic?: ",
             "What is the capital of Sweden?: ",
             "What is the capital of United Kingdom?: ",
             "What is the capital of Spain?: ")  # stores 10 questions in a tuple called "questions"

answers = ("berlin", "copenhagen", "rome", "paris", "reykjavik", "dublin", "prague", "stockholm", "london",
           "madrid")  # stores correct answers in a tuple called "answers"
guesses = []  # list to store the user's guesses
score = 0  # sets score to 0
count = 0  # tracks the current question number

for question in questions:  # ;oops through and displays each question one by one
    print("----------------------------------")  # prints a line for visual separation
    print(question)  # prints the current question
    guess = input(
        "Enter your answer: ").lower()  # asks the user for an answer and converts it to lowercase to ignore capitalization
    guesses.append(guess)  # adds the user's answer to the "guesses" list
    if guess == answers[count]:  # Checks if the user's answer matches the correct answer in "answers" tuple
        score += 1  # increases score by 1 if the answer is correct
        print("CORRECT!")  # informs the user their answer is correct
    else:  # executes if the answer is incorrect
        print("INCORRECT!")  # informs the user their answer is incorrect
        print(f"{answers[count]} is the correct answer.")  # Displays the correct answer
    count += 1  # +1 to the count, so the counter can move to the next question

print("------------------")
print("     RESULTS      ")  # Displays "RESULTS" heading after all questions are answered
print("------------------")

print("answers: ", end="")  # prepares to print all correct answers on the same line
for answer in answers:  # loops through correct answers
    print(answer, end=" ")  # prints each answer in one line
print()  # creates a new line
print("guesses: ", end="")  # prepares to print all user guesses on the same line
for guess in guesses:  # loops through user guesses
    print(guess, end=" ")  # prints each guess in one line
print()  # creates a new line

score = int(score / len(questions) * 100)  # Calculates score as a percentage
print(f"Your score is: {score}%")  # displays the user's score as a percentage
