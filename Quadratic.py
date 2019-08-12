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
        x1 = float((-b+(b**2-4.*a*c)**(1/2.))/(2.*a))
        x2 = float((-b-(b**2-4.*a*c)**(1/2.))/(2.*a))
        print('x = ' + str(x1) + ' V ' + 'x = ' + str(x2))

    confirmation = input('''
    Equation is: ''' + str(a) + '''x^2 + ''' + str(b) + '''x + ''' + str(c) + ''' = 0

    Enter 1 if correct and 2 if incorrect: ''')

    while confirmation == 1:
        quadratic()
        break
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
