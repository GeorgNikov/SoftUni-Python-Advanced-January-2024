def words_sorting(*words):
    result = {}

    for word in words:
        if word not in result:
            sum_of_chars = sum(ord(char) for char in word)
            result[word] = sum_of_chars

    if sum(result.values()) % 2 == 0:
        sorted_words = sorted(result.items())
    else:
        sorted_words = sorted(result.items(), key=lambda x: x[1], reverse=True)

    final_result = []
    for key, value in sorted_words:
        final_result.append(f"{key} - {value}")

    return "\n".join(final_result)




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print()

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print()

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))