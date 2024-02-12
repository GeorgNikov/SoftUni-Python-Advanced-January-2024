def shop_from_grocery_list(giving_budget, g_lst, *products):
    budget = giving_budget
    grocery_list = g_lst.copy()
    shopping_list = []

    for product in products:
        product_name, product_price = product

        if product_name in grocery_list and budget >= product_price and product_name not in shopping_list:
            grocery_list.remove(product_name)
            budget -= product_price
            shopping_list.append(product_name)

        elif product_price > budget:
            break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join(str(x) for x in grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))