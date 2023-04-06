x0 точка от который мы отталкиваемся для поиска пересечений 2х прямых

def overlappoints_random_search(x0):
    itercount = 0

    xk = x0

    directions = 0

#Переименовать Psi и Phi в D и S,  rho_y это метрика Рн, прописываем сами, она параждается нормой

    distance = rho_y(Psi(xk), Phi(xk))#rho_y функция? где это формула в статье. Критерий нашей проверки (7) в статье 02,04,2023

    while (rho_y(Psi(xk), Phi(xk)) > eps): #rho_y функция? где это формула в статье, сделать точку выхода
        toolong = 0 #для проверки и выводи из цыкла, что бы удалить
        itercount = itercount + 1
        found =.false. #что означает .false.

        h = (c2 - c1) * (2 * alpha) ** (-1) * rho_y(Psi(xk) + a, Phi(xk))#формула 4 из статьи от 02,04 определение радиуса поиска
        while (found.eqv..false.):#что означет .eqv..false.
            toolong = toolong + 1
            call random_number(z)#генерирует случайные числа
            xknext = xk + h * (-1 + 2 * z)
            for j in xk:
                if (xknext(j) > c2(j)):# c1 b c2 отграничение на цены
                    xknext(j)=c2(j)
                if (xknext(j) < c1(j)):
                    xknext(j) = c1(j)

            #if (toolong == 100) then

            #print *, 'too long.'

            # exit

        #endif   это условие выхода из цикла
            if ((rho_y(Psi(xknext), Phi(xk)) <= delta * distance)): Проверяем условие 7 из татьи

                distance = rho_y(Psi(xknext), Phi(xknext))

                found =.true. #Флажок поиска

                toolong = 0

                xk = xknext


    if (found.eqv..false.):

        print( *, 'Fail.')

        print( *, 'Minimal distance found is: ')

        write(*, '(f12.5)') mindist

    else:
        print( *, 'New point:')

        write(*, '(f20.8)') xk

        print( *, 'The distance between the functions equals:')

        write(*, '(f12.8)'), rho_y(Psi(xk) + a, Phi(xk))


    return
#пойтись по всем переменным


#Эти функции даты на странице 11 из 1 статьи и прописать S и D
