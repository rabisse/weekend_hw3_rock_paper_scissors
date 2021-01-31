class Game():

    def __init__(self):
        self.win_dict = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"
        }

    def play(self, player_1, player_2):

        winner = None

        if self.win_dict[player_1.choice.lower()] == player_2.choice.lower():
            winner = player_1
        elif self.win_dict[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2

        return winner

