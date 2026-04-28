# print("a" in "ABdulrahman")


# name = input("please enter your name: ")

brothers = ["Ali", "Ahmed", "Abdulrahman", "Abdullah"]

# print(name.capitalize() not in brothers)

print("----------------------------------")

domain = "binsabri.com"
domain = "bot.com"
# in the future i want to make this via api
banned_domains = ['fake.com', 'bot.com', 'spam.com']
# print(domain not in banned_domains)

print("----------------------------------")

# ----------------------------------
a = [1, 2, 3]
b = [1, 2, 3]
# print(a == b)  # checking only the values
# checking identity if the have the same ID on memory/ pointing to same ID in mem
# print(a is b)
# ----------------------------------
c = a
# print(c is a)  # true
# ----------------------------------
a = 1
b = 1
# print(a == b)
# print(a is b)
# ----------------------------------

# data quality to check user entered mail or not

# print(email != None and email != "")
# print(email is not None and email != "") #better
# ----------------------------------


# check that mail 1- must not empty, 2- with . and @ , 3- with one @ ,
#  4- end with .com .net .org , 5- not longer than 254 chars, must start and end with a letter or digit

email = "a-z@.com"
# cleaning data
email = email.strip()

# if ((email is not None and email != "") and ('@' in email and '.' in email) and
#         (email.endswith((".com", ".net", ".org"))) and (0 < len(email) < 254)
#     and (email.startswith(("a-z")))

#         ):
#     print(True)
# else:
#     print(False)
# above is my way and as you see it's messy
# better way by using elif
