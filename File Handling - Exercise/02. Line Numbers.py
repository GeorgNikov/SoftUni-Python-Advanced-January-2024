import os
from string import punctuation

path = os.path.join("resources", "text1.txt")
output_path = os.path.join("resources", "output.txt")

with open(path, "r") as text_file:
    text = text_file.readlines()

output_file = open(output_path, "w")

for row in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1

        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {row + 1}: {text[row][:-1]} ({letters})({marks})\n")

output_file.close()
