def pierwsze(x):
  print('Wypisuję liczby pierwsze z zakresu od 2 do', x )
  for num in range(2, x+1):
    for i in range(2,num):
      if (num % i) == 0:
        break
    else:
      print(num)

print('Podaj koniec zakresu: ')
y=int(input())
pierwsze(y)