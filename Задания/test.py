import numpy as np

c1 = [3, 5] # n мерные вектора можно поменять цифры
c2 = [2, 9]

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


# p - точка которую мы находим, цены на товары если товаров n то P n мерный вектор
# n - колличество итераций
# gamma - бюджет( задаем сами )
# a - критерии модели, прописываем вручную
# b - критерии модели, прописываем вручную


#  Ди и си могут вернуть м мерный векторн рассмотреть случаи где м = н и м<н нашли равновесие на часть товаров


# def summ_Di(gamma, p):
#     result = 0
#     for number in range(n):
#         result = np.array(result)
#         result = result + (gamma * p)
#     return result
# print(summ_Di(gamma,p))

def f1():
    list1 = []
    for number in range(0,n):
        a = (c2[number] -c1[number]) / c1[number]
        list1.append(a)
    list1 = np.array(list1)
    return list1

def f2():
    list2 = []
    for number in range(0,n):
        a = c1[number] / (c2[number] -c1[number])
        list2.append(a)
    list2 = np.array(list2)
    return list2

def f3():
    list2 = []
    for number in range(0,n):
        a = c1[number] * (c2[number] - c1[number])**float(-1) * c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2



def f4():
    list2 = []
    for number in range(0,n):
        a = c1[number] + c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2


def f5():
    list2 = []
    for number in range(0,n):
        a = c1[number] - c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2

def f6():
    result = 0
    for number in range(0,n):
        a = min(abs(gamma[number]) - ((number + 1) * c2)**float(-1) * np.dot(gamma,c1))
        result = result + a
    return result


def BETA():
    a = (n + 1) / n * max(c2) * max(c1**float(-2)) * (max(f2()))**float(-1) * np.dot(gamma,c1) - (((n + 1) / 2*b**2) * min(f1()))
    return a
print(BETA())
