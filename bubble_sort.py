import numpy as np

def bubble_sort(numbers):
    for round in range(1, len(numbers)): # 幾輪
        for index in range(len(numbers) - round): # 3. 每一輪做的事 
            current_bubble, next_bubble = numbers[index],  numbers[index + 1]
            if current_bubble > next_bubble:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
    sorted_numbers = numbers
    return sorted_numbers

if __name__ == '__main__':
    # 1. 每一輪去比較數字, 最大的數字跑到最後面去
    # 2. 共要跑 n - 1 輪
    # 3. 每一輪要越跑越少個 (不用跑後面的幾個, 因為已經確定是最大的了)
    # 時間複雜度關注的是: 你的資料長度若為n, 則你的演算法執行時間與資料長度的關係
    # 時間複雜度是 O(n**2), 代表你的演算法執行時間與 n**2成線性關係
    # 時間複雜度是 O(log(n)), 代表你的演算法執行時間與 log(n)成線性關係
    # Bubble sort 的時間複雜度為 O(n**2) 
    # -> 執行幾次比較與交換: (n-1), (n-2), .... 1 -> (n-1+1)(n-1)/2 -> n*(n-1)/2 
    
    # Code As Description
    for i in range(5):
        bubbles = np.random.choice(100, 10)
        print(i, bubbles)
        result = bubble_sort(bubbles)
        print(i, result)