from gcd import great_common_divisor
from arithmetic_sequence import arithmetic_sequence
from bubble_sort import bubble_sort


gcd_number = great_common_divisor([100, 400])
print("gcd: ", gcd_number)

a_s_1 = arithmetic_sequence(5, 15, 10)
a_s_2 = arithmetic_sequence(d=10, N=20)
print("a_s_1: ", a_s_1)
print("a_s_2: ", a_s_2)

sorted_numbers = bubble_sort([1, 5, 7, 9, 4])
print("bubble sort: ", sorted_numbers)

