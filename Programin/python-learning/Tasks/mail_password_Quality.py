counter = 1
while counter <= 3:
    email = input("Please input your mail: ")
    password = input("Please input your password: ")
    print("- "*25)

    # cleaning data
    email = email.strip().lower()

    # check that mail 1- must not empty, 2- with . and @ , 3- with one @ ,
    #  4- end with .com .net .org , 5- not longer than 254 chars, must start and end with a letter or digit

    if email is None and email == "":
        print("email cannot be empty")

    elif not ('@' in email and '.' in email):
        print("email must contain @ and .")

    elif email.count("@") != 1:
        print("email must contain excatly one @")
    elif not email.endswith((".com", ".net", ".org", "edu", "gov")):
        print("email must end with .net or .org or . com ")
    elif len(email) > 254:
        print("email must be less than 254")
    elif not (email[0].isalnum() and email[-1].isalnum()):
        print("email must start with a letter or digit number")
    else:
        print("congrats, email is valid")

    # data cleaning
    password = password.strip()
    # print(password)
    # check if not empty
    if password != "" and password is None:
        print("password cannot be empty")

    # at least 8 chars
    elif len(password) < 8:
        print("password should longer than 8")

    elif not any(letter.isupper() for letter in password):
        print("must contain at least one upper case letter ")

    elif not any(letter.islower() for letter in password):
        print("must contain at least one lower case letter ")

    elif password == email:
        print("password canot be same as mail")

    elif password.count(" ") >= 1:
        print("password cannot contain spaces")

    elif not (password[0].isalnum() and password[-1].isalnum):
        print("must start and end with a letter or digit not special chars")

    else:
        print("- "*25)
        print("congrats, password is valid!")

    counter += 1
    print("- "*25)
