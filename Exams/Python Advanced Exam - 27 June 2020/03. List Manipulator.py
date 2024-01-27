def list_manipulator(numbers, command, where, *args):
    sub_list = [*args]
    index = (args[0] if len(args) > 0 else 1)

    commands = {
        "add": {
            "beginning": [x for x in sub_list + numbers],
            "end": [x for x in numbers + sub_list],
        },
        "remove": {
            "beginning": numbers[index:],
            "end": numbers[:-index],
        }
    }

    return commands[command][where]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
