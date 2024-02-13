def softuni_students(*args, **kwargs):
    valid = {}
    invalid = []

    for id, username in args:
        if id in kwargs:
            valid.setdefault(username, []).append(kwargs[id])
        else:
            invalid.append(username)

    sorted_valid = sorted(valid.items())

    result = []
    invalid_result = []

    for username, course in sorted_valid:
        result.append(f"*** A student with the username {username} has successfully"
                      f" finished the course {''.join(course)}!")

    if invalid:
        for username in sorted(invalid):
            invalid_result.append(username)

        result.append("!!! Invalid course students: " f"{', '.join(invalid_result)}")

    return '\n'.join(result)



print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))