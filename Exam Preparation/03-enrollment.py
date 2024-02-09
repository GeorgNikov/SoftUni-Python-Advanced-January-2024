def gather_credits(given_credits, *course_info):
    courses = {}

    for course_name, my_credits in course_info:
        if sum(courses.values()) >= given_credits:
            break

        if course_name not in courses:
            courses[course_name] = my_credits

    if sum(courses.values()) >= given_credits:
        return (f"Enrollment finished! Maximum credits: {sum(courses.values())}.\n"
                f"Courses: {', '.join(sorted(courses))}")
    return f"You need to enroll in more courses! You have to gather {given_credits - sum(courses.values())} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
