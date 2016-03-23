from Getch import *
from significance import *
import random

#   ROCK    PAPER   SCISSORS
#   1       2       3

class randomPlayer():

    def __init__(self, filename = None):
        self.rockCount      = 0
        self.scissorCount   = 0
        self.paperCount     = 0

        self.gamesPlayed    = 0
        self.botWins        = 0
        self.playerWins     = 0

    def predict(self):
        return random.randrange(3) + 1

    def report(self, playerMove, botWin):
        if playerMove == 1:
            self.rockCount += 1
        elif playerMove == 2:
            self.paperCount += 1
        else:
            self.scissorCount += 1

        self.gamesPlayed += 1
        if botWin == 1:
            self.botWins += 1
        elif botWin == -1:
            self.playerWins += 1

    def showData(self):
        ties = self.gamesPlayed - self.botWins - self.playerWins

        print("Session Totals:")
        print("      Rocks = " + str(self.rockCount))
        print("     Papers = " + str(self.paperCount))
        print("   Scissors = " + str(self.scissorCount) + "\n")
        print("   Bot Wins = " + str(self.botWins))
        print("Player Wins = " + str(self.playerWins))
        print("       Ties = " + str(ties))
        print("Total Games = " + str(self.gamesPlayed) + "\n")
        self.showWinRates()
        print("likelyhood of score compared to random play:")
        print("player wins -> " + str(significance(1/3,self.gamesPlayed, self.playerWins)))
        print("   bot wins -> " + str(significance(1/3,self.gamesPlayed, self.botWins)))
        print("       ties -> " + str(significance(1/3,self.gamesPlayed, ties)))

    def showWinRates(self):
        print("   bot has a %" + str(round(self.botWins/self.gamesPlayed * 100,3)).ljust(6," ") + " win rate")
        print("player has a %" + str(round(self.playerWins/self.gamesPlayed * 100,3)).ljust(6," ") + " win rate\n")

    def saveData(self, filename = "saves/randomPlayer.rpsd"):
        newRockCount    = self.rockCount
        newPaperCount   = self.paperCount
        newScissorCount = self.scissorCount
        newBotWins      = self.botWins
        newPlayerWins   = self.playerWins
        newGamesPlayed  = self.gamesPlayed

        try:
            f = open(filename, "r")
            newRockCount    += int(f.readline())
            newPaperCount   += int(f.readline())
            newScissorCount += int(f.readline())
            f.readline()
            newBotWins      += int(f.readline())
            newPlayerWins   += int(f.readline())
            newGamesPlayed  += int(f.readline())
            f.close()
        except IOError:
            pass

        f = open(filename,'w')

        f.write(str(newRockCount) + "\n")
        f.write(str(newPaperCount) + "\n")
        f.write(str(newScissorCount) + "\n")
        f.write("\n")
        f.write(str(newBotWins) + "\n")
        f.write(str(newPlayerWins) + "\n")
        f.write(str(newGamesPlayed) + "\n")

        f.close()

if __name__ == "__main__":
    bot = randomPlayer()

    while True:
        botMove = bot.predict()
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

        print()
    print("thanks for playing")
    bot.showData()
    bot.saveData()
