import math
import time
from player import HumanPlayer, RandomComputerPlayer , GeniusComputerPlayer

class TicTacToe :
    def __init__(self):
        self.board = [' ' for _ in range(9)] # empty at the beginning
        self.current_winner = None #keeps track of the winner

        # returns a list of all the possible moves
    def available_moves (self):
        available = ([i for i,spot in enumerate(self.board) if spot == ' '])
        return available

    # prints the board in it's current state
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+ ' | '.join(row) + ' |')

     # prints first to show all the possibilities to the player
    def print_board_nums(self):
        for row in [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]:
            print('| '+ ' | '.join(row) + ' |')

    #checks if there are empty squares left on the
    def empty_squares(self):
        return ' ' in self.board

    def winner (self, square , letter):
        # checking if there is a win when it comes to the row
        row_ind = math.floor(square /3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([i == letter for i in row]):
            return True
        #checking if there is a column win
        col_ind = square%3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([letter == i for i in column]):
            return True
        if square%2 == 0:
            # checking if there is a diagonal win : 2 possibilities left to right diagonal or right to left diagonal
            ldiagonal = [self.board[i] for i in [0,4,8]]
            if all([letter == i for i in ldiagonal]):
                return True
            rdiagonal = [self.board[i] for i in [2,4,6]]
            if all ([letter == i for i  in rdiagonal]):
                return True
        return False

    def make_move(self,square , letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square , letter):
                self.current_winner = True
            return True
        return False
    def num_empty_squares(self):
        return len(self.available_moves())


def play (game, x_player , o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move (square,letter):
            if print_game:
                print(letter + f' player makes move in square {square}')
                game.print_board()
                print(' ')

            if game.current_winner:
                print(letter + ' wins')
                return letter
            letter ='O' if letter =='X'else 'X'
        if print_game:
            time.sleep(0.8)
    if print_game:
        print("it's a tie")

if __name__ == '__main__':
    t = TicTacToe()
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    play(t,x_player,o_player,print_game=True)
