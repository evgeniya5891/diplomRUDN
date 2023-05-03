import numpy as np

c1 = [3, 5, 6, 8] # n мерные вектора можно поменять цифры
c2 = [2, 9 ,8 ,1]

c1 = np.array(c1)
c2 = np.array(c2)

x = [3, 5, 6, 8]
y = [2, 5 ,8 ,1]

x = np.array(x)
y = np.array(y)


p = [3, 5, 6, 8] #вектор
n = 10
# m <= n m - длинна векторов D и S
gamma = [3, 5, 6, 8] #гамма вектор переименовать
a = 1000 # не нашли описание
b = 1

p = np.array(p)
gamma = np.array(gamma)
def rhu_y(x,y):#Критерий нашей проверки (7) в статье 02,04,2023
    rhu_y = max(abs(x - y))
    return rhu_y

print(rhu_y(x,y))


def rhu_x(x,y):#Критерий нашей проверки (7) в статье 02,04,2023
    rhu_x = 2 * max(abs(x - y))/(c2 - c1) # c2 - c1 максимальная и минимальная возможная цена
    return rhu_x

print(rhu_x(x,y))


# p - точка которую мы находим, цены на товары если товаров n то P n мерный вектор
# n - колличество итераций
# gamma - бюджет( задаем сами )
# a - критерии модели, прописываем вручную
# b - критерии модели, прописываем вручную


#  Ди и си могут вернуть м мерный векторн рассмотреть случаи где м = н и м<н нашли равновесие на часть товаров


def summ_Di(gamma, p):
    result = 0
    for number in range(n):
        result = np.array(result)
        result = result + (gamma * p)
    return result
print(summ_Di(gamma,p))

def Di(p):# должен получиться вектор  мерный
    Di = 1 / (n * p) * summ_Di(gamma, p) # А. В. Арутюнов, Н. Г. Павлова, А. А. Шананин 11 стр
    return Di
print(Di(p))

def summ_Si(p):# должен получиться вектор н мерный
    result2 = 0
    for number in range(n):
        result2 = np.array(result2)
        result2 = result2 + p**2
    return result2
print(summ_Si(p))

def Si(p):
    Si = (((a + (b ** 2)) * p)/(b * ((a**2 + b**2)**0.5))) * (summ_Si(p)**(-1/2)) - 1/n**0.5 # А. В. Арутюнов, Н. Г. Павлова, А. А. Шананин 11 стр
    return Si
print(Si(p))

# проверить утверждение 11 и 12 . В. Арутюнов, Н. Г. Павлова, А. А. Шананин 11 , 12 стр
# найти пару примеров удовлетворяющие этим условиям и проверить их
# варировать одно из переменных и посмотреть как это влияет на точку рановесия сделать выводу


def summ_check_c2():
    result3 = 0
    for number in range(n):
        result3 = np.array(result3)
        result3 = result3 + gamma * c2
    return result3

def summ_check_c1():
    result4 = 0
    for number in range(n):
        result4 = np.array(result4)
        result4 = result4 + gamma * c1
    return result4



def check_app():
    if n + 1 / 2*b**2 * min((c2 - c1)/c1) < 2*n*((max(c1*((c2 - c1)**-1)*c2*(summ_check_c2())))**-1) * max(c1 / (c2 - c1)) * summ_check1() * summ_check2() - ((n+1)/n*(max(c2)*max(c1)**-2)*(max(c1/(c2-c1)))**-1 * summ_check_c1()
        print('проверка прошла')




