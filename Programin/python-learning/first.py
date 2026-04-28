# if True:

#     print("""Your Learning Path:
#           \t- Python Basics
#           \t- Data Engineering
#           \t- AI""")


# help("keywords")  # minute 18
import random
import math

print("------------------------------")

domain = "BinSabri.com"

# print("info@", domain)
# print("support@", domain)
# print(f"www.{domain} ")

# print("------------------------------")

# if len(domain) < 15:
#     print("this domain might be fake!")
# else:
#     print("lenghth of domain are ", len(domain))

print("------------------------------")


text = """
ali is my brother
ali is kind 
Ali is giving support
"""
lowereText = text.strip().lower().count("ali")
# print(lowereText)

textWithDoubleQouts = "ali is my brother ali is kind, Ali is giving support,but ALI is "

loweredDoubledText = textWithDoubleQouts.lower().count("ali")
# print(loweredDoubledText)

# 11111  also not working ///////////////


aliBirthDate = "1990/9/10"
modifiedDate = aliBirthDate.replace("/", "-")

# print(modifiedDate)


price = "$1,234.99"
floatedPrice = price.replace("$", "").replace(",", "")
# print(floatedPrice)


phoneNumber = "+49 (176) 123-4567"
modifiedPhoneNumber = phoneNumber.replace(
    "+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
# print(
#     f"old phone number is {phoneNumber} and modified is {modifiedPhoneNumber} ")

# print("------------------------------")

#  help()
data = "Adam-24-USA"
data_Name = data[0: 4]  # .split("-")
# data_age=
# data_country=

# print(f"{data_Name}")


phoneOne = "+49-176-12345"
phoneTwo = "49-196-12345"
phoneThree = "0049-116-12345"

# print(phoneOne[phoneOne.find("-")+1:])
# print(phoneTwo[phoneTwo.find("-")+1:])
# print(phoneThree[phoneThree.find("-")+1:])

# print(phone.find("+009"))
# print("+" in phone)
# print(phone.startswith("+49"))


price = 33.54879865


# print(math.floor(price))
# print(math.ceil(price))
# print(round(price))

price = 10.5
# oh half , round rounds the number to the closest even whatever its on celing or on the floor
# print(round(price))


price = 33.54879865
# print(round(price, 2))

# truncate focus only on whole number
# math.trunc /// same to int , but better to use trunc when using math to avoid thinking about string converting


myrandomNumber = random.random()  # issue is only between 0 - 1 and un controlled
# print(myrandomNumber)

myrandIntNumber = random.randint(1, 100)
if (myrandIntNumber % 2 == 0):
    print(myrandIntNumber)


age = 45

print(18 <= age <= 30)
