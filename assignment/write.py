import random

student_name=input('Enter student name: ')
mark = input('Enter mark of the student: ')

id = random.randint(1,1000)

with open('students.txt','a') as fileWrite:
    fileWrite.write(f'{id}-> name: {student_name} mark: {mark}\n')
    

