from collections import deque
import os

turn = deque(["O", "X"])


class game_TicTac:

    def __init__(self):
        self.values = []
        for i in range(9):
            self.values.append(" ")

    def print_board(self):
        print("\t  A     B     C")
        print("\t     |     |")
        print("1\t  {}  |  {}  |  {}".format(self.values[0], self.values[1], self.values[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("2\t  {}  |  {}  |  {}".format(self.values[3], self.values[4], self.values[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("3\t  {}  |  {}  |  {}".format(self.values[6], self.values[7], self.values[8]))
        print("\t     |     |")
        print("\n")

    def add_move(self, position=0, turn=" "):
        self.values[position] = turn

    def check_tictac(self):
        if (self.values[0] == self.values[1] == self.values[2]) and self.values[0] != " ":
            return True

        if (self.values[0] == self.values[3] == self.values[6]) and self.values[0] != " ":
            return True

        if (self.values[0] == self.values[4] == self.values[8]) and self.values[0] != " ":
            return True

        if (self.values[2] == self.values[4] == self.values[6]) and self.values[2] != " ":
            return True

        if (self.values[1] == self.values[4] == self.values[7]) and self.values[1] != " ":
            return True

        if (self.values[3] == self.values[4] == self.values[5]) and self.values[3] != " ":
            return True

        if (self.values[2] == self.values[5] == self.values[8]) and self.values[2] != " ":
            return True

        if (self.values[6] == self.values[7] == self.values[8]) and self.values[6] != " ":
            return True

        return False

    def check_position(self, position=0):
        if self.values[position] == " ":
            return True
        else:
            return False


def change_turn():
    turn.rotate()
    return turn[0]


if __name__ == '__main__':

    print("Welcome to the Tic-Tac-Toe Game.")
    print("")
    print("RULES")
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    print("2. You are X, your friend is O. Players take turns putting their marks in empty squares.")
    print("3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print(
        "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    print("")

    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    i = 0
    game = game_TicTac()
    player = change_turn()
    while game.check_tictac and i < 9:
        game.print_board()
        print("Player {}: Enter the coordinate to play".format(player))
        pos = input("> ")
        position = 0

        if pos[1] == "2":
            position += 3
        if pos[1] == "3":
            position += 6
        if pos[0] == "B":
            position += 1
        if pos[0] == "C":
            position += 2

        if game.check_position(position):
            game.add_move(position, player)
            player = change_turn()
            clearConsole()
        else:
            print("Please enter a correct coordinate")

        if game.check_tictac():
            game.print_board()
            print("Congratulations! Player {} won!".format(player))
            break

        i += 1

    """
    def get_pos(coord):
      a_dic = {'A1': 0, 'B1': 1, 'C1': 2, 'A2': 3, 'B2': 4, 'C2': 5, 'A3': 6, 'B3': 7, 'C3': 8}
  
      if len(coord) != 2:
        print("Enter a valid coordinate")
        return NULL
      elif coord in a_dic:
        return a_dic[coord]
  
  
    """

"""if __name__ == '__main__':
    print("Welcome to the Tic-Tac-Toe Game.")
    print("RULES")
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    print("2. You are X, your friend is O. Players take turns putting their marks in empty squares.")
    print("3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print("4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    """

"""def single_game(cur_player):

    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}"""


