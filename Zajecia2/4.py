def bez_reszty(x):
    for i in range(2,x):
        if i%5==0:
            print (i)
print ('Podaj liczbe: ')
y=int(input())
bez_reszty(y)

