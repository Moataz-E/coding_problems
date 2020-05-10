import time
from collections import Counter

def detect_anagrams(string1, string2):
    """Checks if two string are anagrams.
    
    One possible way is to check the two sorted string for equality. In this
    function however, we will count each individual character in both strings
    and check for equality.
    """

    #Check if string arn't equal in size
    if not (len(string1) == len(string2)): return False
    
    #Create dictionary of characters and their counts for each string
    string1_char_dict = Counter(string1)
    string2_char_dict = Counter(string2)

    return string1_char_dict == string2_char_dict 


if __name__ == "__main__":
  
    print("This program is used to find if two string are anagrams.")
    print("Please enter the two string seperate by a space:")
    time.sleep(0.5)

    strings_input = input("-->")
    string1, string2 = strings_input.split()

    print(detect_anagrams(string1, string2))
