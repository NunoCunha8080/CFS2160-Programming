print('Password confirmation program\n')
blocked_words = ['huddersfield', 'Huddersfield', 'HUDDERSFIELD', 'password', 'Password', 'PASSWORD', 'CHEESE', 'Cheese',
                 'cheese','programming', 'Programming', 'PROGRAMMING']

username = str(input("Enter your username: "))
student_ID = str(input("Enter your student ID: "))
first_password = str(input("Please insert your new password: "))

for x in blocked_words:
    while x in first_password:
        print("You can not have on your password the following words, " + str(blocked_words))
        first_password = str(input("Please insert your new password again: "))

while (int(len(first_password)) < 6) or (int(len(first_password)) > 12):
    print("The password has to be from 6 to 12 characters long")
    first_password = str(input("Please insert the password again: "))

second_password = str(input("Please confirm the password: "))

while second_password != first_password:
    print("Both passwords have to match")
    second_password = str(input("Please repeat the confirmation of the first password"))

print("Great! Your new password has been confirmed")
