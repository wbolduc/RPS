from Getch import *

from randomPlayer import *
from nTransitionBot import *

def playToWin( prediction ):
    prediction += 1
    if prediction == 4:
        prediction = 1
    return prediction


if __name__ == "__main__":
    bot = nTBot(2)

    while True:
        #Get bot predictions
        botMove = playToWin(bot.predict())
        #get player's move
        playerMove = getch()

        #check for valid player move
        if playerMove in "0123":
            playerMove = int(playerMove)
        else:
            print("Not a move")
            continue

        #check if player wants to quit
        if playerMove == 0:
            break

        print("player " + ("    Rock","   Paper","Scissors")[playerMove-1] + " vs " + ("Rock     ","Paper    ","Scissors ")[botMove-1] + "bot")

        if playerMove == botMove:
            botWin = 0
            print("tie")
        elif playerMove + 1 == botMove or (playerMove == 3 and botMove == 1):
            botWin = 1
            print("bot Wins")
        else:
            botWin = -1
            print("you Win")

        bot.report(playerMove, botWin)
        bot.showWinRates()
        print()

    print("thanks for playing")
    bot.showData()
    bot.saveData()
