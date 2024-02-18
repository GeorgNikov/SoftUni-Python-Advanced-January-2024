from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices_of_foods = deque([int(x) for x in input().split()])
total_foods = len(prices_of_foods)
pocket = 0
eaten_food = 0

while amount_of_money and prices_of_foods:
    current_money = amount_of_money[-1]
    current_food = prices_of_foods[0]

    if current_money == current_food:
        amount_of_money.pop()
        prices_of_foods.popleft()
        eaten_food += 1

    elif current_money > current_food:
        diff = current_money - current_food
        pocket += diff
        amount_of_money.pop()
        if amount_of_money:
            amount_of_money[-1] += diff
        prices_of_foods.popleft()
        eaten_food += 1

    elif current_food > current_money:
        amount_of_money.pop()
        prices_of_foods.popleft()

if eaten_food == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif eaten_food < 4:
    if eaten_food == 1:
        print(f"Henry ate: {eaten_food} food.")
    else:
        print(f"Henry ate: {eaten_food} foods.")
