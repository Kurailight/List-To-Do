import sys
import json
from datetime import datetime, timedelta

class Zadania:
    def __init__(self):
        self.slownik= {}
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    def menu(self):
        print(f'''  1- dodaj zadanie
                    2- skasuj zadania
                    3- wyświetl zadania
                    4- dodaj niestandardowo zadanie
                    0- zakończ program''') 
        
    def save_tasks(self):
        try:
            json_string = json.dumps(self.slownik)
            with open('C:/Users/marta/OneDrive/Pulpit/python_kurs/listatodo', 'w') as f:
                f.write(json_string)
        except Exception as e:
            print("Wystąpił błąd podczas zapisywania pliku:", e)

    def dodaj_zadanie(self, zadanie):
        if self.slownik:  
            indeks = max(map(int, self.slownik.keys())) + 1
        else:
            indeks = 1 
        self.slownik[str(indeks)] = [zadanie, self.now]
        self.save_tasks()

    def niestandardowe(self, m, n):
        self.slownik[str(m)] = [n, self.now]
        self.save_tasks()

    def skasuj(self, zad):
        if str(zad) in self.slownik:  
            del self.slownik[str(zad)]
            self.save_tasks() 
        else:
            print("Nie ma zadania o podanym numerze.")
           