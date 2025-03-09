def checkLength(password):
    long = 0
    for i in range(len(password)):
        long += 1
    if long < 8:
        looong = "Must be at least 8 characters long. "
    else:
        looong = ""
    return looong

def checkUpperLower(password):
    upper = 0
    lower = 0
    for i in range(len(password)):
        if password[i].isupper():
            upper += 1
        if password[i].islower():
            lower += 1
    if upper == 0 or lower == 0:
        upperlower = "Must contain both uppercase and lowercase letters. "
    else:
        upperlower = ""
    return upperlower

def checkSpecialCharacter(password):
    special = 0
    for i in range(len(password)):
        if "!" in password[i] or "@" in password[i] or "#" in password[i]:
            special += 1
    if special == 0:
        bad = "Must include at least one special character (!, @, #)."
    else:
        bad = ""
    return bad


# usr = input("Enter a password: ")
#
# leng = checkLength(usr)
# print(leng)
#
# lowerupper = checkUpperLower(usr)
# print(lowerupper)
#
# usr2 = checkSpecialCharacter(usr)
# print(usr2)

q = 1
while q:
    usr = input("Enter a password: ")
    leng = checkLength(usr)
    lowerupper = checkUpperLower(usr)
    usr2 = checkSpecialCharacter(usr)

    if leng == "" and lowerupper == "" and usr2 == "":
        print("Password is strong!")
        break
    else:
        print("Password does not meet the requirements:",leng, end="")
        print(lowerupper, end="")
        print(usr2)