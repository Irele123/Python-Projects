import random

game_continue="yes"

while game_continue == "yes":
    
    answer=random.randint(1,100)

    print("Welcome to the guessing game")
    print("I'm thinking of a number between 1 to 100")

    game_type=input("Choose a difficulty between easy and hard: ")

    if game_type == "easy":
        limit = 10

    else:
        limit = 5

    tries=limit
    attempts=0

    while  attempts < limit:
        guess = int(input("Guess a number:"))
        if guess == answer:
            print("You win")
            break
    
        elif guess < answer:
            print("Too low")
            tries = tries - 1
            attempts = attempts + 1
            print(f"You have {tries} attempts remaining to guess the number")
    
        else:
            print("Too high")
            tries = tries - 1
            attempts = attempts + 1
            print(f"You have {tries} attempts remaining to guess the number")        


    game_cont=input("Do you want to play again? yes or no ")
