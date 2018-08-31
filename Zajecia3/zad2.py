lista=[1,2,3,4]
print('Podaj index')
	
try:
    my_index =int(input('Enter:'))
    print(lista[my_index])
except IndexError as c:
    print('Index nie istnieje: ',c)