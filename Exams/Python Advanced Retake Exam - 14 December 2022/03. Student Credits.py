import operator


def students_credits(*course_info):
    courses = {}
    diyan_credits = 0

    for course in course_info:
        course_name, credits, max_test_points, points = course.split('-')
        percent = int(points) / int(max_test_points)
        total = percent * int(credits)
        diyan_credits += float(total)

        courses[course_name] = float(total)

    sorted_courses = dict(sorted(courses.items(), key=operator.itemgetter(1), reverse=True))
    result = []

    if diyan_credits >= 240:
        result.append(f"Diyan gets a diploma with {diyan_credits:.1f} credits.")
    else:
        diff = 240 - diyan_credits
        result.append(f"Diyan needs {diff:.1f} credits more for a diploma.")

    for key, value in sorted_courses.items():
        result.append(f"{key} - {value:.1f}")

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print()

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
