def cookbook(*foods):
    result = {}

    for food in foods:
        recipe, cuisine, ingredients = food
        result.setdefault(cuisine, [])
        result[cuisine].append(f"  * {recipe} -> Ingredients: {', '.join(ingredients)}")

    sorted_values = {key: sorted(value) for key, value in result.items()}
    sorted_result = dict(sorted(sorted_values.items(), key=lambda x: (-len(x[1]), x)))

    final_result = []

    for key, value in sorted_result.items():
        final_result.append(f"{key} cuisine contains {len(value)} recipes:")
        final_result.extend([f"{obj}" for obj in value])

    return "\n".join(final_result)




print(cookbook(
                    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
                      ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
                      ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
                      ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
                      ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
                      ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
                      ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
                      ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))




print()
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print()

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
