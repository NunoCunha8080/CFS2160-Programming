'''Task 2'''
import getpass

print('Password confirmation program\n')

first_password = str(input("Please Insert the password: "))

while (int(len(first_password)) < 6) or (int(len(first_password)) > 12):
    print("The password has to be from 6 to 12 characters long")
    first_password = str(input("Please insert the password again: "))

second_password=str(input("Please repeat the password: "))

if first_password==second_password:
    print("Password has been confirmed!")



