"""Conways game of life
Rule 1: Any live cell with two or three live neighbours survives
Rule 2: Any dead cell with three live neighbours becomes a live cell
Rule 3: All other live cells die in the next generation. Similarly, all other dead cells stay dead.
"""
import time
import numpy as np
import os 

class GameBoard:
    "represents GOL board, currently treating outer edge as always dead"
    def __init__(self, board_dimensions, starting_squares):
        """board dimensions: x -> x by x
        starting squares: ([y1,x1], [y2,x2], [y3,x3]) etc"""
        self.board = np.zeros((board_dimensions, board_dimensions), dtype=np.int8)
        self.board_dimensions = board_dimensions
        for coord in starting_squares:
            self.board[coord] = 1
        

    def print_board(self):
        print(self.board)

    def update(self):
        new_board = np.zeros((self.board_dimensions, self.board_dimensions), dtype=np.int8)
        surrounding_squares = ((0,1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1))
        rows = np.arange(1, self.board_dimensions-1)
        columns = np.arange(1, self.board_dimensions-1)
        for row in rows:
            for column in columns:
                count = 0
                for coord in surrounding_squares:
                    if self.board[row+coord[0], column+coord[1]] == 1:
                        count += 1
                if count == 3:
                    new_board[row, column] = 1
                elif (count == 2) and (self.board[row, column] == 1):
                    new_board[row, column] = 1
        self.board = new_board

    def continually_update(self, sleep_time=1, num_iterations=1000):
        count = 0
        while True:
            self.update()
            self.print_board()
            time.sleep(sleep_time)
            clear_console()
            count += 1
            if count == num_iterations:
                break

def clear_console():
    # taken from internet
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


if __name__ == '__main__':
    starting_squares = ((5,5), (4,5), (5,4), (5,6))
    board_dimensions = 11
    gol_board = GameBoard(board_dimensions, starting_squares)
    gol_board.continually_update(num_iterations=15)
