# for i in (1, 2, 3):
#     if i == 2:
#         break
#     print(i)


# =====================================================
#  check names quality
# =====================================================

# brothers = ["ali", "ahmed", "     ", "abdullah"]
# for bro in brothers:
#     if bro.strip() == "":
#         continue
#     print(bro)

# =====================================================
#  print working days
# =====================================================

# days = ["Sat", "Sun", "Mon", "Tue", "Wen", "Thr", "Fri"]
# weekend = ["Sat", "Fri"]  # instructor Idea
# for day in days:
#     if day in weekend:  # or if day == "Sat" or day == "Fri":
#         continue
#     print(day)
# else:
#     print("end/ completted normally/ succsuflly without any interaption")

# =====================================================
#  SQL Injection attack
# =====================================================

# emails = ["ABdulrahmanKazamel@gmail.com",
#           "AliSabri@binsabri.com",
#           "DROP TABLE USERS;",
#           "Ahmedsabri@binsabri.com"]

# for email in emails:
#     if ";" in email:
#         print("SQL Injection Attack!! from a hacker!!")
#         break
#     print(email)
# else:
#     print("end")


# =====================================================
# check duplicates data
# =====================================================

# file_list = ['report.csv', 'data.xlsx',
#              'data.csv', ' summry.docx', ]

# if len(file_list) != len(set(file_list)):
#     print("there is duplicats")


# else:
#     print("no duplicates")


# =====================================================
# nested loops
# =====================================================

# clothes = ['T-Shirt', 'Toruzer', 'Shirt']
# sizes = ['xs', 's', 'm', 'l']

# for cloth in clothes:
#     for size in sizes:
#         print(f"{cloth} Size: {size}")

#     print("----------------------------")

# =====================================================
# nested loops
# =====================================================

# years = [2025, 2026]
# months = ["Jan", "Feb", "Mar", "Apr", "May", 6, 7, 8, 9, 10, 11, 12]
# days = range(1, 31)
# for year in years:
#     for month in months:
#         for day in days:
#             print(f"report_{day}_{month}_{year}.csv")


# =====================================================
# nested loops
# =====================================================

# SELECT count(*) FROM customers WHERE id IS NULL;


# tables = ['customers', 'orders', 'products', 'prices']
# columns = ['id', 'create_date']

# for table in tables:
#     for column in columns:
#         print(f"SELECT count(*) FROM {table} WHERE {column} IS NULL;")


# # =====================================================
# while loopos
# =====================================================
attempts = 0

answer = ""

while attempts < 3:
    answer = input("Do you Agree Yes/ no: ")
    if answer == "yes":
        print("Glad, we are on the same page.")
        break
    attempts += 1

else:
    print("3 strikes, You are out!")
