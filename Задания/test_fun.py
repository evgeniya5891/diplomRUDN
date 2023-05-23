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


n = 10
c1 = np.zeros(n)
c2 = np.ones(n)
a = 0.5
alpha = 0.75
beta = 0.5
delta = 1.0 - beta / alpha
eps = 0.0001

# Declare the necessary variables
x0 = np.zeros(n)
xk = x0
xknext = np.zeros(n)
directions = np.zeros(n)
h = np.zeros(n)
z = np.zeros(n)
mindist = rhu_y(D(xk) + a, S(xk))
distance = rhu_y(D(xk) + a, S(xk))

itercount = 0

while rhu_y(D(xk) + a, S(xk)) > eps:
    toolong = 0
    itercount += 1
    found = False
    h = (c2 - c1) * (2 * alpha) ** (-1) * D(xk) + a, S(xk)

    while not found:
        toolong += 1
        z = np.random.rand(n)
        xknext = xk + h * (-1 + 2 * z)

        for j in range(n):
            if xknext[j] > c2[j]:
                xknext[j] = c2[j]
            if xknext[j] < c1[j]:
                xknext[j] = c1[j]

        print(f'{xknext}')

        if toolong == 100:
            print('too long.')
            break

        if rhu_y(D(xk) + a, S(xk)) <= delta * distance:
            distance = rho_y(Psi(xknext) + a, Phi(xknext))
            found = True
            delta = 1.0 - beta / alpha
            toolong = 0
            xk = xknext
        else:
            pass

    if not found:
        print('Fail.')
        print('Minimal distance found is:')
        print(f'{mindist:12.5f}')
        break
    else:
        print('New point:')
        print(f'{xk:20.8f}')
        print('The distance between the functions equals:')
        print(f'{rho_y(Psi(xk) + a, Phi(xk)):12.8f}')