from Getch import *
from significance import *
import random

#   ROCK    PAPER   SCISSORS
#   1       2       3

class nTBot():

    def __init__(self, scopeSize = 2):
        #basic metrics
        self.rockCount      = 0
        self.scissorCount   = 0
        self.paperCount     = 0

        self.gamesPlayed    = 0
        self.botWins        = 0
        self.playerWins     = 0

        #prediction metrics
        self.pastMoves = [0] * scopeSize
        self.moveChunks = {}

        #make all the move chunks
        chunk = [1] * scopeSize
        place = 0
        while place != scopeSize:
            self.moveChunks[tuple(chunk)] = [0,0,0,0]                   #totalOccurences, rockCount, paperCount, scissorCount
            place = 0
            while place < scopeSize and chunk[place] > 2:
                chunk[place] = 1
                place += 1
            if place < scopeSize:
                chunk[place] += 1

    def loadPastData( self, filename = "saves/basicPlayer.rpsd"):
        pass

    def predict(self):
        #picks the next likely move based on the previous 3 moves

        #get move chunk
        chunk = self.moveChunks.setdefault(tuple(self.pastMoves),[0,0,0,0])

        #totalOccurences, rockCount, paperCount, scissorCount

        if chunk[0] == 0:
            return random.randrange(3) + 1
        else:
            rockLikelyHood = chunk[1] / chunk[0]
            paperLikelyHood = chunk[2] / chunk[0]
            scissorLikelyHood = chunk[3] / chunk[0]

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
        chunk = self.moveChunks.setdefault(tuple(self.pastMoves),[0,0,0,0])
        chunk[0] += 1
        chunk[playerMove] += 1
        self.moveChunks[tuple(self.pastMoves)] = chunk

        #update past 3 moves
        self.pastMoves = self.pastMoves[1:] + [playerMove]


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
