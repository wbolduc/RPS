from randomPlayer import *
from nTransitionBot import *
from basicPlayer import *
from runBot import *

def playToWin( prediction ):
    prediction += 1
    if prediction == 4:
        prediction = 1
    return prediction

if __name__ == "__main__":
    bot1 = nTBot()
    bot2 = runBot()

    for i in range(1000):
        bot1Move = playToWin(bot1.predict())
        bot2Move = playToWin(bot2.predict())

        print("bot1 " + ("    Rock","   Paper","Scissors")[bot1Move-1] + " vs " + ("Rock     ","Paper    ","Scissors ")[bot2Move-1] + "bot2")

        if bot1Move == bot2Move:
            bot1Win = 0
            bot2Win = 0
            print("tie")
        elif bot1Move + 1 == bot2Move or (bot1Move == 3 and bot2Move == 1):
            bot1Win = -1
            bot2Win = 1
            print("bot2 Wins")
        else:
            bot1Win = 1
            bot2Win = -1
            print("bot1 Wins")

        bot1.report(bot2Move, bot2Win)
        bot2.report(bot1Move, bot1Win)
        bot1.showWinRates()
        print()

    bot1.showData()
