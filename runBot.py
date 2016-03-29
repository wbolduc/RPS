from Getch import *
from significance import *
import random

#   ROCK    PAPER   SCISSORS
#   1       2       3

class runBot():

    def __init__(self, scopeSize = 2):
        #basic metrics
        self.rockCount      = 0
        self.scissorCount   = 0
        self.paperCount     = 0

        self.gamesPlayed    = 0
        self.botWins        = 0
        self.playerWins     = 0

        #prediction metrics
        self.runList = {}
        self.runLength = 0
        self.currentRun = 0


    def loadPastData( self, filename = "saves/basicPlayer.rpsd"):
        pass

    def predict(self):
        #run: (play, count) = [total, rock, paper, scissors]
        run = self.runList.setdefault((self.currentRun, self.runLength),[0,0,0,0])


        if run[0] == 0:
            return random.randrange(3) + 1
        else:
            rockLikelyHood = run[1] / run[0]
            paperLikelyHood = run[2] / run[0]
            scissorLikelyHood = run[3] / run[0]

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
        #update basic data
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

        #update prediction data

        #update this transition
        run = self.runList.setdefault((self.currentRun, self.runLength),[0,0,0,0])
        run[0] += 1
        run[playerMove] += 1
        self.runList[(self.currentRun, self.runLength)] = run

        #update current run moves
        if playerMove == self.currentRun:
            self.runLength += 1
        else:
            self.runLength = 1
            self.currentRun = playerMove



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
        #print("likelyhood of score compared to random play:")
        #print("player wins -> " + str(significance(1/3,self.gamesPlayed, self.playerWins)))
        #print("   bot wins -> " + str(significance(1/3,self.gamesPlayed, self.botWins)))
        #print("       ties -> " + str(significance(1/3,self.gamesPlayed, ties)))

    def showWinRates(self):
        print("   bot has a %" + str(round(self.botWins/self.gamesPlayed * 100,3)).ljust(6," ") + " win rate")
        print("player has a %" + str(round(self.playerWins/self.gamesPlayed * 100,3)).ljust(6," ") + " win rate\n")

    def saveData(self, filename = "saves/nTPlayer.rpsd" ):
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
