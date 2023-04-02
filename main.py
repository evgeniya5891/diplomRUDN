

def overlappoints_random_search(x0):
    itercount = 0

    xk = x0

    directions = 0

    mindist = rho_y(Psi(xk) + a, Phi(xk))#rho_y функция? где это формула в статье

    distance = rho_y(Psi(xk) + a, Phi(xk))#rho_y функция? где это формула в статье
    print('delta = ', delta)
    while (rho_y(Psi(xk) + a, Phi(xk)) > eps): #rho_y функция? где это формула в статье
        toolong = 0
        itercount = itercount + 1
        print('---------')

        print ('Starting iteration # ', itercount)

        print ('Current distance between the functions is:')
        write(*, '(f12.8)') rho_y(Psi(xk) + a, Phi(xk)) #что делает write

        found =.false. #что означает .false.

        h = (c2 - c1) * (2 * alpha) ** (-1) * rho_y(Psi(xk) + a, Phi(xk))#rho_y функция? где это формула в статье

        print( *, 'Current seek radius is:')

        write(*, '(2f12.8)') h #что делает write

        print( *, 'On this step, the condition is:')

        write(*, '(f20.8)')#что делает write
        delta * rho_y(Psi(xk) + a, Phi(xk))

        while (found.eqv..false.):#что означет .eqv..false.
            toolong = toolong + 1
            call random_number(z)#что делает call random_number(z)
            xknext = xk + h * (-1 + 2 * z)
            for j in xk:
                if (xknext(j) > c2(j)):# c1 b c2 фунции? Почему xknext?
                    xknext(j)=c2(j)
                if (xknext(j) < c1(j)):
                    xknext(j) = c1(j)
            write(132, '(3f12.4)') xknext
            #if (toolong == 100) then

            #print *, 'too long.'

            # exit

        #endif   это похоже на обычный принт для проверки ошибки
            if ((rho_y(Psi(xknext) + a, Phi(xk)) <= delta * distance)):

                distance = rho_y(Psi(xknext) + a, Phi(xknext))

                found =.true.

                print( *, '%%%%%%%%%%%%%%%%%%%%%%%')

                print( *, 'Found!')

                write(131, '(f12.5)') xknext

                delta = 1.0 - beta / alpha

                print( *, 'toolong: ', toolong)

                toolong = 0

                print( *, 'The condition satisfied with distance:')

                write(*, '(f12.8)'), rho_y(Psi(xknext) + a, Phi(xk))

                print( *, 'New distance between the functions:')

                write(*, '(f12.8)'), distance

                print( *, '%%%%%%%%%%%%%%%%%%%%%%%')

                xk = xknext

                print( *, 'xknext:')

                write(*, '(f12.8)') xknext

            else

                R = R + rho_x(xknext, xk)
    if (found.eqv..false.):

        print( *, 'Fail.')

        print( *, 'Minimal distance found is: ')

        write(*, '(f12.5)') mindist

    else:
        print( *, 'New point:')

        write(*, '(f20.8)') xk

        print( *, 'The distance between the functions equals:')

        write(*, '(f12.8)'), rho_y(Psi(xk) + a, Phi(xk))


    print( *, '')
    print( *, '--------------------------------')
    print( *, '')

    print( *, 'Coincidence point: ')

    write(*, '(f12.8)') xknext

    print( *, 'The distance between the functions equals:')

    write(*, '(f12.8)'), rho_y(Psi(xknext) + a, Phi(xknext))

    print( *, 'This was made in ', itercount, ' steps.')

    print( *, '')
    print( *, '')
    print( *, '')
    print( *, 'Solution is', xknext)
    print( *, '')
    print( *, '')
    print( *, '')
    write(100, '(f12.8,1x)') rho_y(Psi(xknext) + a, Phi(xknext))
    write(110, '(f20.8,1x)') xknext

    xk = 165.108680209104 #почему это число?

    write(*, '(1a,f12.8)') 'The approx distance: ', rho_y(Psi(xk) + a, Phi(xk))

    return
#пойтись по всем переменным
