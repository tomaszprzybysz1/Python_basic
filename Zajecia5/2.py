def moja(nazwa,flaga=True):
    if flaga==True:
        print(nazwa.upper())
    elif flaga==False:
        print(nazwa.lower())
    else:
        print('Nie rozpoznano flagi')


moja('tomek')