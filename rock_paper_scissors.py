import random

# function to evaluate winner
# input: 2 strings
# returns: a or b or "tie"
def whoWins(a,b):
    return a


i = 100
choices = ["rock","paper","scissors"]

# loop to keep playing game
while (i > 0):
    
    # ask for user input (rock, paper, scissors, or quit)
    userChoice = input("please choose rock, paper, or scissors (or quit): ")

    # randomize computer input
    compChoice = choices[random.randint(0,2)]

    # display choices
    print("You chose " + userChoice + " and the computer chose " + compChoice + "...")

    if userChoice == "quit":
        break
    else:
        theWinner = whoWins(userChoice,compChoice)
        if theWinner == "tie":
            print("It's a draw!")
        else:
            print(theWinner + " wins!!!")
    
    i -= 1
