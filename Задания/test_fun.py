# p - точка которую мы находим
# n - колличество итераций
# y - бюджет( задаем сами )
# a - критерии модели, прописываем вручную
# b - критерии модели, прописываем вручную
# убрать все +а

import numpy as np

c1 = [7.08216914, 2.9375804]
c2 = [0.37248224, 2.90394144]
n = 2
gamma = 0.4616454589321557
a = 1
b = 1
p = [3, 5]
x = [3, 5]
y = [2, 5]
alpha = 29.59935772273932
beta = -1.0866962164006442
eps = 0.001
delta = delta = 1.0 - beta / alpha#какое должно быть?из статьи арутюнова 1 -





x = np.array(x)
y = np.array(y)
p = np.array(p)
c1 = np.array(c1)
c2 = np.array(c2)
gamma = np.array(gamma)

x0 = (c1 + c2)/2
xk = x0
xk = np.array(xk)
x0 = np.array(x0)

def D(p):# должен получиться вектор N мерный
    d = 1 / (n * p) * np.dot(gamma,p)
    return d
# print(D(p))

def S(p):
    S= (((a + (b ** 2)) * p)/(b * ((a**2 + b**2)**0.5))) * (np.dot(2,p)**(-1/2)) - 1/n**0.5 # А. В. Арутюнов, Н. Г. Павлова, А. А. Шананин 11 стр
    return S
#print(S(p))

def rhu_y(x,y):#Критерий нашей проверки (7) в статье 02,04,2023
    rhu_y = max(abs(x - y))
    return rhu_y

#print(rhu_y(x,y))


def rhu_x(x,y):#Критерий нашей проверки (7) в статье 02,04,2023
    rhu_x = 2 * max(abs(x - y))/(c2 - c1) # c2 - c1 максимальная и минимальная возможная цена
    return rhu_x

#print(rhu_x(x,y))

xk = x0

def Overlappoints_random_search(x0):
    delta = 1.0 - beta / alpha
    xk = x0
    directions = np.zeros(len(x0))
    mindist = rhu_y(D(xk), S(xk))
    distance = rhu_y(D(xk), S(xk))
    itercount = 0
    toolong = 0

    while rhu_y(D(xk), S(xk)) > eps:
        itercount += 1
        print('Начальная итерация # ', itercount)
        print('Текущее расстояние между функциями равно:', rhu_y(D(xk), S(xk)))

        found = False
        h = (c2 - c1) * (2 * alpha) ** (-1) * rhu_y(D(xk), S(xk))
        print('Текущий радиус поиска равен:', h)# радиус поиска
        print('На этом шаге условие таково:', delta * rhu_y(D(xk), S(xk)), delta * rhu_y(D(xk), S(xk)))

        while found == False:

            toolong += 1

            z = np.random.rand(len(x0))
            xknext = xk + h * (-1 + 2 * z)

            for j in range(len(x0)):
                if xknext[j] > c2[j]:
                    xknext[j] = c2[j]
                if xknext[j] < c1[j]:
                    xknext[j] = c1[j]# исменить код

            print(xknext)

            if toolong == 100:#vj;yj gjvtyznm yf 100000
                print(toolong)
                break


            if (rhu_y(D(xknext), S(xk)) <= delta * distance):

                distance = rhu_y(D(xknext), S(xknext))
                found = True
                print('Найден!',xknext)

                delta = 1.0 - beta / alpha

                print('toolong: ', toolong)
                print('Условие, удовлетворяемое расстоянием:', rhu_y(D(xknext), S(xk)))
                print('Новое расстояние между функциями:', distance)
                xk = xknext
                print('xknext:', xknext)

            else:

                pass

        if not found:
            print('Минимальное найденное расстояние равно: ', mindist)
            return
        else:
            print('Новая точка:',xk)
            print('Расстояние между функциями равно:',rhu_y(D(xk), S(xk)))

    print('Точка совпадения:', xknext)
    print('Расстояние между функциями равно:', rhu_y(D(xknext), S(xknext)))
    print('Это было сделано в ', itercount, ' шагах.')
    print('Решение', xknext)
    print('Приблизительное расстояние: ', rhu_y(D(xknext), S(xknext)))

    return

Overlappoints_random_search(x0)