class bot:
    """
    This class represents the superclass for a prediction bot.
    """

    def __init__(self, filename = None):
        self.rockCount      = 0
        self.scissorCount   = 0
        self.paperCount     = 0

        self.totalGames     = 0
        self.botWins        = 0
        self.playerWins     = 0

    def predict(self):
        raise NotImplementedError("predict")

    def report(self, playerMove, botWin):
        raise NotImplementedError("report")

    def showData(self):
        ties = self.totalGames - self.botWins - self.playerWins

        print("Session Totals:")
        print("      Rocks = " + str(self.rockCount))
        print("     Papers = " + str(self.paperCount))
        print("   Scissors = " + str(self.scissorCount) + "\n")
        print("   Bot Wins = " + str(self.botWins))
        print("Player Wins = " + str(self.playerWins))
        print("       Ties = " + str(ties))
        print("Total Games = " + str(self.totalGames) + "\n")
        print("   bot has a %" + str(round(self.botWins/self.totalGames * 100,3)) + " win rate")
        print("player has a %" + str(round(self.playerWins/self.totalGames * 100,3)) + " win rate\n")
        print("likelyhood of score compared to random play:")
        print("player wins -> " + str(significance(1/3,self.totalGames, self.playerWins)))
        print("   bot wins -> " + str(significance(1/3,self.totalGames, self.botWins)))
        print("       ties -> " + str(significance(1/3,self.totalGames, ties)))

    def saveData(self, filename = "saves/randomPlayer.rpsd"):
        raise NotImplementedError("saveData")
