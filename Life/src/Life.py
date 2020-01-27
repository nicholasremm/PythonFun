import random
import numpy as np
from matplotlib import pyplot as plot
import matplotlib.animation as animate
import seaborn


class Life:
    """
    Class representing Conway's game of life using matplotlib to display the game.
    """

    BOARD_SIZE = 200
    INITIAL_CELLS = 5000
    ANIMATION_FRAMES = 200
    REFRESH_FAST = 200
    REFRESH_NORMAL = 500
    REFRESH_SLOW = 1000
    WINDOW_TITLE = 'Game of Life'

    def __init__(self, size=BOARD_SIZE, initial_cells=INITIAL_CELLS, frames=ANIMATION_FRAMES, interval=REFRESH_NORMAL):
        self.board_size = size
        self.initial_cells = initial_cells
        self.frames = frames
        self.interval = interval
        self.figure = plot.gcf()
        self.image = None
        self.animation = None
        self.board = None
        self.setup_board()
        seaborn.set_style('dark')
        self.figure.canvas.set_window_title(self.WINDOW_TITLE)

    def setup_board(self):
        """
        Creates a 2D numpy array for the game board.
        """
        # Create the board
        self.board = np.zeros((self.board_size, self.board_size))

        # Initialize the starter cells at random
        for i in range(self.initial_cells):
            while True:
                coord = ([random.randint(0, self.board_size - 1),
                          random.randint(0, self.board_size - 1)])
                if self.board[coord[0], coord[1]] == 0:
                    self.board[coord[0], coord[1]] = 1
                    break

    def update_board(self):
        """
        Updates the board given the 4 rules:
        1. An empty space with 3 neighbors becomes alive.
        2. An occupied space with 1 or fewer neighbors dies.
        3. An occupied space with 4 or more neighbors dies.
        4. An occupied space with 2 or 3 neighbors survives.
        """
        # Make a copy of the existing board so it doesn't get clobbered
        old_board = self.board.copy()
        width = self.board.shape[0]
        height = self.board.shape[1]

        # Go through the entire array
        for i in range(width):
            for j in range(height):
                neighbors = self.get_num_neighbors(old_board, i, j)

                # Empty space
                if self.board[i, j] == 0:
                    if neighbors == 3:
                        # Create life
                        self.board[i, j] = 1
                # Life space
                else:
                    if neighbors <= 1 or neighbors >= 4:
                        # Dies
                        self.board[i, j] = 0

    def get_num_neighbors(self, board, row, col):
        """
        Get the number of occupied spaces around the given cell.
        Considers all 8 directions and wraps the array at the edges.
        :param board: the board to process
        :param row: the row in the board
        :param col: the column in the board
        :return: the number of neighbors surrounding the given position
        """
        # TODO this needs to be broken out
        count = 0
        width = board.shape[0]
        height = board.shape[1]

        # Up, left
        new_row = row - 1
        if new_row < 0:
            new_row = height - 1

        new_col = col - 1
        if new_col < 0:
            new_col = width - 1

        if board[new_row, new_col] == 1:
            count += 1

        # Up
        new_row = row - 1
        if new_row < 0:
            new_row = height - 1
        new_col = col

        if board[new_row, new_col] == 1:
            count += 1

        # Up, right
        new_row = row - 1
        if new_row < 0:
            new_row = height - 1

        new_col = col + 1
        if new_col >= width:
            new_col = 0

        if board[new_row, new_col] == 1:
            count += 1

        # Right
        new_row = row
        new_col = col + 1
        if new_col >= width:
            new_col = 0

        if board[new_row, new_col] == 1:
            count += 1

        # Down, right
        new_row = row + 1
        if new_row >= height:
            new_row = 0

        new_col = col + 1
        if new_col >= width:
            new_col = 0

        if board[new_row, new_col] == 1:
            count += 1

        # Down
        new_row = row + 1
        if new_row >= height:
            new_row = 0
        new_col = col

        if board[new_row, new_col] == 1:
            count += 1

        # Down, left
        new_row = row + 1
        if new_row >= height:
            new_row = 0

        new_col = col - 1
        if new_col < 0:
            new_col = width - 1

        if board[new_row, new_col] == 1:
            count += 1

        # Left
        new_row = row
        new_col = col - 1
        if new_col < 0:
            new_col = width - 1

        if board[new_row, new_col] == 1:
            count += 1

        return count

    def animate(self, frame):
        """
        Update the board to provide an updated image.
        :param frame: frame counter from FuncAnimation
        :return: the updated image
        """
        self.update_board()
        self.image.set_data(self.board)
        return self.image

    def play(self):
        """
        Starts the animation by creating and updating an image based off the board.
        """
        self.image = plot.imshow(self.board, interpolation='nearest')
        self.animation = animate.FuncAnimation(self.figure,
                                               self.animate,
                                               frames=self.frames,
                                               interval=self.interval)
        plot.show()
