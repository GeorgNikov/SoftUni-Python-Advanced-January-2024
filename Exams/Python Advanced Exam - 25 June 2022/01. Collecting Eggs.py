from collections import deque


# Switch first and last element in Steck: paper
def switch_paper(paper):
    result = paper.copy()
    result[0], result[-1] = result[-1], result[0]

    return result


eggs = deque([int(x) for x in input().split(', ')])
paper = list([int(x) for x in input().split(', ')])

box_size = 50
boxes = 0

while eggs and paper:
    current_eggs = eggs[0]
    current_paper = paper[-1]

    if current_eggs <= 0 or current_eggs == 13:
        eggs.popleft()
        if current_eggs == 13:
            paper = switch_paper(paper)
        continue

    if current_eggs + current_paper <= box_size:
        boxes += 1
    eggs.popleft()
    paper.pop()

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper])}")