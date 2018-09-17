def moja(*args,glue=':'):
    tab=[]
    tab2=[]
    print('Wpisz string:')

    while True:
        k = input()
        if k:
          tab.append(k)
        else:
            break

    for item in tab:
        if len(item)>3:
            tab2.append(item)

    print(glue.join(tab2))

moja()

