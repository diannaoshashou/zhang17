# %% 第1题
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

np.random.seed(1)
x = np.arange(20)
y = np.random.randn(20)

plt.figure(figsize=(12, 6))
plt.suptitle("图表XX-YY")

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("子图1")
plt.xlabel("X轴模型标")
plt.ylabel("Y轴纵坐标")
plt.ylim(-3, 4)
plt.annotate("图表注释", xy=(2, 2), xytext=(3, 3), arrowprops=dict(arrowstyle="-|>"))

plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.title("子图2")
plt.xlabel("X轴模型标")
plt.ylabel("Y轴纵坐标")

plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.title("子图3")
plt.xlabel("X轴模型标")
plt.ylabel("Y轴纵坐标")

plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.title("子图4")
plt.xlabel("X轴模型标")
plt.ylabel("Y轴纵坐标")

plt.show()


# %% 第2题
np.random.seed(2)
data = np.random.randint(0, 100, (4, 3))
df = pd.DataFrame(data, index=["A", "B", "C", "D"], columns=["一", "二", "三"])
df.plot(kind="barh", title="柱状图")
plt.show()


# %% 第3题
np.random.seed(3)
data = np.random.randint(0, 91, (3, 3))
df = pd.DataFrame(data, index=["语文", "数学", "英语"], columns=["一", "二", "三"])
df.plot(kind="bar", title="柱状图")
plt.show()


# %% 第4题
np.random.seed(4)
data = np.random.randint(1, 100, 5)
labels = ["大米", "小麦", "玉米", "大豆", "小米"]
plt.pie(data, labels=labels, autopct="%1.1f%%")
plt.title("饼图显示物价比例")
plt.show()


# %% 第5题
x = np.arange(1, 11)
y1 = x
y2 = x + 1
y3 = x + 2
plt.plot(x, y1, "k--")
plt.plot(x, y2, "g-.")
plt.plot(x, y3, "b:")
plt.title("多线图颜色与线条管理")
plt.show()
