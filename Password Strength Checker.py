def Password():
    user_password = input("Enter Your Password> ")
    return user_password

def strength_checker(user_password):
    password_point = 0
    Uppercase = any(char.isupper() for char in user_password)
    Lowercase = any(char.islower() for char in user_password)
    Digit = any(char.isdigit() for char in user_password)
    Special_characters = any(not char.isalnum() for char in user_password)
    length = len(user_password)
    return password_point,Uppercase,Lowercase,Digit,Special_characters,length

def Strength_result(password_point,Uppercase,Lowercase,Digit,Special_characters,length):
    print('''----- Password Analysis -----''')

    if Uppercase == True:
        password_point += 1
        print("Uppercase letters: Present")
    else:
        password_point += 0
        print("Uppercase letters: Missing")

    if Lowercase == True:
        password_point += 1
        print("Lowercase letters: Present")
    else:
        password_point += 0
        print("Lowercase letters: Missing")

    if Digit == True:
        password_point += 1
        print("Numbers: Present")
    else:
        password_point += 0
        print("Numbers: Missing")

    if Special_characters == True:
        password_point += 1
        print("Special characters: Present")
    else:
        password_point += 0
        print("Special characters: Missing")

    if length >= 8:
        password_point += 1
        print("Length: Sufficient")
    else:
        password_point += 0
        print("Length: Insufficient")

    if password_point == 5:
        print("Password Strength: Strong")
    elif password_point >= 3 and (Special_characters == False or length <= 8 or length > 8):
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Weak")

def main():
   user_password = Password()
   results = strength_checker(user_password)
   Strength_result(*results)


main()