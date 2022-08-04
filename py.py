import random
print(
    """WELCOME TO GUESSING GAME
************************
    Instructions
  
    1.A secret number is hidden in this game.Players have to guess the secret number.
    2.The secret number is between 1 and 20.
    3.Players can guess the number 6 times.
    4.A total of 6 points wil be awarded to the players at the start of the game.
    5.Clues will be provided for you.
    6.For each clue,one point will be deducted
    All the best! LET'S PLAY
    """
)
#function to handle guessing
def guess_number():
    secret_number=random.randint(1,20)
    guess_count=0
    point=6
    while guess_count<6:
        guess=int(input("Enter a guess:" ))  #Asking the user to guess
        guess_count+=1
        if guess<secret_number:
            print("Your guess is too low")
            point-=1
        elif guess>secret_number:
            print("Your guess is too high")
            point-=1
        elif guess==secret_number:
            print("Congratulations! Your guess is right")

            print(f'You will get {point} points')
            restart()
            break
    else:
        print("You lost")
        restart()

def restart(): #function to restart the game
    input1 = input("Do you want to restart? Enter YES or NO:")
    # Asking the user to restart the game
    if input1 == "YES" or input1 == "yes":
        guess_number()
    else:
        print("Thank you")

input2 = input("Do you want to start? Enter YES:")
#Asking  the user to start the game
if input2 == "YES" or input2 == "yes":
    guess_number()









