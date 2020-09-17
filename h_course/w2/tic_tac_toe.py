import numpy as np
import random

###Exercise 1
def create_board():
    return np.zeros((3,3), dtype=int)

### Exercise 2
def place(board, player, position):
    if (board[position] == 0):
        board[position] = player
board = create_board()
place(board, 1, (0, 0))

### Exercise 3
def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))

### Exercise 4
random.seed(1)
def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
        return board
board = random_place(board, 2)

### exercise 5: new board - each player puts in 3 markers each ###
random.seed(1)
board = create_board()
for i in range(3):
    random_place(board, 1), random_place(board, 2)


### exercise 6
def check_row(row, player):
    for marker in row:
        if marker != player:
            return False
    return True

def row_win(board, player):
    for row in board:
        if check_row(row, player):
            return True
    return False

### Exercise 7
def col_win(board, player):
    for row in board.T:
        if check_row(row, player):
            return True
    return False

### Exercise 8


def check_diag(diagonals, player):
    for marker in diagonals:
        if marker != player:
            return False
    return True

def diag_win(board, player):
    diagonal = np.diagonal(board)
    diagonal2 = np.flipud(board).diagonal()
    diagonal3 = np.array([diagonal, diagonal2])
    board = diagonal3
    for diagonals in board:
        if check_diag(diagonals, player):
            return True
    return False

### Exercise 9
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player):
            winner = player
        if col_win(board, player):
            winner = player
        if diag_win(board, player):
            winner = player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

### Exercise 10

random.seed(1)
def play_game():
    board = create_board()
    for i in range(9):
        random_place(board, 1), evaluate(board), random_place(board, 2), evaluate(board)
        result = evaluate(board)
    if result != 0:
        return result

results = [play_game() for i in range(1000)]
count = results.count(1), results.count(2), results.count(-1)
#print(count) #incorrect answer

random.seed(1)
def play_game2():
    board = create_board()
    while True:
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result

results = [play_game2() for i in range(1000)]
count2 = results.count(1), results.count(2), results.count(-1)
#print(count2) #correct answer

### exercise 11

random.seed(1)
def play_strategic_game():
    board = create_board()
    place(board, 1, (1,1))
    while True:
        for player in [2, 1]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result

strat_results = [play_strategic_game() for i in range(1000)]
strat_count = strat_results.count(1), strat_results.count(2), strat_results.count(-1)
print(strat_count)






