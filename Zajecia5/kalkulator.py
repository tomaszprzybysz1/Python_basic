def kalkulator(*args):
    tab = []
    print('Podaj znak dzialania, które chcesz wykonać: ')
    x=input()
    print('Podaj pierwszą liczbę')
    a = input()

    while a.isalpha():
        print('Podaj liczbę, nie literę')
        a = input()

    a=float(a)

    print('Podaj kolejne liczby: ')
    while True:
        k = input()
        if k.isdigit():
            tab.append(k)
        elif k.isalpha():
            print('Podaj liczbę, nie literę: ')
        else:
            break

    if x=='+':
        for item in tab:
          a+=float(item)
        print('Wynik to', a)
        return a
    elif x=='-':
        for item in tab:
            a-=float(item)
        print('Wynik to',a)
        return a
    elif x=='*':
        for item in tab:
            a*=float(item)
        print('Wynik to', a)
        return a
    elif x=='/':
        if '0' in tab:
            print('Nie dzielimy przez 0')
        else:
            for item in tab:
                a/=float(item)
            print('Wynik to', a)
            return a
    else:
        print('Nie rozpoznano znaku działania')

kalkulator()

