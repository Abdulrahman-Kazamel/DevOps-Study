data = "968-Maria, ( D@t@ Engineer );; 27y  "
modified_data = data.strip().lower().replace(
    "968-", "name: ").replace("( ", "role: ").replace(" )", "").replace(",", " |").replace(";;", " | age:").replace("@", "a").rstrip("y")


print(modified_data)
