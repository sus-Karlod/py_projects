import random

def get_random_no():
    secret_no = random.randint(1,100)
    return secret_no

def get_user_guess():
    num = int(input("Guess the number between 1 to 100 : "))
    return num

def check_guess(user_guess, random_no):
    difference = abs(user_guess - random_no)

    if user_guess == random_no:
        return("You guessed it correct, congrats..! ")
    elif user_guess > random_no:
        if difference >= 50:
            return("The guessed number is much higher, try again")
        elif difference > 11:
            return("The guessed number is higher, try again")
        else:
            return("The guessed is number slightly higher, try again")
        
    elif user_guess < random_no:
        if difference >= 50:
            return("The guessed number is much lower, try again")
        elif difference > 11:
            return("The guessed number is lower, try again")
        else:
            return("The guessed number is slightly lower, try again")


secret_no = get_random_no()

while True:
    guess = get_user_guess()
    result = check_guess(guess, secret_no)
    print(result)

    if guess == secret_no:
        again = input("Do you want to play again? (yes/no) :" ).lower()
        if again != "yes":
            print("Thanks for playing the game!")
            break
        else:
            secret_no = get_random_no