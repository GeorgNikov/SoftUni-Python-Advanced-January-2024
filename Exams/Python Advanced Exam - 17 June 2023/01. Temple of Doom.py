from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool = tools[0]
    current_substance = substances[-1]
    current_challenge = current_tool * current_substance

    if current_challenge in challenges:
        challenges.remove(current_challenge)
        tools.popleft()
        substances.pop()

    else:
        tools[0] += 1
        substances[-1] -= 1
        tools.append(tools.popleft())
        if substances[-1] == 0:
            substances.pop()

if (not tools or not substances) and challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")