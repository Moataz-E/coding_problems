import time
from collections import defaultdict

def uniq_check(string):
    """Checks if a string contains unique characters

    Given a string, this function will populate a list such that each index
    in the list corresponds to a a character's value. If a character's index
    was already set to True, that means the character was already seen, and
    hence the string isn't unique.
    """

    char_parity = defaultdict(bool)

    for char in string:
        if (char_parity[char]): return False
        char_parity[char] = True        

    return True


if __name__ == "__main__":

    print("This program is used to find if a given string contains unique")
    print("characters. Please input the string you would like to check:")
    time.sleep(0.5)

    string_input = input("-->")

    print(uniq_check(string_input))
