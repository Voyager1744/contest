
grades_values = {"A": 26, "B": 25, "C": 24, "D": 23, "E": 22, "F": 21, "G": 20, "H": 19, "I": 18, "J": 17, "K": 16, "L": 15, "M": 14, "N": 13, "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T": 7, "U": 6, "V": 5, "W": 4, "X": 3, "Y": 2, "Z": 1}
grades = list(input())
if len(grades) == 0:
    print(" ")
    exit()
total_grade = sum(grades_values[letter] for letter in grades)
average_grade = total_grade / len(grades)

worst_grade = min(grades_values[letter] for letter in grades)

if average_grade - worst_grade > 1:
    average_grade = worst_grade + 1

for grade, value in grades_values.items():
    if value == round(average_grade):
        print(grade)
