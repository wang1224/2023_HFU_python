dict_a = dict()
dict_b = {
    "class_name": "HFU_AI_engineer_course",
    "location": "Banqiao",
    "city": "New Taipei City"
}

x = 'city'
print("City: ", dict_b["city"], type(dict_b[x]))

dict_a[1] = 'A'
dict_a['A'] = 'one'
dict_a['dict_in_dict'] = dict()
print(dict_a)
print(f'Data type: { type(dict_a["dict_in_dict"]) }')

# 巢狀dict
dict_a['dict_in_dict']['X'] = 5
dict_a['dict_in_dict']['Y'] = 10
dict_a['dict_in_dict']['Z'] = 15 
print(dict_a)

# 修改同新增key
dict_a['dict_in_dict']['X'] = 9
print(dict_a)

# 不存在的key
# print(dict_a['no key here'])
print(dict_a.get('no key here', 'key not found'))


print("Before pop:", dict_a)
dict_a.pop('dict_in_dict')
print("After pop:", dict_a)



# dictionary with for loop
print("=" * 20)
for key in dict_a:  # 拿所有的key
    print(key, dict_a[key])
for key, value in dict_a.items(): # 拿 key value pair
    print(key, value)

for value in dict_a.values(): # 拿所有的value
    print(value)


# comprehension
# {
#     1: '1',
#     2: '22',
#     3: '333',
# }
## traditional-way
print("=" * 20)
dict_a = dict()
for index, number in enumerate(range(1, 10)):
    print(f"index:{index}, number:{number}")
    dict_a[number] = str(number) * (index + 1)
print(dict_a)

## comprehension
dict_a = {number:str(number) * (index + 1) for index, number in enumerate(range(1,10))}
print("Comprehension:", dict_a)




