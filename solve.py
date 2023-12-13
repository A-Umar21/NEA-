def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return True  # Puzzle is solved

    row, col = empty

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If the puzzle is solved, return True

            board[row][col] = 0  # If placing num doesn't lead to a solution, backtrack

    return False  # No valid number found for this cell


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid_move(board, row, col, num):
    # Check if the number is not in the same row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not in the same 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True


# Example usage:
# sudoku_board is a 9x9 list representing the Sudoku puzzle
# 0 denotes an empty cell
# You can modify the input Sudoku board according to your initial puzzle state
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(sudoku_board)
print(sudoku_board)  # Print the solved Sudoku board
