students = int(input())

student_grades = {}

for _ in range(students):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f'{name} -> {formatted_grades} (avg: {avg_grade:.2f})')


    # print(f'{name} ->', end=' ')
    # for grade in grades:
    #     print(f'{grade:.2f}', end=' ')
    # print(f'(avg: {avg_grade:.2f})')