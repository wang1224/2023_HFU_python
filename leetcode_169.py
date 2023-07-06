from collections import Counter
import numpy as np

n = np.random.randint(low=1, high=5*10**4)
# major element: 出現超過 n/2 次
major_element = np.random.randint(low=-1*10**9, high=10**9)
major_part  = np.full(n - n//2, major_element)    # n - n//2
remain_part = np.random.randint(low=-1*10**9, high=10**9, size=n//2) # n//2
nums = np.concatenate([major_part, remain_part])
np.random.shuffle(nums)

print(n, len(nums))

# 包含不夠全面的資料, 可能測試不出來問題
# nums = [1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1]
counter = Counter(nums)
ans = counter.most_common(1)
print(ans, ans[0][0])


