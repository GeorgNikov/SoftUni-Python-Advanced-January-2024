def stock_availability(lst, action, *args):
    box = lst.copy()
    orders = [*args]

    if action == 'delivery':
        sub = [item for item in orders]
        box.extend(sub)

    elif action == 'sell':
        if not orders:
            box.pop(0)
        else:
            if str(orders[0]).isdigit():
                for _ in range(orders[0]):
                    box.pop(0)
            elif orders[0].isalpha():
                for i in range(len(orders)):
                    if orders[i] in box:
                        box = [item for item in box if item != orders[i]]
    return box


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie", "banana"))