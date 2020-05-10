VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

w = input().strip()

consecutive_same = False
consecutive_vowels = False
for c1, c2 in zip(w[:-1], w[1:]):
    if c1 == c2:
        consecutive_same = True
    if c1 in VOWELS and c2 in VOWELS:
        consecutive_vowels = True

beautiful_word = not(consecutive_same or consecutive_vowels)
if beautiful_word:
    print("Yes")
else:
    print("No")
