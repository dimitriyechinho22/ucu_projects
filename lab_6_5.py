from typing import List


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    import random
    from string import ascii_uppercase
    final_list = []
    for i in range(3):
        small_list = []
        for j in range(3):
            j = random.choice(ascii_uppercase)
            small_list.append(j)
        final_list.append(small_list)
    return final_list
