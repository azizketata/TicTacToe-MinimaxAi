import math
import random
class player :
    def __init__(self, letter):
        self.letter = letter

    def get_move (self):
        pass

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        val = None
        valid_square = False
        while not valid_square:
            square = input(self.letter+"\'s turn input number between (0-8)")
            try:
                val = int(square) # protection against input anything other than an int
                if val not in game.available_moves(): # protection in case the input is in an already taken case
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Error enter a Valid number")
        return val

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
class GeniusComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves())==9:
            square =random.choice(game.available_moves())#random choice
        else:
            #get the square based of the minimax algorithm
            square= self.minimax(game,self.letter)['position']
            return square

    def minimax (self, state, player):
        max_player= self.letter
        other_player = 'O' if player == 'X' else 'X'

        #first we want to check if the previous move is a winner
        #this our base case
        if state.current_winner == other_player:
            #we should return position AND score because we need to keep track
            return {'position':None,
                    'score': 1*(state.num_empty_squares()+1) if other_player== max_player else -1 *(state.num_empty_squares()+1)}
        elif not state.empty_squares():
            return {'position': None ,'score':0}

        if player == max_player :
            best ={'position': None,'score': -math.inf}#each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}#each score should minimize

        for possible_move in state.available_moves():
            #step1 : make a move , try that spot
            state.make_move (possible_move, player)

            #step2 : recurse using minmax to simulate a game after making that move
            sim_score= self.minimax(state,other_player)
            #step3 : undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move#otherwise this will get messed up form the recursion

            #step4 : update the dictionaries if necessary
            if player == max_player:
                if sim_score['score']> best['score']:
                    best= sim_score
            else:
                if sim_score['score']<best['score']:
                    best = sim_score

        return best
