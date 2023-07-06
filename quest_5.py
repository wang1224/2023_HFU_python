# 1. 直角三角形
# 2. 置中的三角形
# 3. 靠右的直角三角形

# 1.
# *
# * *
# * * *
# * * * *
# * * * * *
for row_number in range(1, 10):
    # print("* " * row_number)
    pass

# 2.
#    *
#   * *
#  * * *
# * * * *
#* * * * *
level = 10
for row_number in range(1, level + 1):
    print(" " * (level - row_number), "* " * row_number)
    pass

# 3.
# level=4
#      *  6|1  2*4-2|1 4+1=5=level+1
#    * *  4|2  2*3-2|2 3+2=5=level+1
#  * * *  2|3  2*2-2|3 2+3=5=level+1
#* * * *  0|4  2*1-2|4 1+4=5=level+1
#空白個數 = 2*x-2 = 2*(x-1), x+row = level+1, x = level+1-row
level = 10
for row_number in range(1, level + 1):
    space_number = 2 * (level - row_number)
    print("-" * space_number + "* " * row_number)