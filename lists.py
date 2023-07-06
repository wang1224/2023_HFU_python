# Create
list_x = list()
list_y = [1, 2, 3, 4]
list_z = "This is a apple .".split()   # string to list

# new element
list_x.append("A")
list_x.append("B")
list_x.extend(['C', 'D', 'E', 'F'])
list_x.extend('G')
list_x = list_x + list_y
list_x.append(list_z)
# print(list_x)

# find and get
# print(list_x[3:7]) # DEFG
# print(list_x[3:]) # 不設定結尾
index_f = list_x.index("F")
# print(list_x[index_f:])
# print(list_x[-1:-5:-1])  # [起頭:結尾:方向(步數)]
## 翻轉後再取
reversed_f = list(reversed(list_x))
# print(reversed_f[0:4])

# Sort
temp = ['G', 'B', 'E', 'A', '1', '2', '3']
list_w = sorted(temp)
# print(f"list: {temp}")
# print(f"sorted(list) : {list_w}")
temp.sort()
# print(f"list.sort() : {temp}")

# delete
temp.pop()
# print("list.pop():", temp)
temp.remove("A")
# print("list.remove()", temp)



# List assign
list_a = [1, 2, 3, 4]
list_b = list_a # list_a.copy() 去複製一個副本給list_b
# print(list_b)
list_a.append(5)
# print(list_b) # 跟一般單數值(string, integer, float)的變數不同, 會跟著被改變
list_a.remove(2)
# print(list_b)


# iter, generator
list_iter = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]
generator = range(1, 100, 5)
print("iter: ", list_iter)
print("generator: ", generator, generator[11])


# for-loop comprehension
## traditional way
list_n_square = list()
for number in range(1, 100):
    square_n = number*number
    list_n_square.append(square_n)
print(list_n_square, len(list_n_square))
## comprehension
list_n_square_comprehension = [n*n for n in range(1, 100)]
print(list_n_square_comprehension, len(list_n_square_comprehension))

