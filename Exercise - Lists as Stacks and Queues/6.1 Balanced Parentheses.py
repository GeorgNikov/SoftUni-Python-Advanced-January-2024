from collections import deque

sequence = deque(input())
open_brackets = '({['
closed_brackets = ')}]'
count = 0

while sequence and count < len(sequence) / 2:
    if sequence[0] not in open_brackets:
        break
    current_index = open_brackets.index(sequence[0])
    if sequence[1] == closed_brackets[current_index]:
        sequence.popleft()
        sequence.popleft()
        sequence.rotate(count)
        count = 0
    else:
        sequence.rotate(-1)
        count += 1

if sequence:
    print('NO')
else:
    print('YES')
