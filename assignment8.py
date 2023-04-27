import random
import argparse

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.die = Die()

    def take_turn(self):
        turn_score = 0

        decision = input(f"{self.name}, Press r to roll ")
        if (decision == "r"):
            while(decision == "r"):
                roll = self.die.roll()
                if (roll == 1):
                        print(f"{self.name}, you rolled a 1! You get no points this turn and your turn ends.")
                        return
                turn_score += roll
                print(f"{self.name}, you rolled a {roll}! Your current turn score is {turn_score} and your total score is {self.score}.")
                decision = input("Do you want to roll again (r) or hold (h)? ")
                if(decision != "h" and decision != "r"):
                    print("Invalid input, try either 'r' or 'h'")
        
        if(decision == "h"):
            self.score += turn_score
            print(f"{self.name}, your turn has ended. Your total score is now {self.score}.")
            return  
        if(decision != "h" and decision != "r"):
            print("Invalid input, try either 'r' or 'h'")
    
class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.die = Die()

    def take_turn(self):
        turn_score = 0
        while turn_score < min(25, 100 - self.score):
            roll = self.die.roll()
            if roll == 1:
                print(f"{self.name} rolled a 1 and lost all points for this turn.")
                return
            turn_score += roll
            print(f"{self.name} rolled a {roll}. Current turn score: {turn_score}")
        self.score += turn_score
        print(f"{self.name} has decided to hold. Total score: {self.score}")
    
class PlayerFactory:
    def create_player(self, name, player_type):
        if player_type == "human":
            return HumanPlayer(name)
        elif player_type == "computer":
            return ComputerPlayer(name)
        else:
            raise ValueError("Invalid player type")

class Die:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class PigGame:
    def __init__(self, players):
        self.players = players
        self.current_player = players[0]
        self.other_player = players[1]
        self.die = Die()

    def switch_players(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def take_turn(self):
        print(f"It's {self.current_player}'s turn!")
        self.current_player.take_turn()
        print(f"{self.current_player}'s turn is over, score: {self.current_player.score}\n")

    def play(self):
        print(f"Welcome to Pig, {self.players[0]} and {self.players[1]}!\n")

        while True:
            self.take_turn()
            if self.current_player.score >= 100:
                print(f"Congratulations, {self.current_player}! You won!")
                break
            self.switch_players()




def parse_args():
    parser = argparse.ArgumentParser(description='Play Pig game')
    parser.add_argument('--player1', type=str, help='Specify player 1 (human or computer)')
    parser.add_argument('--player2', type=str, help='Specify player 2 (human or computer)')
    args = parser.parse_args()
    factory = PlayerFactory()
    player1 = factory.create_player("Alice", args.player1)
    player2 = factory.create_player("Bob", args.player2)
    return player1, player2

if __name__ == '__main__':
    player1, player2 = parse_args()
    game = PigGame([player1, player2])
    game.play()