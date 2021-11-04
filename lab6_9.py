"""
Plays target game
"""
def generate_grid():
    """
    Returns generated grid
    >>> generate_grid()
    ['в', 'і', 'з', 'ч', 'ь']
    """
    import random
    small_ukr_letters = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
    gen_letters = []
    for r_letter in range(5):
        ukr_let = random.choice(small_ukr_letters)
        if ukr_let not in gen_letters:
            gen_letters.append(ukr_let)
        else:
            continue
    return gen_letters


