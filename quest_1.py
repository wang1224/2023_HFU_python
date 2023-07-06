list_name   = ["Tony", "David", "Danny"]
list_height = [176, 185, 157]

# list_of_tuples = [(name_1,height_1), (...), (...), (...)]
# ans.1
print("="*20)
list_of_tuples = list()
# list_of_tuples.append((list_name[0], list_height[0]))
# list_of_tuples.append((list_name[1], list_height[1]))
# list_of_tuples.append((list_name[2], list_height[2]))
for index, name in enumerate(list_name):
    height = list_height[index]
    list_of_tuples.append((name, height))

print(list_of_tuples) # iter

# ans.2
print("="*20)
generator_of_tuples = zip(list_name, list_height)
# print(generator_of_tuples, list(generator_of_tuples))  # 轉成list -> 一次生完全部
for tuple in generator_of_tuples:
    print(tuple)









print("="*20)
print("Sorted name & height", sorted(list_of_tuples))  # 用名字做排序
# key=lambda x: (x[1], x[0])
print("Sorted name & height with different key (height)", sorted(list_of_tuples, key=lambda x:(x[1],x[0]))) 
sorted_list_of_tuples = sorted(list_of_tuples, key=lambda x:(x[1],x[0]), reverse=True)
print("Sorted name & height with reverse", sorted_list_of_tuples) 