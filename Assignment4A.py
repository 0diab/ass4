usrInput = input("Enter a string: ")

def format_word(firstLetter):
    capitalized_word = firstLetter.capitalize()
    return capitalized_word

def convert_to_pascal_case(usrin):
    stringer = ""
    word = ""
    for i in range(len(usrin)):
        if usrin[i] != " ":
            word += usrin[i]
        else:
            if word:
                stringer += format_word(word)
                word = ""
    if word:
        stringer += format_word(word)
    return stringer

usr2 = convert_to_pascal_case(usrInput)
print("Pascal Case:", usr2)
