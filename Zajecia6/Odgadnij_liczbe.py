from random import randint

while True:
	print('Podaj zakres')
	c=input()
	if c.isalpha():
		print('Podaj liczbe, a nie litere ;)')
		continue
	else:
		c=int(c)
		break
	
r=randint(0,c)

while True:
	print ('Podaj liczbe prob: ')
	a=input()
	if a.isalpha():
		print('Podaj liczbe, a nie litere ;)')
		continue
	else:
		a=int(a)
		break
		

def graj(a):
	while a!=0:
		print('Podaj liczbe: ')
		b=input()
		if b.isalpha():
			print('Podaj liczbe, a nie litere ;)')
			continue
		else:
			b=int(b)
		if r==b:
			print('Wygrales! :)')
			break
		else:
			a-=1
			if a==0:
				print('Przegrales! :(')
			else:
				print('Sprobuj jeszce raz')
				print('Pozostale proby: ',a)



graj(a)

