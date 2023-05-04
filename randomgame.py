import random


upper_bound = input("Enter a number: ")

if upper_bound.isdigit():
    upper_bound = int(upper_bound)
else:
    print("Please enter a digit next time. ")

random_number = random.randint(0,upper_bound)

guess_count = 0

while True:
    guess_count += 1

    user_guess = input("Enter a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("Enter a digit next time!")
        continue

    if user_guess == random_number:
        print("Your guess is correct!")
        break
    elif user_guess > random_number:
        print("Your guess is above the correct answer!")
    else:
        print("You are below the correct answer!")






