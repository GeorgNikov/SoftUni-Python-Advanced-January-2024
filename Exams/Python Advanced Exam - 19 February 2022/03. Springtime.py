def start_spring(**kwargs):
    result = {}
    final = []
    for k, v in kwargs.items():
        result.setdefault(v, []).append(k)

    sorted_values = {key: sorted(value) for key, value in result.items()}
    sorted_result = dict(sorted(sorted_values.items(), key=lambda x: (-len(x[1]), x)))

    for key, value in sorted_result.items():
        final.append(f"{key}:")
        final.extend([f"-{obj}" for obj in value])

    return "\n".join(final)





example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
