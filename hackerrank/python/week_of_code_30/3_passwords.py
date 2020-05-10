import sys
sys.setrecursionlimit(50000)
n = int(input().strip())

alphabet = [
    'a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
    's', 't', 'v', 'w', 'x', 'z'
]
vowels = alphabet[:5]
consonants = alphabet[5:]


def generate_permutations(password, password_length):
    # Base case: If length of password is equal to predefined password length, then we just return
    # the password.
    if len(password) == password_length:
        print(''.join(password))
        return

    last_letter = password[-1]
    if last_letter in vowels:
        for cons in consonants:
            new_password = password[:]
            new_password.append(cons)
            generate_permutations(new_password, password_length)
    else:
        for vowel in vowels:
            new_password = password[:]
            new_password.append(vowel)
            generate_permutations(new_password, password_length)

for letter in alphabet:
    generate_permutations([letter], n)
