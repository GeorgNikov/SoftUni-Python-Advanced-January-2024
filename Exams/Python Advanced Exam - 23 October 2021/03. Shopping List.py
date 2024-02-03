def shopping_list(money, **kwargs):
    budget = money
    orders = ''
    products_limit = 5

    if budget >= 100:
        for product_name, value in kwargs.items():
            total_price = value[0] * value[1]
            if total_price < budget:
                budget -= total_price
                orders += f"You bought {product_name} for {total_price:.2f} leva.\n"
                products_limit -= 1

            if products_limit == 0:
                break
    else:
        return "You do not have enough budget."
    return orders

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10),))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))