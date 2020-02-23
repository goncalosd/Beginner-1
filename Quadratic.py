#   ---   QUADRATIC EQUATIONS   ---
#   Programmed by: Gonza


def main():
    print(''' - Quadratic Equation Solver -
''')
    print('''In the form ax^2 + bx + c = 0
''')
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    def quadratic():
        if ((b**2)-4.*a*c) < 0:
            print('Equation has got no zeros')
        else:
            x1 = round(float((-b+((b**2)-(4.*a*c))**(1/2.))/(2.*a)), 2)
            x2 = round(float((-b-((b**2)-(4.*a*c))**(1/2.))/(2.*a)), 2)
            print('x = ' + str(x1) + ' V ' + 'x = ' + str(x2))

    confirmation = int(input('''
    Equation is: ''' + str(a) + '''x^2 + ''' + str(b) + '''x + ''' + str(c) + ''' = 0

    Enter 1 if correct and 2 if incorrect: '''))

    if confirmation == 1:
        quadratic()
        repeat = int(input('''
        - Insert 1 to resolve another equation
        - Insert 2 to end program '''))
        if repeat == 1:
            main()
        elif repeat == 2:
            print('See you later!')
        else:
            print('Invalid selection')
            main()
    else:
        if confirmation == 2:
            print('''
            Lets try again!
            ''')
            main()
        elif confirmation != 1 and confirmation != 2:
            print('''
            Please make valid selection
            ''')
            main()


main()
