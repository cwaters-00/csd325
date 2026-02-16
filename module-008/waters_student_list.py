#chanceller Waters
#2/15/26
#8.2: JSON
#the purpose of this assignment is to read import and append a json file with a new entry.


import json
import os



#Filename defined
filename = 'C:\\\\Users\\\\chanc\\\\Downloads\\\\Student.json'


def print_students(student_list):
    for student in student_list:
        print(f'{student['F_Name']}, {student['L_Name']} :'
              f'ID ={student['Student_ID']} , Email = {student['Email']}')


if os.path.exists(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
else:

    data = []
  #Notification of original list
print("\n---____Original Student List___---")

print_students(data)
#append with new student data
new_student = {
    "F_Name": "Chanceller",
    "L_Name": "waters",
    "Student_ID": "99999",
    "Email": "cwaters@gmail.com"
}
data.append(new_student)
#notifaction of updated list
print("\n---____Updated Student List___---")

print_students(data)


with open(filename, 'w') as file:
    json.dump(data, file, indent=4)

print("\nNotice: the .json file was updated.")


