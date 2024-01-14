from collections import deque

material = list(map(int, input().split()))
magic = deque(map(int, input().split()))

toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}