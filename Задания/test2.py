import numpy as np

c1 = [3, 5] # n мерные вектора можно поменять цифры
c2 = [4, 9]

c1 = np.array(c1)
c2 = np.array(c2)

x = [3, 5]
y = [2, 5]

x = np.array(x)
y = np.array(y)


p = [3, 5] #вектор
n = 2
# m <= n m - длинна векторов D и S
gamma = [3, 5] #гамма вектор переименовать
a = 1000 # не нашли описание
b = 1

p = np.array(p)
gamma = np.array(gamma)


def f1():
    list1 = []
    for number in range(0,n):
        a = (c2[number] -c1[number]) / c1[number]
        list1.append(a)
    list1 = np.array(list1)
    return list1
print(f1())

def f2():
    list2 = []
    for number in range(0,n):
        a = c1[number] / (c2[number] -c1[number])
        list2.append(a)
    list2 = np.array(list2)
    return list2
print(f2())

def f3():
    list2 = []
    for number in range(0,n):
        a = c1[number] * (c2[number] - c1[number])**float(-1) * c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2
print(f3())

def f4():
    list2 = []
    for number in range(0,n):
        a = c1[number] + c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2
print(f4())

def f5():
    list2 = []
    for number in range(0,n):
        a = c1[number] - c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2
print(f5())



def GAMMA():
    list2 = []
    for number in range(0,n):
        a = abs((n*(f4())**(-1/1)) * np.dot(gamma,f3())[number]) - ((a + b**2)*f3()[number]) / b * (a**2 + b**2)**1/2 * ((f4()**2)[number])**-1/2
        list2.append(a)
    list2 = np.array(list2)
    return max(list2)
print(GAMMA())



