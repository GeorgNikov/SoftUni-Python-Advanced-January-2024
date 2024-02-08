def shopping_cart(*args):
    cart_list = [x for x in args if x != 'Stop']
    stop_index = args.index('Stop')
    cart = {"Pizza": [], "Soup": [], "Dessert": []}
    final_cart = []

    for i in range(stop_index):
        meal = cart_list[i][0]
        product = cart_list[i][1]

        if meal == 'Pizza' and len(cart['Pizza']) == 4:
            continue
        elif meal == "Soup" and len(cart["Soup"]) == 3:
            continue
        elif meal == "Dessert" and len(cart["Dessert"]) == 2:
            continue
        elif product not in cart[meal]:
            cart[meal].append(product)
            continue

    for value in cart.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in sorted_cart:
        final_cart.append(f"{key}:")
        final_cart.extend([f" - {obj}" for obj in sorted(value)])

    return "\n".join(final_cart)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
