import random

gameList = ["Rock", "Paper", "Scissor"]
userScore = 0
computerScore = 0

while True:
    userChoice = input("Choose Rock, Paper or Scissors: ")
    compChoice = gameList[random.randint(0, 2)]

    if userChoice in ["r", "R", "rock", "ROCK", "Rock"]:
        userChoice = "Rock"
    elif userChoice in ["p", "P", "paper", "PAPER", "Paper"]:
        userChoice = "Paper"
    elif userChoice in ["s", "S", "scissor", "SCISSOR", "Scissor"]:
        userChoice = "Scissor"
    else:
        print("\nIncorrect input. Try Again.")
        print("================================================================\n")
        continue

    if userChoice == "Rock" and compChoice == "Scissor":
        result = " You win!"
        userScore += 1
    elif userChoice == "Paper" and compChoice == "Rock":
        result = " You win!"
        userScore += 1
    elif userChoice == "Scissor" and compChoice == "Paper":
        result = " You win!"
        userScore += 1
    elif userChoice == compChoice:
        result = " You're tied. Try Again."
    else:
        result = " You lose!"
        computerScore += 1

    print("\nYou choose " + userChoice + ". The computer choose " + compChoice + "." + result)

    print("\nPlayer wins: " + str(userScore) + "\nComputer wins: " + str(computerScore))

    userTryAgain = input("\nDo you want to try again? (Y|N) ")
    if userTryAgain in ["y", "Y", "YES", "yes", "Yes"]:
        print("\n================================================================\n")
        pass
    elif userTryAgain in ["n", "N", "NO", "no", "No"]:
        print("\nThanks for playing")
        print("================================================================\n")
        break
    else:
        print("\nThanks for playing")
        print("================================================================\n")
        break
