# p - точка которую мы находим
# n - колличество итераций
# y - бюджет( задаем сами )
# a - критерии модели, прописываем вручную
# b - критерии модели, прописываем вручную

import numpy as np

c1 = [1, 1]
c2 = [5, 5]
n = 2
gamma = [0.01 , 0.01]
a = 1
b = 1
p = [3, 5]
x = [3, 5]
y = [2, 5]
alpha = 1#какое должно быть?
eps = 0.00001 #какое должно быть?
delta = 1#какое должно быть?
x0 = [1, 2] #каким должен быть?
beta = 1#каким должен быть?
xk = x0

xk = np.array(xk)
x0 = np.array(x0)
x = np.array(x)
y = np.array(y)
p = np.array(p)
c1 = np.array(c1)
c2 = np.array(c2)
gamma = np.array(gamma)



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
    mindist = rhu_y(D(xk) + a, S(xk))
    distance = rhu_y(D(xk) + a, S(xk))
    itercount = 0

    while rhu_y(D(xk) + a, S(xk)) > eps:
        toolong = 0
        itercount += 1
        print('Starting iteration # ', itercount)
        print('Current distance between the functions is:', rhu_y(D(xk) + a, S(xk)))

        found = False
        h = (c2 - c1) * (2 * alpha) ** (-1) * rhu_y(D(xk) + a, S(xk))
        print('Current seek radius is:', h)
        print('On this step, the condition is:', delta * rhu_y(D(xk) + a, S(xk)), delta * rhu_y(D(xk) + a, S(xk)))

        while found == False:

            toolong += 1

            z = np.random.rand(len(x0))
            xknext = xk + h * (-1 + 2 * z)

            for j in range(len(x0)):
                if xknext[j] > c2[j]:
                    xknext[j] = c2[j]
                if xknext[j] < c1[j]:
                    xknext[j] = c1[j]

            print(xknext)

            if toolong == 100:
                print('too long.')
                break
            delta = 1.0 - beta / alpha

            if (rhu_y(D(xknext) + a, S(xk)) <= delta * distance):

                distance = rhu_y(D(xknext) + a, S(xknext))
                found = True
                print('Found!',xknext)

                delta = 1.0 - beta / alpha

                print('toolong: ', toolong)
                toolong = 0
                print('The condition satisfied with distance:', rhu_y(D(xknext) + a, S(xk)))
                print('New distance between the functions:', distance)
                xk = xknext
                print('xknext:', xknext)

            else:

                pass

        if not found:
            print('Minimal distance found is: ', mindist)
            return
        else:
            print('New point:',xk)
            print('The distance between the functions equals:',rhu_y(D(xk) + a, S(xk)))

    print('Coincidence point:', xknext)
    print('The distance between the functions equals:', rhu_y(D(xknext) + a, S(xknext)))
    print('This was made in ', itercount, ' steps.')
    print('Solution is', xknext)
    print('The approx distance: ', rhu_y(D(xknext) + a, S(xknext)))

    return

Overlappoints_random_search(x0)