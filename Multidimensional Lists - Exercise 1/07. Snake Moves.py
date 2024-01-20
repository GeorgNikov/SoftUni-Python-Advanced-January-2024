from collections import deque

rows, cols = [int(el) for el in input().split()]
word = list(input())

word_copy = deque(word)
step = 1

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    print(*[word_copy.popleft() for _ in range(cols)][::step], sep='')
    step *= -1