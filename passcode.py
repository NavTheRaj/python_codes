#PROGRAM TO ENTER THE PASSWORD THAT HAS ALL PASSWORD REQUIREMENTS

digit_flag=False
upper_flag=False
lower_flag=False
special_flag=False

password_accept=False

password=input('Enter a password\n')

while password_accept==False :
    for char in password:
        if char.isdigit():
            digit_flag=True
        if char.isupper():
            upper_flag=True
        if char.islower():
            lower_flag=True
        if not(char.isdigit()) and not(char.isalpha()):
            special_flag=True

    if digit_flag and upper_flag and lower_flag and special_flag and len(password)>=8:
        print("Password is valid")
        password_accept=True
    else:
        password=input('Password is not valid\nEnter password again\n')
        password_accept=False
