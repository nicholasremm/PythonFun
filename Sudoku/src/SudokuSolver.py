import sys
import os
import csv

SOLVED_CSV = '_solved.csv'


def get_board_and_solve(input_path):
    """
    Load a sudoku file, solve the board in place and save the result.
    :param input_path: the path to the sudoku board
    """
    board = get_board(input_path)
    print('Initial board:')
    print_board(board)

    if solve_board(board):
        print('Solved board:')
        print_board(board)

        save_path = os.path.splitext(input_path)[0] + SOLVED_CSV
        save_board(board, save_path)
    else:
        print('No solution exists')


def get_board(input_path):
    """
    Load a sudoku board from a CSV file.
    :param input_path: the path to the CSV file
    :return: a 2D list representation of the board
    """
    print(f'Loading board from: {input_path}\n')
    board = []
    with open(input_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in csv_reader:
            int_row = [int(num_str) for num_str in row]
            board.append(int_row)

    return board


def save_board(board, output_path):
    """
    Output a 2D list representation of a sudoku board to a file.
    :param board: the sudoku board
    :param output_path: the path to save the file
    """
    print(f'Saving board to: {output_path}\n')
    with open(output_path, 'w', newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in board:
            csv_writer.writerow(row)


def print_board(board):
    """
    Print the sudoku board.
    :param board: the board to print
    """
    for row in board:
        print(' '.join(str(col) for col in row))
    print()


def solve_board(board):
    """
    Recursive function to solve a sudoku board.
    Modifies the existing board using the backtrack algorithm to reach a solution.
    :param board: the 2D list representation of a sudoku board
    :return: True if the board was solved, False otherwise
    """
    row, col = find_empty_cell(board)
    if row is None or col is None:
        # No empty cells
        return True

    for num in range(1, 10):
        if is_valid_number(board, num, row, col):
            board[row][col] = num

            # Check solution with recursive call
            if solve_board(board):
                return True

            # Bad number, reset it to empty
            board[row][col] = 0

    # Backtrack after trying all numbers
    return False


def find_empty_cell(board):
    """
    Find a cell missing a value on a sudoku board.
    :param board: the sudoku board
    :return: a tuple representing row and column coordinates
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return (None, None)


def is_valid_number(board, num, row, col):
    """
    Wrapper function to determine if a cell is valid.
    :return: the results of checking the board's row, column and surrounding box
    """
    return is_valid_col(board, num, col) \
           and is_valid_row(board, num, row) \
           and is_valid_box(board, num, row, col)


def is_valid_col(board, num, col):
    """
    Determine if a new value can be added in the given column.
    :param board: the sudoku board
    :param num: the new value to check
    :param col: the column to check
    :return: True if the column does not already contain the new value
    """
    for i in range(len(board)):
        if board[i][col] == num:
            return False

    return True


def is_valid_row(board, num, row):
    """
    Determine if a new value can be added in the given row.
    :param board: the sudoku board
    :param num: the new value to check
    :param row: the row to check
    :return: True if the row does not already contain the new value
    """
    for i in range(len(board[0])):
        if board[row][i] == num:
            return False

    return True


def is_valid_box(board, num, row, col):
    """
    Determine if a new value can be added in the given row/column box.
    :param board: the sudoku board
    :param num: the new value to check
    :param row: the row to check
    :param col: the column to check
    :return: True if the box does not already contain the new value
    """
    # Get the upper-left-most cell in the box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: SudokuSolver csv_path')
    else:
        input_path = sys.argv[1]
        get_board_and_solve(input_path)
