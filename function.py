import numpy as np

x = [3, 5, 6, 8]
y = [2, 5 ,8 ,1]

x = np.array(x)
y = np.array(y)
def rhu_y(x,y):#Критерий нашей проверки (7) в статье 02,04,2023
    rhu_y = max(abs(x - y))
    return rhu_y


rhu_y = max(abs(x - y))
print(rhu_y)


