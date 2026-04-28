# check username is not empty and age above 18
username = "",
age = 19
# print(username is not None and username != "" and age > 18)
# -------------------------------

# check if the password is 8 charcters long and doesnot conatin spaces
password = " mypassword"
# print(len(password.strip()) >= 8)
# -------------------------------

# check if user mail not empty , contains @ , and ends with .com
user_mail = " abdulrah@amn.com"
modified_user_mail = user_mail.strip().lower()
# print(modified_user_mail is not None and modified_user_mail !=
#       "" and "@" in modified_user_mail and modified_user_mail.endswith(".com"))
# -------------------------------

# check is username is string , not none , longer than 5
user_name = None
# is instanse checks if the object in not None
# I have added this step here to avoid error while dealing with int, and sure could be removed from the check below
if isinstance(user_name, str):
    modified_user_name = user_name.strip().lower()
    print(isinstance(modified_user_name, str)
          and modified_user_name is not None and len(modified_user_name) > 5)
# else:
    # print("please enter alphabet letters")
# -------------------------------

roles = ['admin', 'moderator', 'normal']
banned_users = ['abdullah', 'moamen']

user_role = 'admin'
user_name = 'Abdulrahamn'
is_verfied = False
print(user_role in roles[:-1] and user_name not in banned_users and is_verfied)


# -------------------------------
