# 1. n = 100, 平方每一項
# 2. n = 100, 平方每一項，並加到後一項

# 1.
# [1**2, 2**2, 3**2, 4**2, 5**2, 6**2, ....., 99*2]
list_power2 = list()
for number in range(100):
    number_pow2 = pow(number, 2) # number * number OR number ** 2
    list_power2.append(number_pow2)
list_power2 = [number**2 for number in range(100)]

# 2.
# [
# 1**2, 
# 1**2 + 2**2, 
# 1**2 + 2**2 + 3**2, ........, 
# 1**2+2**2+3**2+...+99*2
# ]
list_power2_stack = list()
number_stack = 0
for number in range(100):
    number_stack = number_stack + pow(number, 2) # number * number OR number ** 2
    list_power2_stack.append(number_stack)
# print(list_power2_stack)
print(list_power2_stack[-1], sum(list_power2))


