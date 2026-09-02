def student_result(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"

    if avg >= 40:
        status = "Pass"
    else:
        status = "Fail"

    return avg, grade, status


m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

avg, grade, status = student_result(m1, m2, m3)

print("Average:", avg)
print("Grade:", grade)
print("Status:", status)