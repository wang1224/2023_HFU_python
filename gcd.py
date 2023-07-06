import numpy as np

def great_common_divisor(numbers):
    # 輾轉相除法 -> 歐西里德算法
    bigger_one = max(numbers)
    small_one = min(numbers)
    answer = 0
    while True:
        remainder = bigger_one % small_one
        if remainder == 0:
            answer = small_one
            break
        else:
            bigger_one, small_one = small_one, remainder
    gcd = answer
    return gcd

if __name__ == '__main__':
    numbers = np.random.choice(10000, 2)
    answer = great_common_divisor(numbers)
    print(numbers, answer)
