tab = [['-', '-', ' '], [' ', '|', ' '], [' ', 'O', ' '], ['/', '|', '\ '], ['/', ' ', '\ ']]

haslo_czyste=[]
haslo_ukryte=[]
db_list=[]
i=15
a=0
b=0
password = 'lot'


def dwymtab():
    for k in range (0, 5):
        new = []
        for l in range (0, 3):
            new.append('*')
        db_list.append(new)
    return db_list

def sprawdz_wynik(letter,pas,haslo_ukryte,haslo_czyste,i):
    if letter==pas:
        print('Dobry jestes!', ''.join(haslo_czyste),'to poprawne haslo!')
        exit()
    elif haslo_ukryte==haslo_czyste:
        print('Ogadles!')
        print('Tak, hasło to rzeczywiscie', ''.join(haslo_ukryte).upper())
        exit()
    elif i==0:
        print('Przegrana!')
        print('Poprawne hasło to', ''.join(haslo_czyste))
    else:
        print('Haslo: ', ''.join(haslo_ukryte).upper())

def zamaskuj_haslo(haslo_ukryte):
    for item in range(0, len(pas)):
        haslo_ukryte.append('*')
    return haslo_ukryte

def wczytaj(password):
    for letter in pas:
        haslo_czyste.append(letter)
    return haslo_czyste

pas = password.lower()

wczytaj(password)

zamaskuj_haslo(haslo_ukryte)

print('Zaczynamy! Haslo to: ',''.join(haslo_ukryte))

dwymtab()

while i > 0:
    t=0
    j=0
    print('Podaj litere, ktora Twoim zdaniem znajduje sie w hasle. Jesli znasz haslo, wpisz je w calosci!')
    lett = input()
    letter=lett.lower()

    if letter in pas and lett!='':
        print('Brawo!')
        for t,j in enumerate(haslo_czyste):
            if j==letter:
                haslo_ukryte[t]=letter


    else:
        print('Takiej litery nie ma w hasle!')
        if b != 3:
            db_list[a][b] = tab[a][b]
            b+=1
            i-=1
        else:
            a+=1 #inkrementacja licznika tablicy, poniewaz kazda tablica ma tylko 3 elementy
            b=0
            db_list[a][b] = tab[a][b]
            b+=1
            i-=1

        for item in db_list:
            print(''.join(item))

    sprawdz_wynik(letter,pas,haslo_ukryte,haslo_czyste,i)