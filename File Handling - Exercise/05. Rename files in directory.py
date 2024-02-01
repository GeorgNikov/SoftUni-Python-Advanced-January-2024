import os
import re

directory = input("Enter a directory: ")
string_to_replace = input("Enter a string to replace: ")
string_to_replace_with = input("enter a string to replace with: ")

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        new_name = filename.replace(string_to_replace, string_to_replace_with)
        new_file = "/".join(re.split(r"[\\/]", file)[:-1]) + "/" + new_name
        os.rename(file, new_name)