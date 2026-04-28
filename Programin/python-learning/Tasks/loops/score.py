# =====================================================
#  starting with loops
# =====================================================


scores = [150, 30, 200, 90]
total = 0


for score in scores:
    total += score
    # print(f"total is: {total}")

# print(f"final total is: {total}")


# =====================================================
#  cleaning and transforming data
# =====================================================


# files = [" Report.cSV", "DATA.csv ", " FINAL.TXT "]
# new_files = ""
# # data cleaning
# for file in files:
#     file = file.strip().lower()
#     if not file.endswith(".csv"):
#         print(f"some files not csv format, as {file}")
#         continue  # better here to use break but i use diffrent concept
#     new_files += file.strip().lower() + " "
# else:
#     print(f"the the csv files are : {new_files.split()}")

# =====================================================
# print the 7 times table from 1 to 10 using for
# =====================================================

# for r in range(1, 11):
#     print(f" 7 * {r} = {7 * r} ")

# =====================================================
# builf left pyramid of 6 stars
# =====================================================

# stars = [1, 2, 3, 4, 5, 6]
# for star in stars:
#     print("*" * star)
