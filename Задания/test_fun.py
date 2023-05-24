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
x0 =list(x)
y = [2, 5]
alpha = 1#какое должно быть?

x = np.array(x)
y = np.array(y)
p = np.array(p)
c1 = np.array(c1)
c2 = np.array(c2)
gamma = np.array(gamma)

def D(p):# должен получиться вектор N мерный
    d = 1 / (n * p) * np.dot(gamma,p)
    return d
#print(D(p))

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


import numpy as np

import random


def overlappoints_random_search(x0):
    global delta

    n = len(x0)
    xk = np.array(x0, dtype=np.float64)
    directions = np.zeros(n, dtype=np.float64)

    mindist = rhu_y(D(xk) + a, S(xk))
    distance = rhu_y(D(xk) + a, S(xk))

    itercount = 0

    print('delta = ', delta)

    while rhu_y(D(xk) + a, S(xk)) > eps:
        toolong = 0
        itercount += 1
        print('---------')
        print('Starting iteration # ', itercount)
        print('Current distance between the functions is:')
        print('{:.8f}'.format(rhu_y(D(xk) + a, S(xk))))
        found = False
        h = (c2 - c1) * ((2 * alpha) ** (-1)) * rhu_y(D(xk) + a, S(xk))
        print('Current seek radius is:')
        print('{:.8f} {:.8f}'.format(h))
        print('On this step, the condition is:')
        print('{:.8f}'.format(delta * rhu_y(D(xk) + a, S(xk))))

        while not found:
            toolong += 1
            z = np.random.random(n)
            xknext = xk + h * (-1 + 2 * z)
            xknext = np.clip(xknext, c1, c2)
            print(xknext)

            if toolong == 100:
                print('Too long.')
                return

            if rhu_y(D(xknext) + a, S(xk)) <= delta * distance:
                distance = rhu_y(D(xknext) + a, S(xknext))
                found = True
                print('%%%%%%%%%%%%%%%%%%%%%%%')
                print('Found!')
                print('xknext: {:.5f} {:.5f}'.format(xknext[0], xknext[1]))
                delta = 1.0 - beta / alpha
                print('toolong:', toolong)
                toolong = 0
                print('The condition satisfied with distance:')
                print('{:.8f}'.format(rhu_y(D(xknext) + a, S(xk))))
                print('New distance between the functions:')
                print('{:.8f}'.format(distance))
                xk = xknext
            else:
                pass  # R = R + rho_x(xknext,xk)

        if not found:
            print('Fail.')
            print('Minimal distance found is: {:.5f}'.format(mindist))
            return
        else:
            print('New point: {:.8f} {:.8f}'.format(xk[0], xk[1]))
            print('The distance between the functions equals: {:.8f}'.format(rhu_y(D(xk) + a, S(xk))))

    print('')
    print('--------------------------------')
    print('')
    print('Coincidence point: {:.8f} {:.8f}'.format(xknext[0], xknext[1]))
    print('The distance between the functions equals: {:.8f}'.format(rhu_y(D(xknext) + a, S(xknext))))
    print('This was made in {} steps.'.format(itercount))
    print('')
    print('')
    print('')
    print('Solution is', xknext)
    print('')
    print('')
    print('')
    print('The approx distance: {:.8f}'.format(rhu_y(D(xknext) + a, S(xknext))))

    return
print(overlappoints_random_search(x0))