print ('\n **** Zaczynamy grę!! **** \n')

pytania = {'Jak ma na imię autor tej gry?': 'tomek',
           'Jak nazywa sie język programowania, którego się uczymy?': 'python',
           'Która funkcja umożliwia wprowadzenie tekstu przez użytkownika (odpowiedz nie uwzględnia nawiasów)?': 'input',
           'Jaki typ zmiennej będzie miała tak wprowadzona zmienna: a=12.3?': 'double',
           'Jaki typ zmiennej będzie miała tak wpisana zmienna: a="6" ':'string',
           'Czy możemy dodać do siebie zmienną typu string i zmienną typu float?': 'nie',
           'Która funkcja pozwala nam na wygenerowanie randomowych liczb (odpowiedz nie uwzględnia nawiasów)?': 'randint',
           'Z której biblioteki importujemy funkcję randint?' : 'random',
           'Czy dzielenie bez reszty jest wykonywane za pomocą operatora % ?': 'tak',
           'Czy operator ** daje nam możliwość podniesienia liczby do dowolnej potęgi? ': 'tak'
           }



def zagadki(pytania):
    score=0
    for p,o in pytania.items():
        print (p)
        user_input=input()
        user_input=user_input.lower()
        if user_input==o:
            print('Poprawna odpowiedź! \n')
            score+=1
        else:
            print('Błędna odpowiedź! \n')
    proc=float(score/len(pytania)*100)
    print ('Ilość poprawnych odpowiedzi to:', score)
    print ('Procent poprawnych odpowiedzi to:', proc,'%' )
    return score

zagadki(pytania)

