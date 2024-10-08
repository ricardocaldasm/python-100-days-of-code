import random
import pandas

# LIST COMPREHENSION
lista = list()
name = "Ricardo"
for i in name:
    lista.append(i)
print(lista)

lista_1 = [i for i in name]
print(lista_1)

# DICTIONARY COMPREHENSION
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(0, 100) for student in names}
print(students_score)
passed_students = {
    student: score for student, score in students_score.items() if score > 60
}
print(passed_students)

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("-" * 20)
for index, row in student_data_frame.iterrows(): #iterrows only in Pandas
    print(index)
    print(row)  # possible row.student or row.score
    print(row.student)
    print(row.score)


