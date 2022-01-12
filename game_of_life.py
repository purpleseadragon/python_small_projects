"""Conways game of life
Rule 1: Any live cell with two or three live neighbours survives
Rule 2: Any dead cell with three live neighbours becomes a live cell
Rule 3: All other live cells die in the next generation. Similarly, all other dead cells stay dead.
"""
import time
import numpy as np

class GameBoard:
    "represents GOL board, currently treating outer edge as always dead"
    def __init__(self, board_dimensions, starting_squares):
        """board dimensions: [x,y]
        starting squares: ([x1,y1], [x2,y2], [x3,y3]) etc"""
        self.board = np.zeros(board_dimensions)
        for coord in starting_squares:
            self.board[coord] = 1
        
    def print_board(self):
        print(self.board)

    def update(self):
        pass

if __name__ == '__main__':
    starting_squares = ((3,4), (3,5), (4,4), (5,4))
    board_dimensions = (20, 20)
    gol_board = GameBoard(board_dimensions, starting_squares)
    gol_board.print_board()
 