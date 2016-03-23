from Getch import *
from significance import *
import random

#   ROCK    PAPER   SCISSORS
#   1       2       3

class basicPlayer():

    def __init__(self, filename = None):
        self.rockCount      = 0
        self.scissorCount   = 0
        self.paperCount     = 0

        self.gamesPlayed    = 0
        self.botWins        = 0
        self.playerWins     = 0

    def loadPastData( self, filename = "saves/basicPlayer.rpsd"):
        pass

    def predict(self):
        #predict always picks the move it thinks you will play
        if self.gamesPlayed == 0:
            return random.randrange(3) + 1

        rockLikelyHood = self.rockCount / self.gamesPlayed
        paperLikelyHood = self.paperCount / self.gamesPlayed
        scissorLikelyHood = self.scissorCount / self.gamesPlayed

        if rockLikelyHood > paperLikelyHood:
            if scissorLikelyHood > rockLikelyHood:
                return 3
            else:
                return 1
        else:
            if scissorLikelyHood > paperLikelyHood:
                return 3
            else:
                return 2

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
        print("   bot has a %" + str(round(self.botWins/self.gamesPlayed * 100,3)) + " win rate")
        print("player has a %" + str(round(self.playerWins/self.gamesPlayed * 100,3)) + " win rate\n")
        print("likelyhood of score compared to random play:")
        print("player wins -> " + str(significance(1/3,self.gamesPlayed, self.playerWins)))
        print("   bot wins -> " + str(significance(1/3,self.gamesPlayed, self.botWins)))
        print("       ties -> " + str(significance(1/3,self.gamesPlayed, ties)))

    def saveData(self, filename = "saves/basicPlayer.rpsd" ):
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

def playToWin( prediction ):
    prediction += 1
    if prediction == 4:
        prediction = 1
    return prediction


if __name__ == "__main__":
    bot = basicPlayer()

    while True:
        botMove = bot.predict()
        playerMove = getch()

        #alter prediction to win
        botMove = playToWin(botMove)

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
