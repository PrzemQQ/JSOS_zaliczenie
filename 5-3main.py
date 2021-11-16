class Student:
    """[klasa zawiera informacje o studencie]
    """
    przedmiot1 = "analiza"
    przedmiot2 = "algebra"
    przedmiot3 = "fizyka"
    oceny_p1 = []
    oceny_p2 = []
    oceny_p3 = []
    
    def __init__(self,imie,nazwisko,indeks) -> None:
        self.imie = imie
        self.nazwisko =nazwisko
        self.indeks = indeks
        
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
            case "analiza":
                self.oceny_p1.append(ocena)
            case "algebra":
                self.oceny_p2.append(ocena)
            case "fizyka":
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
            case "analiza":
                return f"Oceny z {przedmiot.lower()}  dla ucznia {self.imie, self.nazwisko} =  {self.oceny_p1} "
            case "algebra":
                return f"Oceny z {przedmiot.lower()}  dla ucznia {self.imie, self.nazwisko} =  {self.oceny_p2} "
            case "fizyka":
                return f"Oceny z {przedmiot.lower()}  dla ucznia {self.imie, self.nazwisko} =  {self.oceny_p3} "
            case default:
                pass
    def __str__(self,):
        return f"{self.imie} {self.nazwisko} oceny ucznia  \n analiza = {self.oceny_p1}  \n algebra = {self.oceny_p2}  \n fizyka = {self.oceny_p3} "
    
    
jan_kowalski = Student("Jan","Kowalski",266838)
anna_nowak = Student("Anna","Nowak",288564)
joanna_mucha = Student("Joanna","Mucha",234086)

#test metod dla JK
if __name__ == '__main__':
    print(jan_kowalski.dodaj_ocene("analiza",5))
    print(jan_kowalski)
    
