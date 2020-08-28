import random


def get_winner_positions(start_position, end_position, winners_count, seed):
    """
    Script to get diffrent random numbers that will be the positions of
    the winners in the board
    """
    random.seed(seed)
    return random.sample(
        range(start_position, end_position + 1),
        winners_count
    )


def get_random_position(start_position, end_position):
    """Get a random number between a range of ints"""
    return random.randint(start_position, end_position)