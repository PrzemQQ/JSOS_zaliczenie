from main import *
from tkinter import *

#pobieranie listy osób i ocen z pliku głównego
studenci = Student.lista_studentow
print(studenci)
przedmioty = [Student.przedmiot1,Student.przedmiot2,Student.przedmiot3]
oceny = [Student.oceny_p1]
glowna_lista = [("Lp.","Dane personalne",przedmioty[0],przedmioty[1],przedmioty[2])]
lista_obiektow = Student.pomocznicza_lista_studentow
#iteruję liste
for i in range(len(studenci)):
    obiektowa_nazwa = lista_obiektow[i]

    if i ==0:
        tupla = (1,studenci[i],jan_kowalski.oceny_p1,jan_kowalski.oceny_p2,jan_kowalski.oceny_p3)
    elif i ==1:
        tupla = (i+1,studenci[i],anna_nowak.oceny_p1,anna_nowak.oceny_p2,anna_nowak.oceny_p3)
    elif i ==2:
        tupla = (i+1,studenci[i],joanna_mucha.oceny_p1,joanna_mucha.oceny_p2,joanna_mucha.oceny_p3)
    glowna_lista.append(tupla)



root = Tk()
root.title("Oceny studentów")
root.geometry("1366x768")
root.config(background="#123456")


liczba_wierszy = len(glowna_lista)
liczba_kol = len(glowna_lista[0])
for i in range(liczba_wierszy):
    for j in range(liczba_kol):
        table = Entry(
            root,
            width=20,
            font = ('Arial',20)
        )
        table.grid(row = i, column = j)
        table.insert(0,glowna_lista[i][j])
root.mainloop()