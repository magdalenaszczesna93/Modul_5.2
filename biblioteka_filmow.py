class filmy:
    def __init__ (self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen
    def __str__ (self):
        return f'{self.tytul} ({self.rok_wydania})'
    def __repr__ (self):
        return f'{self.tytul} ({self.rok_wydania}) {self.gatunek} {self.liczba_odtworzen}'

#jak zorbić żeby to zwięskzało na stałę listę odtworzeń i za każdym razem dodawało?
def play (self):
        self.liczba_odtworzen += 1
        return f'{self.tytul} odtworzono {self.liczba_odtworzen} razy.'

movie1 = filmy(tytul='Dogs', rok_wydania='1994', gatunek='komedia', liczba_odtworzen=20)
movie2 = filmy(tytul='Cats', rok_wydania='1995', gatunek='dokumentalny', liczba_odtworzen=10)
movie3 = filmy(tytul='Tiger', rok_wydania='1998', gatunek='biograficzny', liczba_odtworzen=25)
movie4 = filmy(tytul='Home', rok_wydania='2005', gatunek='horror', liczba_odtworzen=35)

class seriale(filmy):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
    def __str__ (self):
        return f'{self.tytul} S{self.numer_odcinka:02d}E{self.numer_sezonu:02d}'
    def __repr__ (self):
        return f'{self.tytul} S{self.numer_odcinka:02d}E{self.numer_sezonu:02d} ({self.rok_wydania}) {self.gatunek} {self.liczba_odtworzen}'
    

def play (self):
        self.liczba_odtworzen += 1
        return f'{self.tytul} odtworzono {self.liczba_odtworzen} razy.'

series1 = seriale(tytul='The Simpsons', rok_wydania='1994', gatunek='komedia', liczba_odtworzen=20, numer_odcinka= 1, numer_sezonu= 1)
series2 = seriale(tytul='Game of Thrones', rok_wydania='2000', gatunek='obyczajowy', liczba_odtworzen=45, numer_odcinka= 1, numer_sezonu= 1)
series3 = seriale(tytul='Friends', rok_wydania='1995', gatunek='komedia', liczba_odtworzen=35, numer_odcinka= 1, numer_sezonu= 1)
series4 = seriale(tytul='Star Trek', rok_wydania='2004', gatunek='horror', liczba_odtworzen=10, numer_odcinka= 1, numer_sezonu= 1)

print(play(movie1))
print(movie1)
print(play(movie1))
print(movie1)
print(play(series2))
print(series2)
print(play(series2))
print(series2)
print(series3)

lista_all = []
lista_all.append(movie1)
lista_all.append(movie2)
lista_all.append(movie3)
lista_all.append(movie4)
lista_all.append(series1)
lista_all.append(series2)
lista_all.append(series3)
lista_all.append(series4)
print(lista_all)
