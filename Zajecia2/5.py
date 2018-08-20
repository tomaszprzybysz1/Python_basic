from random import randint

def sortowanie(a,b):
  tab=[]
  for i in range (1,7):
      y=randint(a,b)
      tab.append(y)
  print (sorted(tab))

print('Podaj zakres, z którego mam losować liczby! \n ')
print('Początek zakresu: ')
a=int(input())
print('Koniec zakresu: ')
b=int(input())

sortowanie(a,b)
