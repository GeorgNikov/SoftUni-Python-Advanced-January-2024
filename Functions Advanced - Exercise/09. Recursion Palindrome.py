def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] != word[-index-1]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


    # for arg in args:
    #     if arg == arg[::-1]:
    #         return f"{args[0]} is a palindrome"
    #     return f"{args[0]} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
