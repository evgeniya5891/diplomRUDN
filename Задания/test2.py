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

