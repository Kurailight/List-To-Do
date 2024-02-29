import sys
import json
from datetime import datetime, timedelta
import lista_to_do_modul

zadanie= lista_to_do_modul.Zadania()
zadanie.menu()
while True:
    a= int(input("Podaj cyfrę "))
    if a==1:
        a1= input("Dodaj zadanie: ")
        zadanie.dodaj_zadanie(a1)
    elif a==2:
        a2= input("Skasuj zadanie: ")
        zadanie.skasuj(a2)
    elif a == 3:
        with open('C:/Users/marta/OneDrive/Pulpit/python_kurs/listatodo', 'r') as f:
            json_string = f.read()
            zadanie.slownik = json.loads(json_string)
        print(zadanie.slownik)

    elif a==4:
        m= input("Podaj numer zadania: ")
        n= input("Podaj treść zadania: ")
        zadanie.niestandardowe(m, n)
    elif a==0: 
        sys.exit()