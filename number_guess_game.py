import random
import time


def intro():    # Intro function that introduces the game and prompts for user name
    print("Welcome to number guessing game!\n")
    time.sleep(1)
    print("The game is simple, guess the number I'm thinking of and you win!\n")
    time.sleep(1)
    
    user_name = input("First, enter your first name: ")
    
    while True: # Loop that allows user to try again

        number = generate_number()
    
        user_guess(user_name, number)
    
        try_again = input("Try again? y/n : ").capitalize()

        if try_again == "N":
            print("Thanks for playing!\n")
            break
    



def generate_number(): # Function that generates the number 

    number = random.randint(1,10)
    
    return number

def user_guess(user_name,number): # Function collecting user guess 

    guess = int(input("Enter a number from 1-10: "))
    
    number_compare(guess,number,user_name)

    return guess

def number_compare(guess,number,user_name): # Function comparing generated number to user's guess

    if guess != number:
        print("I was thinking of the number: " , number)
        you_lose(number)
    elif guess == number:
        print(number)
        you_win(user_name)
    else:
        print("INVALID")


def you_lose(number): # Tells user they lost and prompts to try again
    print("Not quite, the correct number was: ", number)
    time.sleep(.5)


def you_win(user_name): # Tells user they won and prompts to try again
    user_name = user_name
    print("Congrats " + user_name + ", you win!")
    time.sleep(1)
    

intro()