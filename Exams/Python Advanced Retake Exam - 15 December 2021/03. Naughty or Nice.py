def naughty_or_nice_list (lst, *args, **kwargs):
    names = lst.copy()
    naughty = []
    nice = []
    not_found = []

    if args:
        for arg in args:
            num, adjective = arg.split('-')
            num = int(num)
            match = [x for x in names if x[0] == num]
            if len(match) == 1:
                if adjective == "Naughty":
                    naughty.append(match[0][1])
                elif adjective == "Nice":
                    nice.append(match[0][1])
                names.remove(match[0])

    if kwargs:
        for name, adjective in kwargs.items():
            match = [x for x in names if x[1] == name]
            if len(match) == 1:
                if adjective == "Naughty":
                    naughty.append(name)
                elif adjective == "Nice":
                    nice.append(name)
                names.remove(match[0])

    for _, name in names:
        not_found.append(name)

    result = []
    if nice:
        result.append(f"Nice: {', '.join(nice)}")
    if naughty:
        result.append(f"Naughty: {', '.join(naughty)}")
    if not_found:
        result.append(f"Not found: {', '.join(not_found)}")

    return "\n".join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))