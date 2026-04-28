is_banned = False
# in first case let's say the website allow login with (any) of those
email = ""
user_name = "abdulrahmanKazamel"
phone_number = ""


# print(any([email, user_name, phone_number]))

# zero and blank is false regarding to bool check
email = ""
user_name = ""
phone_number = 0


# print(any([email, user_name, phone_number]))


# then another page of us allows login with full credianials which means (all) data should be inserted
# print(all([email, user_name, phone_number]))


# check if user and password is correct
email = "Abdulrahmankazamel@gmail.com"
password = "P@ssw0rd"
user_name = "abdulrahman Kazamel"

user_email = input("please enter your mail: \n")
user_password = input("please enter your password: ")

print(
    f"given mail is {user_email.capitalize()} and given password is {user_password}")

# for i in range(3):
if is_banned == False:
    if (user_email.capitalize().strip() == email and user_password == password):
        print(f"{user_name.title()} logged in successfully!")
    elif (user_email == "" or password == ""):  # why it works only with or
        print("welcom guest!")
    else:
        print("please enter correct mail and password")


# is_logged_in = True
# is_guest = False
# is_banned = False

# this to remoember that and is executed before or ,
# for that we need to wrap or with () to give it priority

# print((is_logged_in or is_guest) and not is_banned)
