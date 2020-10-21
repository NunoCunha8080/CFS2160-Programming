'''Practical Task1'''
import math

print("Program to divide students by lab")
print()
nr_students = int(input("Insert the number of students to be divided: "))
nr_PC = int(input("Insert the number of pc's that are in each lab: "))

if nr_students <= 0:
    print("Please enter a valid number of students")
    nr_students = int(input("Enter the number of students to be divided: "))
elif nr_PC <= -1 and nr_PC <= 0:
    print("Please enter a valid number of computers")
    nr_PC = int(input("Enter the number of pc's that are in each lab: "))

nr_labs = nr_students / nr_PC

if nr_labs < 2:
    print("You will need " + str(math.ceil(nr_labs)) + " labs for all students")
else:
    print(" You will need " + str(math.ceil(nr_labs)) + " labs for all students")
