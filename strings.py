string_a = "Hello everybody!"
# print(string_a.lower())
# print(string_a.upper())
# print(string_a.capitalize(), "peter".capitalize())
# print(string_a.replace("e", "E"))
# print(string_a.replace(" ", " ~ "))

string_b = "   This is a string with lots of spacessssss  ".strip()
# print(string_b)
# print(string_a + string_b)
# print(f"{string_a},      {string_b}") # f-string
# # print(string_a, ",     ", string_b)

string_c = "ABCD"
print("*3: ", string_c + string_c + string_c)
print("*3: ", string_c * 3) # repeat
print("--" * 20)
print(string_c.find("CD")) # find lowest index of apperance
# 0 1 2 3
print(string_c[3], string_c[2]) # D
print(string_c.endswith("AB"))

