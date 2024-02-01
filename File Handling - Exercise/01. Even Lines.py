import os

path = os.path.join("resources", "text1.txt")

symbols = ("-", ",", ".", "!", "?")

with open(path) as even_lines_file:
    text = even_lines_file.readlines()

for txt in range(0, len(text), 2):
    for symbol in symbols:
        text[txt] = text[txt].replace(symbol, '@')

    print(*text[txt].split()[::-1])