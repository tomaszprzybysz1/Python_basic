def kalkulator(a,b):
    print('Podaj znak dzialania, które chcesz wykonać: ')
    x=input()
    c=0
    if x=='+':
        c=a+b
        print (c)
        return c
    elif x=='-':
        c=a-b
        print(c)
        return c
    elif x=='*':
        c=a*b
        print(c)
        return c
    elif x=='/':
        if b==0:
            print('Nie dzielimy przez 0')
        else:
            c=a/b
            print(c)
            return c
    else:
        print('Nie rozpoznano znaku działania')

print('Podaj pierwszą liczbę: ')
a=float(input())
print('Podaj drugą liczbę: ')
b=float(input())
kalkulator(a,b)
