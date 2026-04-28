print("Hello, may I know some information about you?")
print("---------------------------------")
name = input("let's start with your name: ")
print("---------------------------------")
age = int(input(f"Okay, {name}, what is your age? "))
print("---------------------------------")

height = float(
    input("now, after we knew your name and age, what is your height? "))
print("---------------------------------")
student = bool(input(f"{name}, Are you student? "))
print("---------------------------------")

ChildrenNames = None


print(f"Type of name is \"{type(name)}\", \n type of age is {type(age)} , \n type of height is {type(height)} \n type of student {type(student)}, \n and type of Childeren Names is {type(ChildrenNames)}")
