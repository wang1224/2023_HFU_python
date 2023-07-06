import numpy as np
a = np.random.randint(1, 5)
b = np.random.randint(1, 5)

if a > b:
    print("a > b", a, b)
elif a == b:
    print("a = b", a, b)
else:
    print("a < b", a, b)

print("End")  

# if-else with dictionary
dict_a = {
    1:"A",
    2:"B"
}
# 判斷一個key 3, 是否出現在dict_a之中
if 3 in dict_a:
    print("Find it:", dict_a[3])
else:
    dict_a[3] = 'C'


