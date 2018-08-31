print('Podaj liczbe')
a=float(input())
try:
    if a%2==0:
        raise ValueError('Parzysta')
        
		
    elif a<0:
        raise TypeError('Mniejsza od 0')
        
    elif a>10:
        raise IndexError('Index ErroR')
        
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except IndexError as e:
    print(e)