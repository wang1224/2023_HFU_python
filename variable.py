# x = "hello world"
# print(x)
# x = x + x

# number = 100
# number_divide_nine = number / 9
# print("1:", number_divide_nine, number // 9, number + 78, number - 81, number % 6)
# print("2:", number)
number = 200
# print("3:", number)
# print("4: ", abs(number), max(number, 300), min(number, 300), pow(number, 3))
# print("5: ", number ** 3, number * 3)

import math
# print("6: ", round(math.sqrt(abs(number)), 2))
number_log2 = round(math.log2(number), 2)
print("A: ", number_log2, math.log10(number), math.log(number))
print("A reverse: ", math.exp2(number_log2))

gcd = math.gcd(120, 250, 130)
print(gcd)

print("Floor and Ceil: ", math.floor(2.37), math.ceil(2.37))
# sin(60度) = 3**0.5/2, cos(60度) = 1/2
print("Sin Cos Tan", math.sin(math.radians(60)), (3 ** 0.5) / 2, math.cos(math.radians(60)), math.tan(math.radians(60)))



