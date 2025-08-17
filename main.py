import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

# 绘制图形代码
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)

