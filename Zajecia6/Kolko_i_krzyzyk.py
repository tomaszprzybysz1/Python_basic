from random import randint

tab = []

def rysuj_tabele():
    print(tab[0], '|', tab[1], '|', tab[2])
    print('---------')
    print(tab[3], '|', tab[4], '|', tab[5])
    print('---------')
    print(tab[6], '|', tab[7], '|', tab[8])

def sprawdz_wynik_x():
    if tab[0] == 'X' and tab[1] == 'X' and tab[2] == 'X':
        print('\n' + 'Gracz X wygrywa!')
        exit()
    elif tab[3] == 'X' and tab[4] == 'X' and tab[5] == 'X':
        print('\n' + 'Gracz X wygrywa!')
        exit()
    elif tab[6] == 'X' and tab[7] == 'X' and tab[8] == 'X':
        print('\n' + 'Gracz X wygrywa!')
        exit()
    elif tab[0] == 'X' and tab[3] == 'X' and tab[6] == 'X':
        print('\n' + 'Gracz X wygrywa!')
        exit()
    elif tab[1] == 'X' and tab[4] == 'X' and tab[7] == 'X':
        print('\n' + 'Gracz X wygrywa!')
        exit()
    elif tab[2] == 'X' and tab[5] == 'X' and tab[8] == 'X':
        print('\n' + 'Gracz X wygrywa!')
        exit()
    elif tab[0] == 'X' and tab[4] == 'X' and tab[8] == 'X':
        print('\n'+'Gracz X wygrywa!')
        exit()
    elif tab[2] == 'X' and tab[4] == 'X' and tab[6] == 'X':
        print('\n'+'Gracz X wygrywa!')
        exit()

def sprawdz_wynik_o():
    if tab[0] == 'O' and tab[1] == 'O' and tab[2] == 'O':
        print('\n'+'Gracz Y wygrywa!')
        exit()
    elif tab[3] == 'O' and tab[4] == 'O' and tab[5] == 'O':
        print('\n' + 'Gracz Y wygrywa!')
        exit()
    elif tab[6] == 'O' and tab[7] == 'O' and tab[8] == 'O':
        print('\n' + 'Gracz Y wygrywa!')
        exit()
    elif tab[0] == 'O' and tab[3] == 'O' and tab[6] == 'O':
        print('\n' + 'Gracz Y wygrywa!')
        exit()
    elif tab[1] == 'O' and tab[4] == 'O' and tab[7] == 'O':
        print('\n' + 'Gracz Y wygrywa!')
        exit()
    elif tab[2] == 'O' and tab[5] == 'O' and tab[8] == 'O':
        print('\n' + 'Gracz Y wygrywa!')
        exit()
    elif tab[0] == 'O' and tab[4] == 'O' and tab[8] == 'O':
        print('\n' + 'Gracz Y wygrywa!')
        exit()
    elif tab[2] == 'O' and tab[4] == 'O' and tab[6] == 'O':
        print('\n' + 'Gracz Y wygrywa!')
        exit()

def graj_x():
    while True:
        print('Graczy X: Podaj nr pola z zakresu [1-9]:')
        a = input()
        if a.isalpha():
            print('Cyfre, nie litere :)')
            continue
        elif a=='':
            continue
        else:
            a = int(a)
        if a < 1 or a > 9:
            print('Nie ma takiego pola')
            continue
        else:
            if tab[a - 1] != '?':
                print('Pole jest już zajete!')
                continue
            else:
                tab[a - 1] = 'X'
                rysuj_tabele()
                sprawdz_wynik_x()
                break

def graj_y():
    while True:
        print('Gracz Y: Podaj nr pola z zakresu [1-9]:')
        a = input()
        if a.isalpha():
            print('Cyfre, nie litere :)')
            continue
        elif a=='':
            continue
        else:
            a = int(a)
        if a < 1 or a > 9:
            print('Nie ma takiego numeru pola')
            continue
        else:
            if tab[a - 1] != '?':
                print('Pole jest juz zajete!')
                continue
            else:
                tab[a - 1] = 'O'
                rysuj_tabele()
                sprawdz_wynik_o()
                break

def sprawdz_ruch():
    if '?' not in tab:
        print('\n' + 'Remis!' + '\n' + 'Koniec! :) ')
        exit()

def graj_komputer():
    while True:
        a = randint(0, 8)
        if tab[a] != '?':
            continue
        else:
            tab[a] = 'O'
            print('\n'+ 'Ruch komputera:' + '\n')
            rysuj_tabele()
            sprawdz_wynik_o()
            break

def liczba_graczy():
    while True:
        print('Ilu graczy?')
        a = input()
        if a.isalpha():
            print('Cyfre, nie litere :)')
            continue
        elif a=='':
            continue
        else:
            a = int(a)
        if a > 2:
            print('Maksymalnie dwoch graczy!')
            continue
        elif a<1:
            print('Minimalnie jeden gracz!')
            continue
        elif a == 2:
            while True:
                graj_x()
                sprawdz_ruch()
                graj_y()
                sprawdz_ruch()
        else:
            while True:
                graj_x()
                sprawdz_ruch()
                graj_komputer()
                sprawdz_ruch()

for item in range(0, 9):
    tab.append('?')

liczba_graczy()