
list_a = [1, 3, 2, 5, 4, 6]

for n in list_a:
    pass
    # print(n)
    # print(n * n)
    # print(n ** 3)

for index, n in enumerate(list_a):
    # print(f"Index:{index}, N:{n}")
    pass

for i in range(20):
    # print(i)
    pass


# continue
# print and calculate list element, which is even number
import numpy as np
array_a = np.random.randint(1, 500, 20) # 1~500 任取20個隨機數 (可能重複)
list_b = list()

for element in array_a:
    if element % 2 == 1:  # odd number
        print("This is a odd number.", element)
        continue
    else:
        print("This is a even number:", element)
        list_b.append(element*2)
    print("Iteration End")

print(array_a)
print(list_b)