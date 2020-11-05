import random


def get_random_cells(rows, columns, winner_cells_by_row, seed):
    """
    Function that returns a list of numbers representing cells in a matrix
    of {rows} by {columns}. The function will pick {winner_cells_by_row} random
    numbers in every row and will be added to the final array of winner
    cells
    """
    random.seed(seed)
    winning_cells = []
    for i in range(1, (rows * columns) + 1, columns):
        winning_cells += random.sample(
            range(i, i + columns), winner_cells_by_row
        )
    return winning_cells