#    ---   Temperature Converter   (Celsius, Farenheit, Kelvin)   ---
#    Programmed by: Gonza


def c_to_f():
    cf = float(input('Enter temperature in Celsius: '))
    f1 = round((cf*(9/5.))+32, 2)
    print(str(cf) + ' Celsius equals to ' + str(f1) + ' degrees Farenheit.')


def f_to_c():
    fc = float(input('Enter temperature in Farenheit: '))
    c1 = round((fc-32)*(5/9.), 2)
    print(str(fc) + ' Farenheit equals to ' + str(c1) + ' degrees Celcius.')


def c_to_k():
    ck = float(input('Enter temperature in Celcius: '))
    k1 = round(ck+273.15, 2)
    print(str(ck) + ' Celsius equals to ' + str(k1) + ' degrees Kelvin.')


def k_to_c():
    kc = float(input('Enter temperature in Kelvin: '))
    c2 = round(kc-273.15, 2)
    print(str(kc) + ' Kelvin equals to ' + str(c2) + ' degrees Celsius.')


def f_to_k():
    fk = float(input('Enter temperature in Farenheit: '))
    k2 = round((fk-32)*(5/9.)+273.15, 2)
    print(str(fk) + ' Farenheit equals to ' + str(k2) + ' degrees Kelvin.')


def k_to_f():
    kf = float(input('Enter temperature in Kelvin: '))
    f2 = round((kf-273.15)*(9/5.)+32, 2)
    print(str(kf) + ' Kelvin equals to ' + str(f2) + ' degrees Farenheit.')


print('  --  Temperature Converter  --  ')

a = int(input('''What unit do you want to convert?

    Select 1 for Celsius
    Select 2 for Farenheit
    Select 3 for Kelvin
    '''))

if a == 1:
    b = int(input('''What unit do you want to convert to?

    Select 1 for Farenheit
    Select 2 for Kelvin
    '''))
elif a == 2:
    b = int(input('''What unit do you want to convert to?

    Select 1 for Celsius
    Select 2 for Kelvin
    '''))
elif a == 3:
    b = int(input('''What unit do you want to convert to?

    Select 1 for Celsius
    Select 2 for Farenheit
    '''))
else:
    print('Please make valid selection.')

if a == 1 and b == 1:
    c_to_f()
elif a == 1 and b == 2:
    c_to_k()
elif a == 2 and b == 1:
    f_to_c()
elif a == 2 and b == 2:
    f_to_k()
elif a == 3 and b == 1:
    k_to_c()
elif a == 3 and b == 2:
    k_to_f()
