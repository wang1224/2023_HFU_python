from matplotlib import pyplot as plt

# 長條圖
plt.plot([1, 2, 3, 4], 'o-r') # 畫線
plt.plot([4, 3, 2, 1], 'o--y') # 畫線
plt.ylabel('some numbers')    # 改 y軸的顯示名稱 為 'some numbers'
plt.xlabel('index of numbers')
plt.legend(["upstair", "downstair"])
# ticks: range(4): 欲更換的座標0~4, 其餘部分會被消除
# labels: 後面部分是更換成甚麼東西
plt.xticks(range(4), [f"idx:{i}"  for i in range(4)], rotation=20)
plt.savefig('.\plots\plot_1.jpg') # 存圖
# plt.show()  # 顯示圖