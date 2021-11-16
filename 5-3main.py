class Student:
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
        match przedmiot.lower():
            case "analiza":
                self.oceny_p1.append(self.ocena)
            case "algebra":
                self.oceny_p2.append(self.ocena)
            case "fizyka":
                self.oceny_p3.append(self.ocena)
            case default:
                pass
        return f"Dodano ocenę {self.ocena} do przedmiotu {self.przedmiot}" 
    
    def wyswietl_oceny(self,przedmiot):
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
print(jan_kowalski)
