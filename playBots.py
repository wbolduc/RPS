import sys

from Getch import *

def playToWin( prediction ):
    prediction += 1
    if prediction == 4:
        prediction = 1
    return prediction

class getMove():
    def __init__(self, playList = None):
        self.playList = playList
        self.currentMove = 0

    def move( self ):
        if self.playList == None:
            return getch()
        else:
            self.currentMove += 1
            return self.playList[self.currentMove - 1]


if __name__ == "__main__":
    try:
        botName = sys.argv[1].split(".")[0]
        module_obj = __import__(botName)
        globals()[botName] = module_obj
    except ImportError:
        print("No Bot called " + botName)
        sys.exit(1)

    try:
        f = open(sys.argv[2],'r')
        get = getMove(list(f.read()))
        f.close()
    except IndexError:
        get = getMove()

    bot = getattr(module_obj,botName)()





    while True:
        #Get bot predictions
        botMove = playToWin(bot.predict())
        #get player's move
        playerMove = get.move()

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
