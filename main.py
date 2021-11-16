class Student:
    """[klasa zawiera informacje o studencie]
    """
    przedmiot1 = "analiza"
    przedmiot2 = "algebra"
    przedmiot3 = "fizyka"
    oceny_p1 = []
    oceny_p2 = []
    oceny_p3 = []
    lista_studentow = []
    pomocznicza_lista_studentow = []
    def __init__(self,imie,nazwisko,indeks) -> None:
        self.imie = imie
        self.nazwisko =nazwisko
        self.indeks = indeks
        self.oceny_p1 = []
        self.oceny_p2 = []
        self.oceny_p3 = []
        self.lista_studentow.append(f"{imie}, {nazwisko}, {indeks}")
        self.pomocznicza_lista_studentow.append(f"{imie.lower()}_{nazwisko.lower()}")
        
    def dodaj_ocene(self,przedmiot,ocena):
        """[Dodaje oceny do indeksu]

        Args:
            przedmiot ([type]): [string]
            ocena ([type]): [int]

        Returns:
            [type]: [zwraca informacje o dodaniu oceny i dodaje ocene do listy]
        """
        self.ocena = ocena
        self.przedmiot = przedmiot
        match przedmiot.lower():
            case self.przedmiot1:
                self.oceny_p1.append(ocena)
            case self.przedmiot2:
                self.oceny_p2.append(ocena)
            case self.przedmiot3:
                self.oceny_p3.append(ocena)
            case default:
                pass
        return f"Dodano ocenę {ocena} do przedmiotu {przedmiot}" 
    
    def wyswietl_oceny(self,przedmiot):
        """[wyswietla ocene]

        Args:
            przedmiot ([type]): [int]

        Returns:
            [list]: [wyswietla ocene z danego przedmiotu dla danego studenta]
        """
        match przedmiot.lower():
            case self.przedmiot1:
                return f"Oceny z {przedmiot.lower()}  dla ucznia {self.imie, self.nazwisko} =  {self.oceny_p1} "
            case self.przedmiot2:
                return f"Oceny z {przedmiot.lower()}  dla ucznia {self.imie, self.nazwisko} =  {self.oceny_p2} "
            case self.przedmiot3:
                return f"Oceny z {przedmiot.lower()}  dla ucznia {self.imie, self.nazwisko} =  {self.oceny_p3} "
            case default:
                pass
            
    def __str__(self,):
        return f"{self.imie} {self.nazwisko} oceny ucznia  \n analiza = {self.oceny_p1}  \n algebra = {self.oceny_p2}  \n fizyka = {self.oceny_p3} "
    
    def edytuj_ocene(self,przedmiot,pozycja_oceny,nowa_ocena):
        """[Edycja oceny dla poszczególnego przedmiotu]

        Args:
            przedmiot ([str]): [wybrany przedmiot ]
            pozycja_oceny ([int]): [pozycja oceny na liście od 0 do n = len(lista)]
            nowa_ocena ([int]): [Nowa ocena od 0 do 6]
        """
        self.przedmiot = przedmiot
        przedmiot = przedmiot.lower()
        self.pozycja_oceny = pozycja_oceny
        self.nowa_ocena = nowa_ocena
        match przedmiot:
            case self.przedmiot1:
                stara_ocena = self.oceny_p1[pozycja_oceny]
                self.oceny_p1[pozycja_oceny] = nowa_ocena
                print(f"zmieniono {stara_ocena} na {nowa_ocena} dla przedmiotu {przedmiot} ")
            case self.przedmiot2:
                stara_ocena = self.oceny_p2[pozycja_oceny]
                self.oceny_p2[pozycja_oceny] = nowa_ocena
                print(f"zmieniono {stara_ocena} na {nowa_ocena} dla przedmiotu {przedmiot} ")
            case self.przedmiot3:
                stara_ocena = self.oceny_p3[pozycja_oceny]
                self.oceny_p3[pozycja_oceny] = nowa_ocena
                print(f"zmieniono {stara_ocena} na {nowa_ocena} dla przedmiotu {przedmiot} ")
            case default:
                pass
#dodajemy studentów      
jan_kowalski = Student("Jan","Kowalski",266838)
anna_nowak = Student("Anna","Nowak",288564)
joanna_mucha = Student("Joanna","Mucha",234086)

#zaprezentowanie funckjonalnosci
if __name__ == '__main__':
    #test metod dla JK
    print(jan_kowalski.dodaj_ocene("analiza",5))
    print(jan_kowalski.dodaj_ocene("analiza",5.5))
    print(jan_kowalski.dodaj_ocene("analiza",3))
    print(jan_kowalski.dodaj_ocene("fizyka",4))
    print(jan_kowalski.dodaj_ocene("fizyka",5))
    print(jan_kowalski.dodaj_ocene("fizyka",2))
    #wyswietlanie wszystkich ocen JK
    print(jan_kowalski)
    #test metody wystwielenia dla poszczegolnego przedmiotu
    print(jan_kowalski.wyswietl_oceny("analiza"))
    
    #test metod dla AN
    print(anna_nowak.dodaj_ocene("algebra",1))
    print(anna_nowak.dodaj_ocene("algebra",2))
    print(anna_nowak.dodaj_ocene("algebra",3))
    print(anna_nowak.dodaj_ocene("analiza",5))
    print(anna_nowak.dodaj_ocene("analiza",6))
    print(anna_nowak.dodaj_ocene("analiza",7))
    #wyswietlanie wszystkich ocen AK
    print(anna_nowak)
    
    #test edycji 
    print(jan_kowalski.edytuj_ocene("analiza",0,2))
    print(jan_kowalski)
    
#dla 5-3gui.py  
else:
    jan_kowalski.dodaj_ocene("analiza",5)
    jan_kowalski.dodaj_ocene("analiza",5.5)
    jan_kowalski.dodaj_ocene("analiza",3)
    jan_kowalski.dodaj_ocene("fizyka",4)
    jan_kowalski.dodaj_ocene("fizyka",5)
    jan_kowalski.dodaj_ocene("fizyka",2)
    
    #test metody wystwielenia dla poszczegolnego przedmiotu
    jan_kowalski.wyswietl_oceny("analiza")
    
    #test metod dla AN
    anna_nowak.dodaj_ocene("algebra",1)
    anna_nowak.dodaj_ocene("algebra",2)
    anna_nowak.dodaj_ocene("algebra",3)
    anna_nowak.dodaj_ocene("analiza",5)
    anna_nowak.dodaj_ocene("analiza",6)
    anna_nowak.dodaj_ocene("analiza",2)
    
    #test edycji 
    jan_kowalski.edytuj_ocene("analiza",0,2)
    
    joanna_mucha.dodaj_ocene("analiza",5)
    joanna_mucha.dodaj_ocene("analiza",3)
    joanna_mucha.dodaj_ocene("analiza",2)