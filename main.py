import numpy as np
import matplotlib.pyplot as plt
from pyscript import display  # 导入pyscript的display函数

# 绘制图形代码
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)

# 获取当前的图形对象
fig = plt.gcf()

# 使用display函数将图形渲染到指定的HTML元素中
display(fig, target="my-plot")
