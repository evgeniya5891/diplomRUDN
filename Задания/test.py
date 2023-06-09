import numpy as np

c1 = [1, 1]
c2 = [2, 2]

c1 = np.array(c1)
c2 = np.array(c2)

n = 2

gamma = [1 , 1]
a = 1
b = 2

gamma = np.array(gamma)

def f1():
    list1 = []
    for number in range(0,n):
        a = (c2[number] -c1[number]) / c1[number]
        list1.append(a)
    list1 = np.array(list1)
    return list1
# print(f1())

def f2():
    list2 = []
    for number in range(0,n):
        a = c1[number] / (c2[number] -c1[number])
        list2.append(a)
    list2 = np.array(list2)
    return list2
# print(f2())

def f3():
    list2 = []
    for number in range(0,n):
        a = c1[number] * (c2[number] - c1[number])**float(-1) * c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2
# print(f3())

def f4():
    list2 = []
    for number in range(0,n):
        a = c1[number] + c2[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2
#print(f4())

def f5():
    list2 = []
    for number in range(0,n):
        a = c2[number] - c1[number]
        list2.append(a)
    list2 = np.array(list2)
    return list2
# print(f5())

def f6():
    result = 0
    for number in range(0,n):
        a = min(abs(gamma - ((n * c2)**float(-1) * np.dot(gamma,c1))))
        result = result + a
    return result
# print( f6())

def f7():
    a = (n + 1) / (2 * (b**2)) * min(f1())
    return a
print(f7())
def f8():
    a = (n + 1) / n * max(c2) * max(c1**float(-2)) * (max(f2()))**float(-1) * np.dot(gamma,c1)
    return a
print(f8())


def GAMMA():
    list2 = []
    for number in range(1,n+1):
        w = abs(((n*f4()[number-1])**float(-1) * np.dot(gamma,f4())) - ((((a + b**2) * f4()[number-1] )/ (b * (a**2 + b**2)**(1/2))) * (np.dot(f4(),f4()))**float(-1/2)) + n**float(-1/2))
        list2.append(w)
    list2 = np.array(list2)
    return max(list2)

print(GAMMA())

def ALFA():
    w =  2 * n * (max(f3() * np.dot(gamma,c2))**float(-1)) * max(f2()) * f6() * max(c1**2)*((np.dot(gamma,c2))**float(-2))
    return w

print(ALFA())

def BETA():
    a = f8() - f7()
    return a
print(BETA())

def condition():
    if GAMMA() < ALFA() - BETA() and f7() <  ALFA() - f8():
        return True #'модель удовлетворяет условиям'
    else:
        return False #'модель НЕ удовлетворяет условиям'
print(condition())

