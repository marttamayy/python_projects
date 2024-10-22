student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def calculate_grade(number):
    if number <= 70:
        return "Fail"
    elif number <= 80:
        return "Acceptable"
    elif number <= 90:
        return "Exceeds Expectations"
    elif number <= 100:
        return "Outstanding"
    else:
        return "ERROR. Value out of range."


student_grades = {student: calculate_grade(score) for student, score in student_scores.items()}

print(student_grades)