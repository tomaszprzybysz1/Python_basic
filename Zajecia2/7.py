from random import randint

def tupla():
    tuplaa=[]
    tab=[]
    for i in range (1,11):
        y=randint(0,50)
        tuplaa.append(y)
    print(tuplaa)
    print('Najwieksza wartosc to: ', max(tuplaa))
    print('Najmniejsza wartosc to: ', min(tuplaa))


tupla()