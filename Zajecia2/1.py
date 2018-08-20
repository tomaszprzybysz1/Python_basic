def pole(a,b):
    if a==b:
        print('Jest to kwadrat!')
        c=a*b
        print('Pole wynosi', c)
    else:
        c=a*b
        print('Pole wynosi', c)
    return c

while True:
  print('Podaj a: ')
  a=input()
  if a.isalpha():
       print("Chyba cos nie tak")
       continue
  else:
      a=float(a)
      break

while True:
  print('Podaj b: ')
  b=input()
  if b.isalpha():
    print('Chyba cos nie tak')
    continue
  else:
      b=float(b)
      break


pole(a,b)