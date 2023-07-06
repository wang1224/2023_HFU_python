import matplotlib.pyplot as plt

# 假設有一些點的座標資料
x = [1, 2, 3, 4, 5]  # x 座標
y = [2, 4, 6, 8, 10]  # y 座標

# 繪製點狀圖
plt.scatter(x, y)
plt.plot(x, y, linestyle='dashed', color='red')
# 設定圖表標題與軸標籤
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("stack price")
plt.legend(["price", "flow"])
plt.savefig('.\plots\scatter_1.jpg') # 存圖
# 顯示圖表
plt.show()