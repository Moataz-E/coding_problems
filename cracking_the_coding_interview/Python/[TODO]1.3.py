import time

def remove_duplicate_chars(string):
    """Removes duplicate characters without additional data structures

    Given a string, this function will go through the string replacing  
    """

    string_list = list(string)

    #If string is empty or contains only one character, return the unmodified
    #string
    if ((not string_list) or (len(string_list) < 2)): return string

    #The tail is used to mark the index before which there are no duplicate
    #characters
    tail = 1

    for i1, char1 in enumerate(string_list):

        j = tail

        for i2, char2 in enumerate(string_list[:j]):
            if (char1 == char2):
                j = i2
                break

        if (j == tail):
            string_list[tail] = char1
            tail += tail

    return ''.join(string_list[:tail])       

if __name__ == "__main__":

    print("This program is used to remove duplicate characters from a string")
    print("without using any additional data structures.")
    print("Please enter a string:")
    time.sleep(0.5)

    string_input = input("-->")

    print(remove_duplicate_chars(string_input))
