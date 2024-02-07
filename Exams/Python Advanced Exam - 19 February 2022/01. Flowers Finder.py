from collections import deque

vowels = deque(input().split())
consonants = input().split()
found_word = False

flowers = {
    "rose": [letter for letter in "rose"],
    "tulip": [letter for letter in "tulip"],
    "lotus": [letter for letter in "lotus"],
    "daffodil": [letter for letter in "daffodil"],
}

while vowels and consonants and not found_word:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower, value in flowers.items():
        if vowel in value:
            c = value.count(vowel)
            for _ in range(c):
                flowers[flower].pop(value.index(vowel))

        if consonant in value:
            c = value.count(consonant)
            for _ in range(c):
                flowers[flower].pop(value.index(consonant))

        if len(value) == 0:
            print(f"Word found: {flower}")
            found_word = True

if not found_word:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left:", *vowels)
if consonants:
    print(f"Consonants left:", *consonants)
