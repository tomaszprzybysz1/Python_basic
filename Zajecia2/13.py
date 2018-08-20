lista={'Jablko': 'to-delete',
       'Marchew': 'add',
       'Ogorek':'to-delete',
       'Banan':'remove',
       'Cytryna':'apply',
       'Rzodkiew':'to-delete'}
word=' '
for item in lista:
    if lista[item]=='to-delete':
      word = word + " " + item
print (word)