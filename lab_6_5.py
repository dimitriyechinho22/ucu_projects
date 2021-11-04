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

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    from string import ascii_lowercase
    list_of_ascii = [small for small in ascii_lowercase]
    with open('en.txt', 'r', encoding='utf-8') as file:
        list_f_words = []
        for skip in range(2):
            file.readline()

        for line in file:
            line = line.strip()
            if len(line) >= 4 and letters[4] in line:
                list_f_words.append(line)
        for match in letters:
            if match in list_of_ascii:
                list_of_ascii.remove(match)
        work_list = list_f_words.copy()
        for key in work_list:
            low = key.lower()
            for item in low:
                if item in list_of_ascii:
                    list_f_words.remove(key)
                    break
        work2_list = list_f_words.copy()
        str_letters = ''
        for let in letters:
            str_letters += let
        for it in work2_list:
            less = it.lower()
            for out in less:
                if less.count(out) > str_letters.count(out):
                    list_f_words.remove(less)
                    break
        return list_f_words

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = input()
    user_words = user_words.strip()
    user_words = user_words.split()
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str], list_f_words: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pure_list = []
    for wor in user_words:
        letter_of_wor = [j for j in wor]
        if len(wor) >= 4 and letters[4] in wor:
            rule = True
        else:
            rule = False
        for let in letter_of_wor:
            if letter_of_wor.count(let) < letters.count(let):
                rule = True
            else:
                rule = False
            if rule and wor not in list_f_words:
                pure_list.append(wor)


def results():
    letters = []
    gen = generate_grid()
    for i in gen:
        print(i)
    for i in gen:
        for j in i:
            letters.append(j.lower())
    us_words = get_user_words()
    needed_words = get_words('en.txt', letters)
    print(needed_words)
    print(us_words)
    pure_words = get_pure_user_words(us_words, letters, needed_words)
    print(pure_words)
    with open('result.txt', 'w') as result:
        for i in gen:
            result.writelines(f'{i}\n')
        result.writelines(needed_words + '\n')
        result.writelines(us_words + '\n')
        result.writelines(pure_words + '\n')