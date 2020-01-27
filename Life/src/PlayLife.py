from Life import Life


GAME_TITLE = '=== Game of Life ==='


def play_game_loop():
    """
    Gets user input and runs the game.
    """
    while True:
        print(f'\n{GAME_TITLE}\n')
        board_size = get_board_size_input()
        life_cells = get_life_cells_input(board_size)
        refresh = get_refresh_input()
        run_game(board_size, life_cells, refresh)
        

def get_board_size_input():
    """
    Get board size from user input.
    :return: the board size from the user
    """
    board_size = 0
    while board_size <= 1:
        value = input('Board size (max=300): ')
        try:
            board_size = int(value)
            if board_size > 300:
                board_size = 0
        except ValueError:
            pass

        if board_size <= 1:
            print('Invalid board size. Try again.\n')
    print()

    return board_size


def get_life_cells_input(board_size):
    """
    Get starting life cells from user input.
    Number is constrained by the board size.
    :return: the number of starter life cells
    """    
    life_cells = 0
    while life_cells <= 1:
        value = input('Initial life percentage (whole number): ')
        try:
            percentage = int(value)
            if percentage in range(1, 100):
                life_cells = int((board_size * board_size) * percentage / 100.0)
        except ValueError:
            pass

        if life_cells <= 1:
            print('Invalid starting size. Try again.\n')
    print()

    return life_cells


def get_refresh_input():
    """
    Get refresh rate from user input.
    :return: the refresh rate chosen by the user
    """    
    refresh = -1
    while refresh not in range(0, 2):
        value = input('1) Fast refresh, 2) Normal refresh or 3) Slow refresh: ')
        try:
            refresh = int(value)
            if refresh == 0:
                refresh = Life.REFRESH_FAST
                break
            elif refresh == 1:
                refresh = Life.REFRESH_NORMAL
                break
            elif refresh == 2:
                refresh = Life.REFRESH_SLOW
                break
        except ValueError:
            pass

        print('Invalid refresh value. Try again.\n')
    print()

    return refresh


def run_game(board_size, life_cells, refresh):
    """
    Play the game with the given parameters.
    :param board_size: the grid size of the board
    :param life_cells: the number of starter life cells
    :param refresh: the refresh rate of the game
    """    
    print(f'Total cells: {board_size * board_size}, Life cells: {life_cells}\n')
    life_game = Life(size=board_size, initial_cells=life_cells, interval=refresh)
    life_game.play()


if __name__ == '__main__':
    play_game_loop()
