
import numpy as np

c1 = 1
c2 = 100

x = [3, 5, 6, 8]
y = [2, 5 ,8 ,1]

x = np.array(x)
y = np.array(y)
def rhu_y(x,y):#Критерий нашей проверки (7) в статье 02,04,2023
    rhu_y = max(abs(x - y))
    return rhu_y

print(rhu_y(x,y))


def rhu_x(x,y):#Критерий нашей проверки (7) в статье 02,04,2023
    rhu_x = 2 * max((abs(x - y)) / (c2 - c1)) # c2 - c1 максимальная и минимальная возможная цена
    return rhu_x

print(rhu_x(x,y))


# p - точка которую мы находим
# n - колличество итераций
# y - бюджет( задаем сами )
# a - критерии модели, прописываем вручную
# b - критерии модели, прописываем вручную

p = 100
n = 10
y = 10000
a = 1000
b = 1
def summ_Di(y, p):
    result = 0
    for number in range(n-1):
        result = result + (y * p)
        return result

print(summ_Di(y,p))
def Di(p):
    Di = 1 / (n * p) * summ_Di(y, p) # А. В. Арутюнов, Н. Г. Павлова, А. А. Шананин 11 стр
    return Di
print(Di(p))

def summ_Si(p):
    result = 0
    for number in range(n - 1):
        result = result + (p ** 2)
        return result
print(summ_Si(p))
def Si(p):
    Si = (((a + (b ** 2)) * p)/(b * ((a**2 + b**2)**0.5))) * (summ_Si(p)**(-1/2)) - 1/n**0.5 # А. В. Арутюнов, Н. Г. Павлова, А. А. Шананин 11 стр
    return Si
print(Si(p))


# поправить формулы с учетом сумм, посмотреть на формулу





