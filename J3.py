def calculate_student_gpa(daneshju):
    grades = daneshju["grades"]

    total = 0
    count = 0

    for g in grades:
        total = total + g
        count = count + 1

    gpa = total / count
    return gpa

students_list = [
    {"name": "Ali", "student_id": 1, "grades": [18, 19, 20]},
    {"name": "Zahra", "student_id": 2, "grades": [15, 14, 16.5]}
]

for st in students_list:
    gpa = calculate_student_gpa(st)
    print("Name:", st["name"], "GPA:", gpa)